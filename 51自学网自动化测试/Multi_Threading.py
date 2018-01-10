from time import ctime,sleep
import multiprocessing
#定义说和写
def talk(content,loop):
    for i in range(loop):
        print("开始说：%s%s"%(content,ctime()))
        sleep(2)

def write(content,loop):
    for i in range(loop):
        print("开始写：%s%s"%(content,ctime()))
        sleep(2)

#定义和加载说和写的线程
process=[]    #创建一个线程空间
p1=multiprocessing.Process(target=talk,args=("你好，自学网",2)) #target= 调用函数    args= 传参
process.append(p1)   #将线程1加入线程空间
p2=multiprocessing.Process(target=write,args=("人生苦短",2))
process.append(p2)

#执行多线程 使用for循环保证线程全部执行
if __name__=="__main__":
    for p in process:
        p.start()
    for p in process:
        p.join()
print("结束了%s"%ctime())

