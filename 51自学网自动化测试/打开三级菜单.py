menu_dict = {
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

flag = True

while flag:
 	#记录一级菜单的个数
 	count1 = 0
 	#打印一级菜单
 	for index,key in enumerate(menu_dict.keys()):
 		count1 += 1
 		print(index,key)
 	user_choice = input("请输入你的选择:")
 	#判断是否输入数字
 	if user_choice.isdigit() is True:
 		user_choice = int(user_choice)
 		#判断是否输入正确
 		if user_choice < count1:
 			#menu_dict.keys转换成列表
 			menu_list = list(menu_dict.keys())
 		else:
 			print("你需要输入正确数字")
 			continue
 	elif user_choice == "q":
 		flag = False
 		break
 	else:
 		print("请输入一个数字")
 		continue
