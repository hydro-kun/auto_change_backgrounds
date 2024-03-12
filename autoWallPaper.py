#!/usr/bin/python
import os
import xml.etree.ElementTree as ET

def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


# 设置变量
Directory = '/usr/share/backgrounds/WallPaper'  # 壁纸文件夹，可变
fileName = '/usr/share/backgrounds/contest/jammy.xml'  # 配置文件位置，不能变
encoding = 'UTF-8'
durationTime = '1795.0'     # 每张壁纸持续时间
changeTIme = '5.0'          


def getFile(Directory):
    root, dirs, files = next(os.walk(Directory))
    print(root)
    for name in dirs:
        print("Directory:", name)  # 打印文件夹名
    files=checkSuffix(files)  # 剔除非图片的文件
    for name in files:
        print("FileName:", name)  # 打印文件名
    return root, dirs, files


def xmlwrite(mainElement):
    tree = ET.ElementTree(mainElement)
    tree.write(fileName)
    tree = ET.parse(fileName)  # 解析movies.xml这个文件
    root = tree.getroot()  # 得到根元素，Element类
    pretty_xml(root, '\t', '\n')  # 执行美化方法
    tree.write(fileName, encoding=encoding)


# static block
'''
<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
'''


def addStartTime(father):
    starttime = ET.SubElement(father, 'starttime')
    year = ET.SubElement(starttime, 'year')
    month = ET.SubElement(starttime, 'month')
    day = ET.SubElement(starttime, 'day')
    hour = ET.SubElement(starttime, 'hour')
    minute = ET.SubElement(starttime, 'minute')
    second = ET.SubElement(starttime, 'second')
    year.text = '2009'
    month.text = '1'
    day.text = '1'
    hour.text = '0'
    minute.text = '0'
    second.text = '0'


'''
  <static>
    <duration>1795.0</duration>
    <file>/usr/share/backgrounds/0.png</file>
  </static>
'''


def addStatic(father, duration, file):
    static = ET.SubElement(father, 'static')
    d = ET.SubElement(static, 'duration')
    f = ET.SubElement(static, 'file')
    d.text = duration
    f.text = file


'''
  <transition>
    <duration>5.0</duration>
    <from>/usr/share/backgrounds/0.png</from>
    <to>/usr/share/backgrounds/Cherry_Tree_in_Lakones_by_elenastravoravdi.jpg</to>
  </transition>
'''


def addTransition(father, duration, fRom, to):
    transition = ET.SubElement(father, 'transition')
    d = ET.SubElement(transition, 'duration')
    f = ET.SubElement(transition, 'from')
    t = ET.SubElement(transition, 'to')
    d.text = duration
    f.text = fRom
    t.text = to

'''
检查后缀是否为jpg和png和jpeg, 否则跳过
'''
def checkSuffix(files):
    res=[]
    for i in range(len(files)):
        suffix = files[i].split('.')[-1]
        if 'jpg'==suffix or 'png'==suffix or 'jpeg'==suffix:
            res.append(files[i])
        else:
            print(files[i]," out!")
    return res


def main():
    root, dirs, files = getFile(Directory)
    background = ET.Element("background")
    addStartTime(background)
    add = lambda y: '%s%s%s' % (root,'/',y)

    first = files[0]
    for i in range(0, len(files) - 1):
        addStatic(background, durationTime, add(files[i]))
        addTransition(background, changeTIme, add(files[i]), add(files[i + 1]))

    i = i + 1
    # 跳转开头壁纸
    addStatic(background, durationTime, add(files[i]))
    addTransition(background, changeTIme, add(files[i]), add(first))
    xmlwrite(background)


main()