# 已迁移至 Git Safe Collaboration

正式 Skill 为 [git-safe-collaboration](../git-safe-collaboration/README.md)，调用 `$git-safe-collaboration`。

本目录不是第二套 Skill，不含 `SKILL.md` 或调用元数据。仅暂留 `scripts/git_latest_code.py` 作为旧 CLI 路径转发；实际执行新目录下的 `scripts/git_safe_collaboration.py`，使用相同参数、状态与退出码。导入旧 Python 模块不属于兼容接口。

请更新全局规则、工具命令和收藏路径。在途会话若仍尝试读取旧 `SKILL.md`，应改读新目录的 `SKILL.md`，不要从旧摘要重建规则。不需要重命名聊天工作区或改写历史提交。

此兼容层依赖相邻的正式 Skill；部署或保留兼容入口时须同时安装新目录。确认旧调用方迁移完毕后可单独移除本目录。旧安装目录会备份到 Skill 扫描范围外，避免维护两套完整规则。
