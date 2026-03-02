# How To Start
26.2.7版
## 车载端
需要先启动车载端，因为VLFM接收basr_link2map的变换，中间有odom的桥接，需要等待map2odom初始化完成后才能启动服务器端
  
集成到了一个launch文件中：
``` bash
roslaunch scout_bringup bringup_all.launch
```

## 服务器端
`/home/sxz/sjd/vlfm`下：
``` bash
conda activate /home/yyw/miniconda3/envs/vlfm-py39
```
``` bash
python -m vlfm.final_0206.py
```

## win转发端

``` bash
ssh -N -L 9000:localhost:9000 -p 2222 sxz@10.208.40.25
```
Anaconda Prompt中
``` bash
G:
cd \Datas\VLA\vlfm
```
``` bash
python win_bridge.py
```