# Blog · 开发计划

## 当前目标

持续维护 Gumezm 个人博客：Chirpy 主题 + EF/ORI 双风格、静态相册、GitHub Pages 发布。
当前同时跟踪四条工作流：EF 主题细节打磨、相册维护与扩充、文章写作与内容、部署与站点基础设施。

2026-11-03 完成一轮全文件审计（不改代码），发现的问题整理为 P08–P14，明细见文末「审计发现」。

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
| P08 | 站点隐私与可访问性修正：`_config.yml` exclude 加 `plan.md`（现已泄露到公开站点）、head.html 去掉 `user-scalable=no`、theme-color 对齐 EF 纸色 | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | infra | 审计发现 A1/A2/A5，改动小、收益高，建议最先做 |
| P09 | EF 第二强调色清理：青绿 `--ef-link-hover` hover 改为语言内方案（去色 + 下划线变墨色），删除该 token | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | theme | 审计发现 A3（即此前审计的 P1）；违反「唯一强调色」法则 |
| P10 | EF 头像配置化：`_config.yml` 增加 `avatar_ef`，sidebar.html 改读配置；顺手清理 `#avatar img` 的双重 border 规则（1px 与 0 冲突） | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | theme | 审计发现 A4/A8；以后换头像只改一处 |
| P11 | 文章排版规范：重排 markdown-study 的 11 处 `#####` 步骤标题（改列表/加粗，让 TOC 回归章节级）；沉淀写作约定（标题层级、图片引用相册文件名） | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | content | 审计发现 A6；涉及正文改写，等用户确认再动 |
| P12 | 分享预览图：设置 `social_preview_image`（og:image），补社交分享卡片 | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | infra | 审计发现 B6；可选一张站标图 |
| P13 | 自定义域名落地：CF Pages 与 GitHub Pages 的取舍定案后，统一改 `url`/CNAME/DNS | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | infra | 审计发现 B5；依赖用户在 Cloudflare 侧的决策，暂缓 |
| P14 | EF 字号阶梯收敛（17 种一次性字号 → 5 档）+ 首页列表行键盘焦点补底色 | 未开始 | 未记录 | 未记录 | 未记录 | main | planned | theme | 审计发现 A9（即此前审计的 P3）；锦上添花 |

## 计划变更记录

后续调整保留已有任务编号，新增任务使用新的唯一编号；在此记录新增、调整或取消的编号、原因及挂接关系，不将记录重复计为任务。

| 日期 | 变更 | 涉及编号 | 原因 |
| --- | --- | --- | --- |
| 2026-11-02 | 初始建立 | P01–P07 | 看板初始化：P01–P03 依据现有提交记录整理为基线，P04–P07 为当前四条工作流的后续任务 |
| 2026-11-03 | 新增 | P08–P14 | 2026-11-03 全文件审计：扫描 config、布局、插件、数据、脚本、CI 与 `_site` 产物，按严重度立任务；P04 保留为 EF 走查的总项 |

## 审计发现（2026-11-03，只审计未改代码）

已核实的错误与隐患，已全部立为任务：

- **A1（P08，重要）**：`plan.md` 无 front matter，被 Jekyll 当静态文件拷进 `_site`，正在公开站点发布（`/plan.md` 可直接访问）。修法：`_config.yml` 的 `exclude` 增加 `plan.md`。
- **A2（P08）**：`head.html` 的 viewport 带 `user-scalable=no`，禁止双指缩放，WCAG 1.4.4 可访问性问题（继承自模板）。
- **A5（P08）**：`theme-color` 是 `#f7f7f7`/`#1b1b1e`，与 EF 纸色 `#f4f4f2`/`#191919` 不一致，移动端浏览器框出现色差。
- **A3（P09）**：EF 链接 hover 用青绿 `#2dbaba`，是黄色之外的第二强调色，违反设计语言的「唯一强调色」。
- **A4/A8（P10）**：EF 头像文件名硬编码在 `sidebar.html`（换头像要改两处）；`#avatar img` 的 border 规则写了两次（1px 与 0），后者实际生效。
- **A6（P11）**：`markdown-study` 用 11 个 `#####` 当步骤编号，TOC 冗长、层级失真。
- **B6（P12）**：`social_preview_image` 未设置，社交分享无预览图。
- **B5（P13）**：域名决策悬置——`_config.yml` 仍是 `url: https://gumezm.github.io`，www.seija.org 的接入等 CF Pages 定案。
- **A9（P14）**：字号一次性值 17 种；列表行键盘焦点只有黄条无底色变化。

审计中确认无问题的部分：布局与插件的 Liquid 逻辑（首页置顶分页、相册排序、灯箱）、`ef-theme.js` / `mode-toggle.js` 的持久化与跨标签同步、`tools/process-gallery.py`（EXIF 清除、命名去重）、`pages-deploy.yml`（分支发布避开部署锁）、`Gemfile` 与 `gallery.yml`。前两轮已完成未提交的修正：提示块图标对齐、死代码清理（`--ef-snap`/`--ef-danger`/prompt 重复规则）、EF 方形头像——已在 2026-11-03 随提交 `e5fca3c` 发布。
