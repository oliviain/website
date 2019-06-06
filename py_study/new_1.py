a = 'dude hello world world hey hello java world hi python word how can you do this with out me what are you going to do never say never'
b = 'Although each society differs in its resources' \
    'palliative care can be tailored to local contexts'\
    'The Commission1 describes three levels of palliative care'\
    'care provided by general practitioners in the community '
def rank1(text):
    text_list = text.split()

    words= list(set(text_list))
    word_dic={x:text_list.count(x) for x in words}
    rank_result=sorted(word_dic.items(),key = lambda x:x[1],reverse = True)
    print(rank_result[0:10])
rank1(a)
rank1(b)
import collections
def rank2(text):
    text_list = text.split()
    final_a=collections.Counter(text_list)
    final_result=final_a.most_common()
    #print(final_result)
    print(final_result[:10])


    # for i in final_result:
    #     print(i,":",final_result[i])
    #     if i == 10:
    #         break

    # final_form=
    # print(final_result)
rank2(a)
rank2(b)

