#AUTHOR:FAN
import time
#定义一个用户字典
user_dict={}
#定义一个用户列表
user_list=[]

f=open("user.txt",'r')
#用for循环获取文件中每行的内容，并写入到字典中，value_interm[0]表示username,value_interm[1]表示password,value_interm[2]表示
#账户的锁定信息：0表示正常，1表示锁定
for line in f.readlines():
    useriterm = line.strip()
    value_interm = useriterm.split(',')
    value_username = value_interm[0]
    value_password = value_interm[1]
    value_lock = value_interm[2]
    user_dict[value_username]={
        "name":value_username,
        "password":value_password,
        "lock":value_lock
    }
f.close()
#print(user_dict)
#定义个count_num用户计算用户输入错误用户的次数
count_num = 0
#用于跳出多层循环
flag = True
while flag:
    if count_num == 3:
        print("dute to input non-existent user ,you need to wait 10s")
        time.sleep(10)
    # 获取用户输入的用户名
    user_name = input("please input your username:")
    if user_name in user_dict.keys():
        #print(type(user_dict[user_name]["lock"]))
        #判断用户是否被锁定
        if int(user_dict[user_name]["lock"]) == 0:
            for i in range(3):
                password = input("please input you password:")
                #判断密码是否正确
                if password == user_dict[user_name]["password"]:
                    print("welcome to login my system!")
                    flag=False
                    break
                else:
                    print("password is error")
            else:
                #用户输入密码错误三次后被锁定
                user_dict[user_name]["lock"]="1"
                f = open("user.txt","w+")
                #将字典装换成列表，将改变的信息写入到文件中
                for value in user_dict.values():
                    user_list =[value["name"],value["password"],value["lock"]]
                    user_list =",".join(user_list)
                    f.write(user_list+"\n")
                print("you input wrong password too many,the user is locked")
                break
        else:
            print("user is locked")
    else:
        print("user is not exist")
        count_num+=1