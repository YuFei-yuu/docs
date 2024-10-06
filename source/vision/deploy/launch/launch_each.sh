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


#### ros启动环境
source /opt/intel/openvino_2021/bin/setupvars.sh
source /opt/ros/$ROS_DISTRO/setup.bash
source ${CWORK_SPACE}/install/setup.bash

#### 启动节点
log_meg "launch $package $launchscript"
time=`date +"%F-%T"`
ros2 launch $package $launchscript | tee ${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log 
# >${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log 2>${WORK_SPACE}/launch/logs/${time}_launch_$package_${launchscript%.*}.log

exit 0
