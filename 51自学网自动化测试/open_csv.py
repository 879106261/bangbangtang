import csv
stu=['rom',28,'changsha']
stu1=['lili',30,'nanjing']
#打开文件
out=open('tt.csv','a',newline='')   #newline=''为了不出现空行
#设定写入模式
csv_write=csv.writer(out,dialect='excel')   #dialect='excel' 编码方式excel
#写入具体的内容
csv_write.writerow(stu)
csv_write.writerow(stu1)
print('写入成功')
csv_file=csv.reader(open('tt.csv','r'))

for stu in csv_file:
    print(stu)
