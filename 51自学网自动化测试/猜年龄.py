age_of_dean = 23
count = 0
while count < 3:
	guess_age = int(input("请输入你的年龄:"))
	if guess_age == age_of_dean:
		print("你猜对了")
		break
	elif guess_age > age_of_dean:
		print("猜小一点")
	else:
		print("猜大点")
	count += 1
	if count == 3:
		input_continue = input("你想继续么")
		if input_continue != "n":
			count = 0