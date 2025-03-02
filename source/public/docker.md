# docker安装相关

## 配置docker环境

参考：

[学姐的馈赠](https://polaris-notebook.readthedocs.io/zh-cn/latest/develop/Docker/docker.html)

[VScode-doeker官方文档](https://code.visualstudio.com/docs/devcontainers/tutorial)

[CSDN-wsl及docker安装](https://blog.csdn.net/weixin_43726471/article/details/122267300)

[CSDN-Windows安装Docker并创建Ubuntu环境](https://blog.csdn.net/laoxue123456/article/details/133526607)

安装过程状况百出……没有Hv和容器选项需要自己写.bat文件下载

在users\hp里要写个.wslconfig文件（似乎网络相关

[下载Xlaunch](https://blog.csdn.net/zhouzhiwengang/article/details/139729949)

从coding拉取镜像登录用户名是邮箱 docker login huoguozhandui-docker.pkg.coding.net


拉取命令：docker pull huoguozhandui-docker.pkg.coding.net/24vision_nav/sentry_dockerhub/rm_sentry:latest0408



    PS C:\Windows\system32> docker pull ubuntu
    Using default tag: latest
        latest: Pulling from library/ubuntu
    9c704ecd0c69: Pull complete
    Digest: sha256:2e863c44b718727c860746568e1d54afd13b2fa71b160f5cd9058fc436217b30
    Status: Downloaded newer image for ubuntu:latest
    docker.io/library/ubuntu:latest

    What's next:
        View a summary of image vulnerabilities and recommendations → docker scout quickview ubuntu
    PS C:\Windows\system32> docker run -it --name test1 ubuntu

    root@a3a2bb9fb0e1:/# ls
        bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@a3a2bb9fb0e1:/# exit
        exit

    PS C:\Windows\system32> docker ps -a
        CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                     PORTS     NAMES
        a3a2bb9fb0e1   ubuntu    "/bin/bash"   33 seconds ago   Exited (0) 3 seconds ago             test1

    PS C:\Windows\system32> docker run -it --name test1 -v I:/Docker:/data ubuntu bash

    root@28fc2e21cac7:/# ls
        bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@28fc2e21cac7:/# ls
        bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
    root@28fc2e21cac7:/# ls /data/
        1
    root@28fc2e21cac7:/#exit
        exit


### 启动命令:

**25.3.1更新**
``` bash
 docker run --name 25nav --gpus all -dit --ipc=host --net=host --privileged -e DISPLAY=host.docker.internal:0.0 -e NVIDIA_DRIVER_CAPABILITIES=all -v F:\yu:/data g-dvxc1780-docker.pkg.coding.net/25nav/docker/25nav:0301
 ```


在I:/rm文件夹中挂载data
    docker run -it --name rm_try --network=host --privileged -e DISPLAY=${DISPLAY} -v F:\rm:/data huoguozhandui-docker.pkg.coding.net/24vision_nav/sentry_dockerhub/rm_sentry:latest0408 bash

终端连接到容器：
docker attach rm

退出容器：exit

**[图形化](https://blog.csdn.net/zhouzhiwengang/article/details/139729949)**

    echo "export DISPLAY=192.168.18.1:0.0" >> ~/.bashrc
    source ~/.bashrc
    Xlaunch启动时display number改成0；
    ipconfig改成本机ip

**二轮期间更新：上面的通通不要管，直接改启动命令：--ipc=host --net=host(参照25.3.1更新)
（此时不要改bashrc不然反而出问题**


X11apps 测试用
```shell
    apt-get update && apt-get install -y x11-apps
```

---

### 24.9.15更新：docker镜像存储位置问题
直接手改，复制粘贴删除一气呵成，亲测有效()

下载好desktop之后在设置里就会有一个镜像存储路径（本人是C:\Users\hp\AppData\Local\Docker\wsl

先尝试一下直接点browse，能改的话万事大吉但我估计大概率不行，会显示docker_data.vhdx无法移动，推测原因是打开了desktop这个文件就会开始运行然后就没法移动了

1. 终止所有容器，完全关闭desktop，可以用wsl --list -v测试
2. 把C:\Users\hp\AppData\Local\Docker\wsl\disk目录下的docker_data.vhdx移动到你需要的路径下（如F:\Docker\DockerDesktopWSL）
3. 把原来的docker_data.vhdx删除（注意main文件夹下ext4.vhdx不要动，至少本人动他就会定位不到，反正这个也就138MB留着他吧还是另一个.vhdx比较占空间
4. 重新启动desktop，把设置里的路径更改到F盘，再重启看启动界面的镜像和容器有没有丢失。如果在设置里更改路径的时候显示比如说什么该文件夹下DockerDesktopWSL已存在之类的，善用文件夹重命名反复移动一下，最终只要实现了把docker_data.vhdx塞到DockerDesktopWSL\disk下且设置里定位的位置是F:\Docker\DockerDesktopWSL就没问题
