# 点云处理

## CloudCompare

[下载链接](https://cloudcompare-org.danielgm.net/release/
)

1. 打开文件：File -> Open （.pcd类型）
2. 鼠标左键旋转，右键平移，单击选中
3. 滤波去除离群点：Tools -> Clean -> SOR filter
    - Number of points to use for mean distance estimation ：用于估计平均距离的点数，判断一个点是否为离群点，较小时容易移除有效数据点
    - Standard deviation multiplier threshold (nSigma)：标准差乘数阈值，
    - 设置合适的参数 (25,1 作为参考) 然后 apply