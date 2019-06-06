#family_name=input("家庭成员都有谁？")
member_age= input("分别多大年纪？用阿拉伯数字输入，英文逗号隔开")#得到字符串“number1,number2,..."
#print(member_age.split(","))
listtype_member_age=member_age.split(",")#按照","将字符串拆分成字符串列表["number1","number2",...]

sum=0
for i in listtype_member_age:#提取每一个字符串并用int转化成数字，即提取每一个数字，用循环求和
    sum +=int(i)
number_of_member = int(len(listtype_member_age))#求list类型年龄表的长度，并将str类型转化成int,可以进行数字间的除法
#print(type(number_of_member))

average_age= sum /number_of_member
print("我家的平均年龄",average_age)

