# 雷达网线配置相关

## 本地
在设置里添加以太网
IPv4：192.168.1.50
子网掩码：255.255.255.0

## 查看雷达ip
[livox viewer下载地址](https://www.livoxtech.com/cn/mid-360/downloads)

设置本地ip
refresh
点设置查看雷达ip

24.10.30：雷达静态ip192.168.1.3

## 检测方法
docker内外ping192.168.1.3

只launch livox ros driver（livox_ros_driver/launch_ROS2/msg_MID360_launch.py）