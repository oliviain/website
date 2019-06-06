import jieba
import re
sentence = '''以习近平同志为核心的党中央以巨大的政治勇气和强烈的使命担当，
提出了一系列新理念新思想新战略，
解决了许多长期想解决而没有解决的难题，办成了许多过去想办而没有办成的大事，
推动党和国家事业取得了历史性成就、发生了历史性变革，中国特色社会主义进入了新时代。'''
cut = jieba.cut(sentence)
print(cut)
print('，'.join(cut))
