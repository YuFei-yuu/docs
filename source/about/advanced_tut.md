# 文档管理进阶教程

## 什么是sphinx

Sphinx是一个基于Python的文档生成工具，它可以将你的文档写成一个标准的rst文件，然后通过sphinx生成一个漂亮的html文档。

使用rst是其标准的写法，当然也支持markdown，但是markdown的功能相对较少，如果你想要更高级的排版，建议使用rst。

## 官方教程

[官方教程](https://www.osgeo.cn/sphinx/index.html)

## 环境配置（如果你想在本地生成文档）

1. 创建python虚拟环境

此处使用conda，你也可以使用pipenv或者virtualenv

```shell
conda create -n sphinx python=3.7
```

2. 激活虚拟环境

```shell
conda activate sphinx
```

3. 安装sphinx

```shell
pip install sphinx
```

4. 从requirements.txt安装依赖

```shell
pip install -r requirements.txt
```

5. 生成文档

```shell
make html

# 生成其他格式的文档
make latexp
make pdf
make epub

```

6. 查看文档

使用浏览器打开`build/html/index.html`即可查看文档

## 文档git管理

本文档使用git进行版本管理，同样有锁定文档、提交权限设置、分支管理等功能。

## reStructuredText教程


主要就是支持更高级的排版

[reStructuredText教程1](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
)

[reStructuredText教程2](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)