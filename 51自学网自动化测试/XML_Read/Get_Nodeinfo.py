from xml.dom import minidom
#打开xml文件
dom=minidom.parse('class_info.xml')
#打在dom对象元素
root=dom.documentElement
#通过.getElementsByTagName方法 定位子节点
tags=root.getElementsByTagName('student')
#打印节点信息

print(tags.nodeName)
print(tags.nodeValue)
print(tags.nodeType)

