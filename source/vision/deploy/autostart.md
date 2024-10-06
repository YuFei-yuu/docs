# init_tools 自启动脚本

## 1. 启动脚本

在工作空间新建`launch`文件夹，在该文件夹下新建三个文件：`launch_daemon.sh`、`launch_each.sh`、`launch_ext.sh`。

如果需要启动不同工作空间的节点，同样在工作空间新建`launch`文件夹，在该文件夹下新建两个文件：`launch_each.sh`、`launch_ext.sh`。

注意需要更改的几个地方：

1. `launch_daemon.sh` 中的工作目录和 ros 启动节点
2. `launch_each.sh` 中的工作目录和 ros 启动环境，包括ros2版本

`launch_daemon.sh` 文件内容如下：

```bash
#!/bin/sh

log_meg(){
        time=`date +"%F %T"`
        echo "[INFO] [$time]: $1"
}

process_monitor(){
  NUM=`ps -ef | grep $2 | grep -v grep | wc -l` 
  #Get the number of processes based on the process name

  if [ "${NUM}" -lt "1" ];then #If the number of processes is less than 1, start a new process
	log_meg "$1 $2 not exists, will launch..."
	# sh ${WORK_SPACE}/launch/launch_each.sh $1 $2
	gnome-terminal -- bash -c "bash ${WORK_SPACE}/launch/launch_each.sh $1 $2;exit;"
 #  If the number of processes is greater than 1, kill all processes and restart a new process with the same name
  elif [ "${NUM}" -gt "3" ];then
	log_meg "more than 1 $1,killall $1"
	kill -9 $(ps -ef|grep $1|grep -v grep|awk '{print $2}')
	# sh ${WORK_SPACE}/launch/launch_each.sh $1 $2
	gnome-terminal -- bash -c "bash ${WORK_SPACE}/launch/launch_each.sh $1 $2;exit;"
	# gnome-terminal -x bash -c "sh ~/daemon_script/run_total.sh $2;exec bash;"
  fi
#    Kill zombie processes
   NUM_STAT=`ps aux | grep $1 | grep T | grep -v grep | wc -l` 
 
  if [ "${NUM_STAT}" -gt "0" ];then
   	kill -9 $(ps -ef|grep $1 |grep -v grep|awk '{print $2}')
  fi
}

while true
do
    #### 设置工作目录
    WORK_SPACE=/home/scurm/sentry_workspace/scu_rm_ros
    cd $WORK_SPACE
    #### 设置启动节点
    process_monitor rm_sentry sentry_imu_up.launch.py
sleep 3s
    #### 同一工作空间的其他节点
    process_monitor rm_sentry sentry_all_up.launch.py
sleep 0.1
    #### 不同工作空间的节点
    #### 设置工作目录
    WORK_SPACE=/home/scurm/sentry_workspace/scu_rm_ros
    cd $WORK_SPACE
    #### 设置启动节点
    process_monitor rm_sentry sentry_imu_up.launch.py
done # 结束循环
sleep 0.1

exit 0
```

`launch_each.sh` 文件内容如下：

```bash
#!/bin/sh

log_meg(){
        time=`date +"%F %T"`
        echo "[INFO] [$time]: $1"
}

#### 设置工作目录
WORK_SPACE=/home/scurm/sentry_workspace/scu_rm_ros
CWORK_SPACE=/home/scurm/sentry_workspace/scu_rm_ros

package=$1
launchscript=$2

#### 启动环境和ROS版本
source /opt/intel/openvino_2021/bin/setupvars.sh
source /opt/ros/$ROS_DISTRO/setup.bash
source ${CWORK_SPACE}/install/setup.bash

#### 启动节点
log_meg "launch $package $launchscript"
time=`date +"%F-%T"`
# 如果logs文件夹不存在则创建
if [ ! -d "${WORK_SPACE}/launch/logs" ]; then
  mkdir ${WORK_SPACE}/launch/logs
fi
ros2 launch $package $launchscript | tee ${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log 
# >${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log 2>${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log

exit 0
```

`launch_ext.sh` 文件内容如下：

```bash
#!/bin/sh

ps -ef | grep launch_daemon | grep -v grep | awk '{print $2}' | xargs kill -9
ps -ef | grep ros | grep -v grep | awk '{print $2}' | xargs kill -9

exit 0
```

## 2. 设置启动脚本

在 `/home/scurm/rm_ws/launch/launch_daemon.sh` 中设置工作目录和 ros 启动节点

在 `/home/scurm/rm_ws/launch/launch_each.sh` 中设置工作目录和 ros 启动环境

## 3. 设置自启动

在 ubuntu startup application 中添加 `/home/scurm/rm_ws/launch/launch_daemon.sh`

## 停止自启动进程的方法

```bash
./launch_ext.sh
```
