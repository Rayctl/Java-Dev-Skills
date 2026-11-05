"""Check catalog compatibility and malformed multi-turn fixtures."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_semantic_evals import validate_catalog


SCRIPT = Path(__file__).with_name("validate_semantic_evals.py")
CATALOG = SCRIPT.parent.parent / "evals" / "semantic-cases.json"


class CatalogValidationTest(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    def test_current_catalog_and_followups(self):
        self.assertEqual(validate_catalog(self.catalog), len(self.catalog["cases"]))
        self.assertTrue(any(case.get("followups") for case in self.catalog["cases"]))

    def test_schema_one_remains_compatible(self):
        self.catalog["schema_version"] = 1
        for case in self.catalog["cases"]:
            case.pop("followups", None)
        self.assertEqual(validate_catalog(self.catalog), len(self.catalog["cases"]))

    def test_version_is_an_integer_and_supported(self):
        for version in (True, 2.0, "2", 3):
            with self.subTest(version=version), self.assertRaisesRegex(
                ValueError, "schema_version_unsupported"
            ):
                validate_catalog({**self.catalog, "schema_version": version})

    def test_followups_require_schema_two(self):
        self.catalog["schema_version"] = 1
        with self.assertRaisesRegex(ValueError, "followups_require_schema_2"):
            validate_catalog(self.catalog)

    def test_followups_are_nonempty_and_well_formed(self):
        example = next(case for case in self.catalog["cases"] if "followups" in case)
        for bad in ([], {}, [None], [{"prompt": "continue"}]):
            with self.subTest(followups=bad), self.assertRaises(ValueError):
                validate_catalog({**self.catalog, "cases": [{**example, "followups": bad}]})

    def test_followup_prompt_and_assertions(self):
        example = next(case for case in self.catalog["cases"] if "followups" in case)
        for field, value in (
            ("prompt", " "),
            ("expected_decisions", []),
            ("disallowed_decisions", ["same", "same"]),
            ("unexpected_field", True),
        ):
            bad_case = copy.deepcopy(example)
            bad_case["followups"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_catalog({**self.catalog, "cases": [bad_case]})

    def test_unknown_case_fields_and_duplicate_ids(self):
        case = self.catalog["cases"][0]
        with self.assertRaisesRegex(ValueError, "fields_invalid"):
            validate_catalog({**self.catalog, "cases": [{**case, "typo": "value"}]})
        with self.assertRaisesRegex(ValueError, "id_duplicate"):
            validate_catalog({**self.catalog, "cases": [case, copy.deepcopy(case)]})

    def test_cli_reports_invalid_and_unreadable_catalogs(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "catalog.json"
            for content, code, status in (
                ("{", 1, "INVALID"),
                (json.dumps({**self.catalog, "schema_version": True}), 1, "INVALID"),
                (json.dumps(self.catalog), 0, "VALID"),
            ):
                path.write_text(content, encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, "-B", str(SCRIPT), str(path)],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertEqual(json.loads(result.stdout)["status"], status)
            missing = Path(folder) / "missing.json"
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), str(missing)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["reason"], "catalog_unreadable")


if __name__ == "__main__":
    unittest.main()
