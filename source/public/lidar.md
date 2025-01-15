# 雷达网络配置相关

## 本地
在设置里添加有线
IPv4：192.168.1.50
子网掩码：255.255.255.0

## 查看雷达ip
[livox viewer下载地址](https://www.livoxtech.com/cn/mid-360/downloads)

- 设置本地ip：

    win11下 设置-网络和Internet-以太网-IP分配-手动-192.168.1.50-255.255.255.0
- 打开livox viewer，左上角refresh，找到192.168.1.50，点击设置，查看雷达ip

## 更改雷达配置
``/home/sentry_ws/src/livox_ros_driver2/config/MID360_config.json``
```json
"lidar_configs" : 
      "ip" : "192.168.1.XXX",
```
```shell
colcon build --packages-select livox_ros_driver2
```

## 检测方法
docker内外ping雷达

```shell
ros2 launch livox_ros_driver msg_MID360_launch.py
```
