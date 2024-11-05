# SCURM KnowledgeBase

## 构建状态

[ReadTheDOCS](https://readthedocs.org/projects/flyingfish/)<BR>
[一只飞鱼](https://scurm-knowledgebase.readthedocs.io/zh/latest/)

## 使用方式

1. 在对应的文件夹下创建一个markdown文档，如source/control/gimbal/template.md

2. 写入文档内容，注意只能有一个一级标题，如# 云台控制

3. 如果要加入图片，在对应的文件夹下创建一个pic文件夹用于存放图片

4. 在对应的文件夹内的index.rst中添加文档的链接，如在source/control/gimbal/index.rst中，toctree的最后一行添加template.md（刚才写的文档名）

   ```rst
   .. toctree::
      :maxdepth: 2

      ./template.md
   ```

## 一些命令
``` shell
./make html #在本地.\build\html\index.html预览
```
``` shell
git add .
```
``` shell
git commit -m "bulabula"
```
``` shell
git push origin master 
```