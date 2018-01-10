import sys
sys.path.append("./Car2")  #将Car目录添加到环境变量path下
from Car2 import Car

BMW = Car.Car1(5, 'black')
print('车的颜色为:%s'%BMW.color)
print('车轮子数量为:%d'%BMW.wheelNum)

