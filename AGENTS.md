# 工作区记忆（D:\Code\Blog）

## 协作流程（必须遵守）

1. **用户提问，我只负责修改。** 不主动扩大范围、不顺手重构无关文件。
2. **修改后立即 `git add`。** 只暂存，不 commit。
3. **保持博客端口可见。** 本地预览服务常驻（默认 `bundle exec jekyll serve --livereload`，端口 4000），供用户随时打开检查；不要随意关闭或反复重启。
4. **不要 commit / push 到 GitHub。** 用户检查完并明确说 **c&p** 之后才执行。
5. **c&p = commit + push。** 用户用该简写时，先 `git add` 全部相关改动，再 commit，再 push 到远端。

## 交付方式

- 每次修改后给出：改了哪些文件、预览地址、需要检查的点。
- 未完成项明确列出，不要声称已完成。

## 构建与验证

- 构建：`bundle exec jekyll build`
- 本地预览：`bundle exec jekyll serve --livereload`（http://127.0.0.1:4000）
- 本文件已加入 `_config.yml` 的 `exclude`，不会发布到站点。
