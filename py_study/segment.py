import jieba
file = open(r"C:\Users\goodluck\Downloads\政府工作报告1000句 (1).txt","r", encoding="UTF-8")
text=file.read()
cut = jieba.cut(str(text))
#text1=file.readline()和text2=file.read()可以同时出现，不影响各自实现，但任一一个不能和file.readlines()同时起作用，会互相干扰
#print("text1 is",text1)
#print ("text2 is",text2)
result='/'.join(cut)
print("text is", text)
print(cut)
print(result)
file_1=open(r"C:\Users\goodluck\Downloads\政府工作报告1000句 (1)改.txt","w", encoding="UTF-8")
new=file_1.write(result)
print(new)

