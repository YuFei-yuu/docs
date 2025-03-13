# 换边（改初始点
## 建图
1. 录制点云
    ```bash
    ros2 bag record /livox/lidar /livox/imu
    ```
    录下来的包在执行这条命令的目录下，可以加`-o /path/to/your/bagfile`来指定路径和文件名
2. 开始建图
    ```bash
    ros2 launch sentry_bringup mapping.launch.py
    ```
   - 
       ```bash
       ros2 run nav2_map_server map_saver_cli -t /projected_map -f test_map --fmt png
       ```
    - 
       ```bash
       ros2 service call /map_save std_srvs/srv/Trigger
       ```
3. 在起始点和换边之后的起点狠狠地多停一段时间
4. 直接ctrl+c结束

## 重定位
1. 更改`relocalization.launch.py`
    ```python
    ld.add_action(mid360_node)  # 接入雷达，用录下来的包的点云时注释掉
    ```
2. 启动重定位
    ```bash
    ros2 launch sentry_bringup relocalization.launch.py
    ```
3. 输出发布点的坐标
    ```bash
    ros2 topic echo /clicked_point
    ```
4. 播放录制下来的点云
    ```bash
    ros2 bag play /filepath/file.db3
    ```
5. 开始重定位，等到换边的地方publish point，记录播放到这里经过的秒数

## 换边
1. 修改`relocalization.launch.py`中对应的坐标
    ```python
    # --- Blue ---
    # {'initial_x':14.16},
    # {'initial_y':5.35},
    # {'initial_z':0.0},
    # {'initial_a':3.14},

    # --- Red ---
    {'initial_x':0.0},
    {'initial_y':0.0},
    {'initial_z':0.0},
    {'initial_a':0.0},
    ```
2. 测试
    ```bash
    ros2 launch sentry_bringup relocalization.launch.py
    ```
    ```bash
    ros2 bag play /filepath/file.db3 --start-offset 111
    ```
    --start-offset设置开始播放的秒数<br><br>


---
<br>

- 检查录制是否成功<br>
ros2 bag info /path/to/your/bagfile<br>
如果有topic information就成功了，还有start和end的时间


