# 简明编写文档教程

## 克隆仓库

首先获得仓库的写权限，然后clone仓库到本地

```bash
git clone xxx
```

## 新建文档

1. 在对应的文件夹下创建一个markdown文档，如source/control/gimbal/template.md

文件树
```bash
source
├── control
│   └── gimbal
│       ├── index.rst
│       └── template.md
```

2. 写入文档内容，注意只能有一个一级标题，如# 云台控制

```markdown
# 云台控制

## 云台控制简介

balabala

## 云台控制实现

balabala

## Author

张三
```

3. 如果要加入图片，在对应的文件夹下创建一个pic文件夹用于存放图片

文件树
```bash
source
├── control
│   └── gimbal
│       ├── index.rst
│       ├── pic
│       │   └── robomaster.png
│       └── template.md
```

4. 在对应的文件夹内的index.rst中添加文档的链接，如在source/control/gimbal/index.rst中，toctree的最后一行添加template.md，就是刚才写的文档名

   ```rst
   .. toctree::
      :maxdepth: 2

      ./template.md
   ```

## 提交文档【重要】

提交文档请遵循commit message规范!

最简单的commit message格式如下：

```bash
doc: add gimbal control tutorial
```

推送，等待自动构建完成，访问[https://scurm-knowledgebase.readthedocs.io/zh/latest/index.html](https://scurm-knowledgebase.readthedocs.io/zh/latest/index.html)查看效果。

## Markdown语法

添加图片

    ![图片](./pic/robomaster.png)

![图片](./pic/robomaster.png)

或者这样可以指定图片大小

    <img src="./pic/robomaster.png" width="10%">

<img src="./pic/robomaster.png" width="10%">

超链接

    [链接](https://www.google.com)

[链接](https://www.google.com)

代码块

    ```python
    print("Hello World")
    ```

```python
print("Hello World")
```

表格

    | 1 | 2 | 3 |
    |---|---|---|
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

列表

    - 1
    - 2
    - 3

- 1
- 2
- 3

有序列表

    1. 1
    2. 2
    3. 3

1. 1
2. 2
3. 3

引用

    > 这是一个引用

> 这是一个引用

加粗

    **加粗**

**加粗**

斜体

    *斜体*

*斜体*

删除线

    ~~删除线~~

~~删除线~~

行内代码

    `行内代码`

`行内代码`

数学公式（支持latex）

    $$
    \frac{1}{2}
    $$

$$
\frac{1}{2}
$$

## 常犯的错误

index.rst有严格的空行和缩进要求，不要随意添加空行和缩进

只有这样才能正确地构建文档

```rst
.. 这一行用于分割不同的toctree
.. _vision_tutorial:

.. 这一行是页面标题
视觉&导航入门教程
#######################

.. 这里是toctree，用于链接其他文档
.. 这里的每一个空行和缩进都是有意义的，不要随意添加
.. toctree::
   :maxdepth: 1

   1-c++/c++培训笔记.md
   2-linux环境配置/linux-note.md
   3-opencv-cpp/opencv-cpp.md
   4-ros/ros.md
   AutoCarControl/autoCar.md

```