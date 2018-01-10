#AUTHOR:FAN
#定义一个菜单字典
menu_dict={
    "河南省":{
        "焦作市":{
            "修武县":{"AA","BB","CC"},
            "武陟县":{"DD","EE","FF"},
            "博爱县":{"GG","HH","II"}
        },
        "新乡市":{
            "辉县":{"AA","BB","CC"},
            "封丘县":{"DD","EE","FF"},
            "延津县":{"GG","HH","II"}
        }
    },
    "河北省":{
        "邢台":{
            "宁晋县":{"AA","BB","CC"},
            "内丘县":{"DD","EE","FF"},
            "邢台县":{"GG","HH","II"}
        },
        "唐山":{
            "乐亭县":{"AA","BB","CC"},
            "唐海县":{"DD","EE","FF"},
            "玉田县":{"GG","HH","II"}
        }
    }
}
#用户退出多级菜单用flag
flag =True
while flag:
    #用于记录一级菜单key的个数
    count1 = 0
    #打印一级菜单
    for index,key in enumerate(menu_dict.keys()):
        count1+=1
        print(index,key)
    user_choice = input("please input your choice:")
    #判断用户输入的值是否为全数字
    if user_choice.isdigit() is True:
        user_choice = int(user_choice)
        #判断用户输入的值是否大于列表的最大值
        if user_choice < count1:
            #将字典转换成列表，menu_dict.keys()默认不是列表
            menu_list = list(menu_dict.keys())
        else:
            print("you need input right num")
            continue
    elif user_choice == "q":
        flag= False
        break
    else:
        print("please input a num")
        continue
    while flag:
        count2= 1
        for index,key in enumerate(menu_dict[menu_list[user_choice]].keys()):
            count2+=1
            print (index,key)
        user_choice2 = input("please input your choice(q：退出程序，up上一级):")
        if user_choice2.isdigit() is True:
            user_choice2 = int(user_choice2)
            if user_choice2 < count2:
                menu_list2 = list(menu_dict[menu_list[user_choice]].keys())
            else:
                print("you need input right num")
                continue
        elif user_choice2 == "q":
            flag=False
            break
        elif user_choice2 =="up":
            break
        else:
            print("please input a num")
            continue
        while flag:
            count3=0
            for index,key in enumerate(menu_dict[menu_list[user_choice]][menu_list2[user_choice2]].keys()):
                print(index,key)
                count3+=1
            user_choice3 =input("please input your choice(q：退出程序，up上一级):")
            if user_choice3.isdigit() is True:
                user_choice3=int(user_choice3)
                if user_choice3 < count3:
                    menu_list3 = list(menu_dict[menu_list[user_choice]][menu_list2[user_choice2]])
                else:
                    print("you need input right num")
                    continue
            elif user_choice3 == "up":
                break
            elif user_choice3 =="q":
                flag =False
                break
            else:
                print("please input a num")
                continue
            while flag:
                for index,key in enumerate(menu_dict[menu_list[user_choice]][menu_list2[user_choice2]][menu_list3[user_choice3]]):
                    print (index,key)
                #提示用户已经到最后一级目录，可以退出或返回上级目录
                q_or_up = input("This is last level,you want to q（退出程序） or up(上一级)：")
                if q_or_up == "q":
                    flag = False
                    break
                elif q_or_up == "up":
                    break
                else:
                    continue