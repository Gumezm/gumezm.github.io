# Blog · 开发计划

## 当前目标

持续维护 Gumezm 个人博客：Chirpy 主题 + EF/ORI 双风格、静态相册、GitHub Pages 发布。
当前同时跟踪四条工作流：EF 主题细节打磨、相册维护与扩充、文章写作与内容、部署与站点基础设施。

## 开发计划

任务顺序只表示计划展示顺序；未声明阻塞依赖。开发、自动验证、用户验收与交付分别记录。

| ID | Task | Development | Verification | Acceptance | Delivery | Route | Origin | Workstream | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | EF 主题层：`html[data-ef="ef"]` 作用域样式、侧栏样式切换、EF 脚本 | 已完成 | 未记录 | 未记录 | 未记录 | main | recorded | theme | 依据提交 `b4f01f7` 及后续 EF 系列提交；EF 样式与脚本带构建版本号 |
| P02 | 静态相册：`_data/gallery.yml`、年份分组、灯箱、`tools/process-gallery.py` | 已完成 | 未记录 | 未记录 | 未记录 | main | recorded | gallery | 依据提交 `8dbd51c`、`6b804e1`；图片命名为 `YYYY-MM-DD-名称` |
| P03 | GitHub Pages 发布链路：构建站点并推送 `gh-pages` 分支 | 已完成 | 未记录 | 未记录 | 未记录 | main | recorded | infra | 站点只托管在 GitHub Pages；其余托管方案已停用 |
| P04 | EF 主题细节走查与修正（页眉、导航、文章排版、动效） | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | theme | 延续 EF 系列提交的细粒度修正方式，发现即修，不单独立项 |
| P05 | 相册扩充：新照片压缩、命名、重跑 `tools/process-gallery.py` | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | gallery | 手工维护的 tags 重跑时保留；总量不超过 200 张 |
| P06 | 新文章写作：正文、图片、分类与标签 | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | content | 文章图片引用相册文件名 |
| P07 | 站点基础设施维护：构建版本号/缓存、404、主题切换等 | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | infra | 避免浏览器缓存旧样式 |

## 计划变更记录

后续调整保留已有任务编号，新增任务使用新的唯一编号；在此记录新增、调整或取消的编号、原因及挂接关系，不将记录重复计为任务。

| 日期 | 变更 | 涉及编号 | 原因 |
| --- | --- | --- | --- |
| 2026-11-02 | 初始建立 | P01–P07 | 看板初始化：P01–P03 依据现有提交记录整理为基线，P04–P07 为当前四条工作流的后续任务 |
