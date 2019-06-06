'''year = int(input("输入年份"))
if year%100==0:
    if year%400==0:
        print("该年是闰年")

    else:
        print("该年非闰年")

else:
    if year%4==0:
        print("该年是闰年")'''
'''
i = 1
sum = 1
multi_sum=1
while i<=10:

    sum*=i
    i+=1
print(sum)
i = 1
while i<=100:
    if i%7 == 0:
        print("过",end=",")
    elif str(i)[-1]=="7":
        print("过",end=",")

    elif str(i)[0]=="7":
        print("过",end=",")

    else:
        print(i,end=",")

    i+=1
'''
'''
num=int(input("输入一个数"))
i = 2
if num>2:
    while i<=num:
        if num%i == 0:
            print(num,"不是质数")
            i+=1
        #break
    else:
        print(num,"是质数")
else:
    print(num,"不是质数")
    '''
'''
for e in "Python":
    print("当前字母为",e)
'''
'''
num=int(input("输入一个数"))
i = 2
if num>2:
    for i in range(2,num):
        if num%i == 0:
            print(num,"不是质数")
            i+=1
        break
    else:
        print(num,"是质数")
else:
    print(num,"不是质数")'''

'''
for row in range(1,9):
    print("%d * %d = %d"%(col,row,row*col))
    for col in range(1,9):
        
for i in range(1,10):
    for j in range(1.i+1):
        print("%d*%d=%d"%(i,j,i*j),end="")
    print(" ")
'''
file = open(r"C:\Users\goodluck\Downloads\政府工作报告1000句.txt","r", encoding="UTF-8")
text1=file.readline()
text2=file.read()
print(text1)
print(text2)
