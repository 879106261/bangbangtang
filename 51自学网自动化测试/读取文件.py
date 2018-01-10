f = open('user.txt','r')

'''content = f.readlines()
value_interm = content.split(",")
print(value_interm)'''
for line in f.readlines():
	useriterm = line.strip()
	value_interm = useriterm.split(",")
	print(value_interm)
	value_username = value_interm[0]
	value_password = value_interm[1]
	value_lock = value_interm[2]

f.close()
