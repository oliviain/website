# a = int(input("输入a值"))
# b = int(input("输入b值"))
# if a>b:
#     print(a)
# elif a==b:
#     print("a,b相等")
# else:
# #     print(b)
# a = int(input("输入a值"))
# b = int(input("输入b值"))
# if a>b:
#     print(a,b)
# elif a<=b:
#     print(b,a)
# score=int(input("请输入你的成绩"))
# if 0<=score <=100:
#     if 0<=score<=59:
#         print("你的等级为F，绩点为0")
#     elif 60<=score<=66:
#         print("你的等级为D，绩点为1.0-1.3")
# else:
#     print("你的成绩不在打分范围")
# year = int(input("输入年份"))
# if year%400==0:
#     print("是闰年")
# elif year%4==0 and year%100!=0:
#     print("是闰年")
# else:
#     print("非闰年")
# 冒泡排序
# def bubblesort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-1-i):
#             if nums[j]<nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums
# nums=[33,22,55,11,99]
# print(bubblesort(nums))
# 100的阶乘
# sum=1
# i = 1
# while i<=100:
#     sum*=i
#     i+=1
# print(sum)
# 清除标点符号
# import re
# text_clean=re.sub(r"[^a-zA-Z0-9]","",text)
#1-4组成不重复的三位数
#number_list=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i!=j) and (j!=k) and (i!=k):
#                 number=str(i)+str(j)+str(k)
#                 number_list.append(number)
# print(len(number_list),"个不重复的数字，是",number_list)
# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
# num = int(input("请输入一个数字: "))
#
# # 质数大于 1
# if num > 1:
#    # 查看因子
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"不是质数")
#            print(i,"乘于",num//i,"是",num)
#            break
#    else:
#        print(num,"是质数")
#
# # 如果输入的数字小于或等于 1，不是质数
# else:
#    print(num,"不是质数")
# 9x9乘法表
for i in range(1,10):
    for j in range(1,i+1):#关键i+1
        print("%dx%d=%d\t"%(i,j,i*j),end="")#中间的乘号可以换，要用\t横向制表符
    print() #要点在和for对齐
# num=int(input("输入一个数字"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"不是质数。",num,"=",i,"*",num//i)
#             break
#     else:#关键在和for对齐，表示循环结束没有整除
#         print(num,"是质数")
# else:
#     print(num,"不是质数")
# for i in "python":
#     print("字母为",i)
# animals={"1":"pig",3:"bird"}
# for animal in animals:
#     print("当前动物是",animal)
#画同心圆加正方形
# import turtle
# turtle.goto(0,0)
# for i in range(0,41,8):
#     turtle.penup()
#     turtle.goto(0,-i)
#     turtle.pendown()
#     turtle.circle(i)
# for i in range(3):
#     turtle.forward(300)
#     turtle.left(120)
# import re
# input=open(r"C:\Users\goodluck\Downloads\周一周二博婷\博婷期末要求111.txt","r",encoding="utf-8")
# input_str=input.read()#读取全部做为一个字符串
# input_nextstr=input.readline()#读第一行
# print(input_str)
# #print(input_nextstr)
# text_clean=re.sub(r"[^\w]","",input_str)
# print(text_clean)
# #path=re.compile(r"[\u4e00-\u9fa5]")
# found_text=re.findall(r'[0-9]',text_clean)
# print(found_text)
# output=open(r"C:\Users\goodluck\Downloads\周一周二博婷\博婷期末要求111.txt","a")
# write_text=output.write(str(found_text))
# print(write_text)
# print(output)
#
# import nltk
# from nltk.tokenize import sent_tokenize
# sentence = "how are you? Fine, thanks."
# sent_cut = sent_tokenize(sentence)
# print(sent_cut)
# for sentence in sent_cut:
#     word_cut=nltk.word_tokenize(sentence)
#     print(word_cut)

# import jieba
# import re
# sentence = '''以习近平同志为核心的党中央以巨大的政治勇气和强烈的使命担当，提出了一系列新理念新思想新战略，
# 解决了许多长期想解决而没有解决的难题，办成了许多过去想办而没有办成的大事，
# 推动党和国家事业取得了历史性成就、发生了历史性变革，中国特色社会主义进入了新时代。'''
# cut = jieba.cut(sentence)
# print(cut)
# print('，'.join(cut))

# a = 'dude hello world world hey hello java world hi python word how can you do this with out me what are you going to do never say never'
# # origin_text=a.split()
# # text=list(set(origin_text))
# # print({x:origin_text.count(x)for x in text})

a={"3":9,"o":2,"44":'pensil'}
for i in a:
    print(i,":",a[i])
