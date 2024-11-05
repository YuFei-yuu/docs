# 待完成的从0开始配置舒适好用的NUC环境

## ToDesk
[下载链接](https://www.todesk.com/linux.html)

- 远控时黑屏/连接进度卡死在某个百分数：
    ```shell
    echo $XDG_SESSION_TYPE #查看图形接口协议
    ```
    如果返回结果为Wayland则说明是接口协议不符导致的，需要将Wayland禁用更改为X11
    - 编辑/etc/gdm3目录下的custom.conf文件
        ``` shell
        sudo vim  /etc/gdm3/custom.conf
        ```
    - 键入```i```进入编辑模式
    - 删掉```#WaylandEnable=false```前的注释符号
    - 键入```:wq```保存并退出
    - 重启电脑
    - 重新输入```echo $XDG_SESSION_TYPE```查看接口协议，输出为X11即可正常使用远程

## 搜狗拼音
尽管这显得非常呆但确实完美解决了中文输入问题 &nbsp;&nbsp;&nbsp;~~&nbsp;能走捷径谁愿意非要配出来ubuntu自带的中文输入呢&nbsp;~~

[下载链接](https://shurufa.sogou.com/linux/guide)

## QQ
没有人可以抗拒把报错信息直接复制粘贴给老登的诱惑

[下载链接](https://im.qq.com/linuxqq/index.shtml)

## VScode所需插件
反正原来的小电脑里这些都有，管他用不用得到呢
- WSL
- C/C++ Themes
- Dev Containers
- Remote-SSH
- Remote-SSH:Editing Configuration Files
- Remote-Tunnels
- Remote Development
- Remote Explorer
- Baidu Comate
<BR>
<font color="gray">docker外：</font>
- C/C++
- C/C++ Extension Pack
- CMake
- CMake Tools
- Docker
- Pylance
- Python
- Python Debugger
- Savr Typing
- Serial Monitor
- vscode-pdf

## 一些没用的小技巧
- Ctrl+shift+C/V 终端中复制粘贴
- Ctrl+F 文件内查找