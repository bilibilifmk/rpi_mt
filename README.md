# rpi_mt
## 树莓派移动终端 全键盘及2.4寸tft材质屏幕

# 这是一个还在开发中的项目 

## 我自己打包的系统镜像 
img镜像：https://jia666-my.sharepoint.com/:u:/g/personal/byjt7zwnr_xkx_me/EbDBW9j-o8hDrcH_12RZnNwBDYK6B51_uuKVfxjyH1TYVw?e=7YSqbK

https://pan.baidu.com/s/1et3HwhCRhgPBmtK6T9dM4g  提取码：k1xn   
该镜像为dd命令备份出来的，镜像包含opencv python3可以直接用python来代替 源以替换国内源，所有软件包均为最新 （2020.4.7）已经打开ssh   
用户名pi 密码 1  root用户密码 a






## α版本展示：https://www.bilibili.com/video/av96884398/

2020.3.16:键盘驱动基本上达到能用的程度了


2020.3.2:键盘驱动还在开发中

使用树莓派作为底版（支持4b 3b zero） 的扩展板

# 效果图
正面
![image](https://github.com/bilibilifmk/rpi_mt/blob/master/%E6%AD%A3%E9%9D%A2.jpg)
背面
![image](https://github.com/bilibilifmk/rpi_mt/blob/master/%E8%83%8C%E9%9D%A2.jpg)


# 键盘驱动说明

键盘驱动使用说明 


 首先安装i2c相关工具
 
sudo apt update

sudo apt upgrade

sudo apt install i2c-tools

i2c-detect -y 1


 一 替换内核 两种方法
 
1.使用我编译好的内核 boot 压缩文件替换 原本boot分区 （linux或win下操作）

2.自行编译内核 在配置内核时勾选tca8418


二 替换内核设备树

# 使用我提供的内核可以跳过这部
 
rca8418内提供键盘key值 

编译指令 sudo dtc -@ -I dts -O dtb -o tca8418.dtbo tca8418.dts

得到tca8418.dtb  执行树替换 sudo cp tca8418.dtbo /boot/overlays/

重启后 执行dmesg | grep i2c 

输出 

i2c /dev entries driver
input: tca8418 as /devices/platform/soc/20804000.i2c/i2c-1/1-0034/input/input0

即代表成功


# 屏幕驱动说明


屏幕驱动项目地址 ：https://github.com/juj/fbcp-ili9341

make参数

cmake -DARMV8A=ON -DDISPLAY_ROTATE_180_DEGREES=ON -DILI9341=ON -DGPIO_TFT_DATA_CONTROL=24 -DGPIO_TFT_RESET_PIN=25 -DSPI_BUS_CLOCK_DIVISOR=10 -DADAFRUIT_ILI9341_PITFT=ON -DDISPLAY_BREAK_ASPECT_RATIO_WHEN_SCALING=ON -DSTATISTICS=0 -DUSE_DMA_TRANSFERS=OFF ..



使用我编译的驱动方法：

1.吧build放在用户目录下（/home/pi/）

2.执行cd /home/pi/build/

2.添加启动权限： chomd +x fbcp-ili9341

3.测试（执行成功应该会黑屏）：sudo ./fbcp-ili9341

4.写入启动项（请先安装vim插件）

执行  sudo vi /etc/rc.local

在exit0前添加 sudo /home/pi/build/fbcp-ili9341 &

5.设置在没有HDMI情况下依然输出

执行 sudo vi /boot/config.txt


在任意位置添加以下参数


hdmi_group=2

hdmi_mode=87

hdmi_cvt=320 240 60 1 0 0 0

hdmi_force_hotplug=1

