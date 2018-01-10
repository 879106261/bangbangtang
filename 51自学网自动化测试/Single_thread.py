from time import ctime,sleep
import threading

#说
def talk():
    print("开始说:%r"%ctime())
    sleep(2)
#写
def write():
    print("开始写:%r"%ctime())
    sleep(3)

if __name__=='__main__':
    talk()
    write()
    print('结束了%r'%ctime())


#if _name_=='_main_':表示如果当前模块是被直接运行的，则执行后面的语句，如果模块是被导入的，则不执行，