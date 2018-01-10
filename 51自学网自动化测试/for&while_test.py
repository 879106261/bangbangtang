import random
list = []
i = 0
for i in range(100):
    nub = random.randint(10, 1000)
    list.append(nub)
    i += 1


for i in range(0, 100):
    for j in range(i + 1, 100):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print('排序后的结果是:%s' % list)