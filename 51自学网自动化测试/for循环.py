import random
class MySort():
    '''
    随机生成100个10至1000之间的数，对生产的100个数进行排序
    '''
    def __init__(self, start, end, count):
        '''
        :param start: 限制随机数生产的范围
        :param end: 生成随机数生产的范围
        :param count: 生成的随机数个数
        :mylist为生成的随机数组成的列表
        '''
        self.start = start
        self.end = end
        self.count = count
        self.mylist = []

        mycount = 0
        while mycount <self.count:
            value = random.uniform(self.start, self.end)
            mycount = mycount + 1
            self.mylist.append(value)
        self.__mysort__()
        print(self.mylist)


    def __mysort__(self):
        '''
        使用冒泡法排序
        '''
        mycount = self.count
        for i in range(0, mycount):
            for j in range(i + 1, mycount):
                if self.mylist[i] > self.mylist[j]:
                    self.mylist[i], self.mylist[j] = self.mylist[j], self.mylist[i]






if __name__ == "__main__":
    # calc = Calc(5, 4)
    # calc_result = calc.__add__()
    # # calc_result = calc.div()
    # print(calc_result)
    myso = MySort(10, 1000, 100)
    print(myso)

