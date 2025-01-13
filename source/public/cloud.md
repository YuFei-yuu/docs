# 点云处理

## CloudCompare

[下载链接](https://cloudcompare-org.danielgm.net/release/
)

1. 打开文件：File -> Open （.pcd类型）
2. 鼠标左键旋转，右键平移，单击选中
3. 滤波去除离群点：Tools -> Clean -> SOR filter
    - Number of points to use for mean distance estimation ：用于估计平均距离的点数，判断一个点是否为离群点，较小时容易移除有效数据点
    - Standard deviation multiplier threshold (nSigma)：标准差乘数阈值，通常取值为1/2/3，对应不同的置信水平,较大时保留更多的点
    - 设置合适的参数 (25,1 作为参考) 然后 apply
4. 上一步会生成一系列点云，在其中选中想要的，删除不要的，合并他们
5. 选中合并好的点云，点击 ``tools->Other->Remove duplicate points``, 每 0.01-0.1m 保留一个点，减小点云的大小
6. 选中处理完的点云，点击 file->save as, 选择 .pcd format，保存

## 地形分析
1. 在``autonomous_exploration_development_environment/terrain_analysis_ext/launch/terrain_analysis_ext_offline.launch``中将点云路径改成处理好的点云
2. 
    ``` shell
    ros2 launch terrain_analysis_ext terrain_analysis_ext_offline.launch
    ```
3. 打开 rqt 选择 ``plugins->configuration->dynamic reconfigure``, 调整terrain_analysis节点的参数，直到坡面可以被正确分析为可通行，墙面可以被分析为不可通行(可通行区域为绿色，不可通行区域为红色)
4. 保存无残影的2D导航地图
    ```bash
    ros2 run nav2_map_server map_saver_cli -t /projected_map -f test_map --fmt png
    ```
    - 这个有问题 用ps吧
