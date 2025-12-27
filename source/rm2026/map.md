# 不建图导航

## 获取栅格地图

[CloudCompare](https://www.cloudcompare.org/)

Edit > Mesh > Sample Points

cut

Tools > Projection > Rasterize

图像 > 图像大小 280*150

灰度 阈值

## 使用栅格地图导航

ros2 launch sentry_bringup navigation.launch.py

ros2 topic echo /clicked_point

ros2 launch sentry_bringup bringup_without_relocalization.py

## 视频教程已更新

[并非无图导航的无图导航](https://www.bilibili.com/video/BV1p2spz2EG1/?share_source=copy_web&vd_source=39b6d1d3c9ea7d9c3748b1b07ca91aeb)

文字版懒得写了~