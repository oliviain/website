import nltk
#nltk.download()
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize
#调用sent_tokenize()分句
para = "how are you? Fine, thanks."
print(sent_tokenize(para))
sentence = "It's good to see you."
tokens=nltk.word_tokenize(sentence)
print(tokens)

#from nltk.tokenize.stanford_segmenter import StanfordSegmenter
#para_zn="今天天气不错？对啊，没有雾霾。少见"
#print(sent_tokenize(para_zn))
#tokens_a=nltk.word_tokenize(para_zn)
#print(tokens_a)
#nltk分词，斯坦福接口未成功，中文没有效果，英文基本成功，只有小部分错误
