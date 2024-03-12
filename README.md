# ubuntu22.04自动更换壁纸

本仓库仅作备份

ubuntu22.04桌面自动更换壁纸并不是只将图像放到`/usr/share/backgrounds`即可

还需要修改`/usr/share/backgrounds/contest/jammy.xml`，因此编写此文件

## 实现

1.autoWallPaper.py

* 详见[autoWallPaper.py](./autoWallPaper.py)
* 主要作用是读取特定文件夹下的所有图片名，并生成jammy.xml文件
* 有一些全局变量可以修改

2.autoWallPaper.sh

* 详见[autoWallPaper.sh](./autoWallPaper.sh)
* 主要用于开机启动脚本

3.jammy.xml

* 生成的配置文件
* 具体格式如下所示：

```xml
<!--  开始块  -->
<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
```

```xml
<!--  静态块  -->
  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/jammy.png</file>
  </static>
```

```xml
<!--  转换块  -->
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/jammy.png</from>
    <to>/usr/share/backgrounds/Cherry_Tree_in_Lakones_by_elenastravoravdi.jpg</to>
  </transition>
```

## 使用
1.将autoWallPaper.py和autoWallPaper.sh放到任意路径下，添加开机启动 (需要修改sh文件路径)

2.如果不想每次加壁纸都sudo的话，可以另外指定壁纸路径

3.如果不想给开机启动程序添加sudo权限的话，使用软链接即可

```bash
ln -s /home/username/.config/jammy.xml jammy.xml
```
