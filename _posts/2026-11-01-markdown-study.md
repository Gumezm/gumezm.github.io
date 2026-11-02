---
title: Markdown编写学习
date: 2026-11-01 14:00:00 +0800
categories: [随笔]
tags: [Markdown]
math: true
---

## 一、准备工作

##### 1. 安装VS Code

##### 2. 下载插件

- MEO Enhanced - Markdown Editor
- Markdown Preview Enhanced
- Paste Image

##### 3. 创建.md文件，打开同步预览功能，开始编辑

## 二、基本语法

##### 1. 标题

```
#一级标题
##二级标题
......
```

##### 2. 引用

```
>使用">"来进行嵌套
>>当然使用">>"也能够叠加嵌套
```

>使用">"来进行嵌套
>>当然使用">>"也能够叠加嵌套

##### 3. 列表

**无序列表**

- 列表 **+**
- 列表 **-**
- 列表 **\***

**有序列表**

```
使用"数字."的形式
1. A
2. B
...
```

**嵌套**

**TodoList**

```
格式
- [ ] aaa
- [x] bbb
```

- [ ] aaa
- [x] bbb

##### 4. 表格

```
| 左对齐 | 居中对齐 | 右对齐 |
| :---- | :----: | ----: |
| a | b | c |
```

| 左对齐 | 居中对齐 | 右对齐 |
| :---- | :----: | ----: |
| a | b | c |

##### 5. 段落

- **换行**  —— 两个及以上空格回车/空一行

- **分割线** —— 三个 **\***

***

- **字体**

| 字体 | 代码 |
| :---: | :---: |
| *斜体* | `* *` |
| **粗体** | `** **` |
| ***斜粗体*** | `*** ***` |
| ~~删除~~ | `~~ ~~` |
| <u>下划线</u> | `<u> </u>` |

- **脚注**

    点击这里[^1]跳转至脚注

##### 6. 代码

```GDScript
extend Node2D

func _ready() -> void:
  print("Hello World")
```

`Hello World`

##### 7. 超链接

- 进入我的Github:<https://github.com/gumezm>
- 进入我的[Github][Github]

##### 8. 图片

- **图床**(不推荐)
- **格式**:`[![图片说明](图片URL)](跳转URL)`

![Medic](https://gumezm.github.io/assets/img/gallery/2026-10-31-Medic-Cat.webp)

- 使用**HTML**来调整图片大小和位置

<img src="https://gumezm.github.io/assets/img/gallery/2026-10-31-Medic-Cat.webp" width="50" alt="Medic Cat">

## 三、其他操作

- **插入latex公式**

    - 行内显示：$f(x)=ax+b$

    - 块内显示：

$$
\begin{aligned}
a &= b + c \\
d &= e + f
\end{aligned}
$$

- **使用html/css语法**

    - 使用VSCode插件"Markdown Preview Enhanced:Customize CSS"
    - 在style中使用css语法改标题格式
    - ......

[Github]:https://github.com/gumezm

[^1]: 这里就是脚注了
