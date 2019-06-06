# import re
# file_input=open(r"C:\Users\goodluck\Downloads\周一周二博婷\1.txt","r",encoding="utf-8")
# text=file_input.read()
# print(text)
# text_clean=re.sub(r"[^\w]"," ",text)
# text_find=re.findall(r"[\u4e00-\u9fa5]",text_clean)
# output=open(r"C:\Users\goodluck\Downloads\周一周二博婷\1.txt","a")
# write_text=output.write(str(text_find))
# print(write_text)

# str="acordingt to ur name" #查找
# print(str.find("[a-z]"))
#递归
# def recur_fibo(n):
#    """递归函数
#    输出斐波那契数列"""
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#    print("输入正数")
# else:
#    print("斐波那契数列:")
#    for i in range(nterms):
#        print(recur_fibo(i))
# def bubblesort(a):
#     for i in range(len(a)-1):
#         for j in range(len(a)-1-i):
#             if a[j]<a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print(a)
# a=[33,55,6,2,4,9]
# print(bubblesort(a))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dx%d=%d\t"%(i,j,i*j),end=",")
#     print()
#判断质数
num=int(input("输入一个数"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("非质数",i,"x",num//i,"=",i)
            break
    else:
        print("是质数")
else:
    print("非质数")
