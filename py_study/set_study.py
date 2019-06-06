a= open(r"C:/Users/goodluck/Documents/example.txt","r")
print(a.readlines())

# split_string=a.split()
# print (split_string)
# print(len(split_string))
# words_num=set(split_string)
# print(len(words_num))
# dir1={}
# for i in words_num:
#     count_num=split_string.count(i)
#     dir1[i]=count_num
# print(dir1)
a = 'hello world world hey hello java world hi python word how can you do this with out me'
split_words=a.split()
unique_words=set(split_words)
print(split_words)
print(unique_words)
dir={}
for i in unique_words:
    dir[i]=split_words.count(i)
print(dir)
rank_dir=sorted(dir.items(),key=lambda x:x[1],reverse=True)
print (rank_dir)
