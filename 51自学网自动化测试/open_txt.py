f=open('user.txt',"r")
lines=f.readlines()
print(lines)

for line in lines:
    #print(line.split(','))
    #print(line.split(',',1))
    print(line.split(',')[0])
