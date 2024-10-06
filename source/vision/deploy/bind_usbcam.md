# 部署之绑定多个USB摄像头

## 1.插入其中一个摄像头

## 2.查看设备信息

```bash
lsusb

# Bus 004 Device 002: ID 0781:558b SanDisk Corp.
# Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
# Bus 003 Device 007: ID 0c45:6366 Elan Microelectronics Corp.
# Bus 003 Device 005: ID 5986:212b Acer, Inc
# Bus 003 Device 022: ID 0a0a:5846
# Bus 003 Device 021: ID 0b95:772b ASIX Electronics Corp. AX88772B
# Bus 003 Device 020: ID 062a:4c01 Creative Labs
# Bus 003 Device 019: ID 093a:4202 Pixart Imaging, Inc.
# Bus 003 Device 018: ID 0c46:636a WaveRider Communications, Inc.
# Bus 003 Device 017: ID 14cd:8608 Super Top
# Bus 003 Device 009: ID 8087:0026 Intel Corp.
```

记录idVendor以及idProduct: ID [IdVendor:IdProduct]

比如`Bus 003 Device 007: ID 0c45:6366 Elan Microelectronics Corp.`

`IdVendor`为0c45,`IdProduct`为6366

## 2*.如果多个设备型号相同，则还需要根据插入的端口来绑定，那么还需要查看设备端口

查看设备端口

```bash
ls /dev/video*
# 会出现两个video开头的端口号，大概率是0和1，神奇的是单数的端口号是不可用的
```

查找插入的是哪个端口

```bash
udevadm info -a /dev/video0
```

找到和上面同样的idVendor以及idProduct的device的信息，记录KERNELS，这一条指示了插入的是电脑的哪一个硬件端口

比如KERNELS=="1-9"

## 3.编辑规则文件

```bash
sudu gedit /etc/udev/rules.d/77-xxxx
```

末尾添加

```
KERNEL=="vedio[0,2,4,6]", ATTRS{idVendor}=="0c45", ATTRS{idProduct}=="6366", SYMLINK+="usbcama"
```

单数端口不可用，因此指定绑定偶数端口。

如果两个设备型号完全相同，则需要通过插入的端口来分辨，则应该写入

```
KERNELS=="1-9", KERNEL=="vedio[0,2,4,6]", ATTRS{idVendor}=="0c45", ATTRS{idProduct}=="6366", SYMLINK+="usbcama"
```

## 3*. 剩余设备依次绑定

1. 一次插入一个设备是为了方便查看设备信息

2. 如果要绑定端口号，那么绑定的时候就要把设备插入到指定的端口上，并且以后也要插入到这个端口上

## 4.启用规则

```bash
sudo udevadm trigger
sudo /etc/init.d/udev restart
```

## 5.验证

```bash
ls -l /dev |grep video 
```
查看是否存在箭头指向固定端口，若存在则代表端口绑定成功

## 6.OpenCV打开指定端口号摄像头

```cpp
cv2.VidioCapture("/dev/usbcama",cv2.CAP_V4L) 
```

## Author 

夏旗