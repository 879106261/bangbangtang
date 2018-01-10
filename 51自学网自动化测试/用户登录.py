import time
#定义一个用户字典
user_dict = {}
#定义一个用户列表
user_list = []

f = open("user.txt","r")
#用for循环获取文件每行的内容，并写入字典中，
for line in f.readlines():
	useriterm = line.strip()
	value_interm = useriterm.split(",")
	value_username = value_interm[0]
	value_password = value_interm[1]
	value_lock = value_interm[2]
	user_dict[value_username] = {
		"name":value_username,
		"password":value_password,
		"lock":value_lock
		}
f.close()
#print(user_dict)
#定义count_num计算用户输入错误的次数
count_num = 0
flag = True
while flag:
	if count_num == 3:
		print("输入次数超过三次，你需要等待10s")
		time.sleep(10)
	#获取用户名
	user_name = input("请输入用户名:")
	if user_name in user_dict.keys():
		#print(type(user_dict[user_name]["lock"])
		#判断用户是否被锁定
		if int(user_dict[user_name]["lock"]) == 0:
			for i in range(3):
				password = input("请输入密码:")
				#判断密码是否正确
				if password == user_dict[user_name]["password"]:
					print("登陆成功")
					flag = False
					break
				else:
					print("密码错误")
			else:
				#三次后锁定
				user_dict[user_name]["lock"] = "1"
				f = open("user.txt","w+")
				for value in user_dict.values():
					user_list = [value["name"],value["password"],value["lock"]]
					user_list = ",".join(user_list)
					f.write(user_list+"\n")
				print("密码输错太多，账号锁定")
				break
		else:
			print("账号锁定")
	else:
		print("账号不存在")
		count_num += 1
