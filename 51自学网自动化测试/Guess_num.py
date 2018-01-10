import  random
answer = random.randint(1,100)
n = int(input("请输入一个数字（1-100）"))
while n !=answer:
    if n > answer:
        n = int(input("数值大了，请输入一个数字（1-100）"))
    elif n < answer:
        n = int(input("数值小了，请输入一个数字（1-100）"))
print("你赢了")50
