import tarfile
import json
from bs4 import BeautifulSoup
import config as cg
import jieba
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

tar = tarfile.open(cg.file_path)
for tarinfo in tar:
    if tarinfo.name.find(cg.topic_file_name) == -1:
        continue
    filetext = tar.extractfile(tarinfo).read().decode(
        'utf-8').replace('&nbsp;', '').split('\n')

data = [json.loads(d) for d in filetext if len(d) != 0]
jieba.set_dictionary('../dict/dict.txt.big')
for w in cg.word_:
    jieba.add_word(w)
texts = list()
count = 0
for i in data:
    if 'content' in i:
        soup = BeautifulSoup(i['content'])
        if not len(soup.text):
            continue
        else:
            sentence = soup.text
            a = list(jieba.cut(sentence))
            test = 0
            for j in a:
                while test != 1:
                    if j in cg.constellationlist:
                        test = test + 1
                        count = count + 1
                        # 過濾垃圾值
                        for item in cg.relist:
                            while item in a:
                                a.remove(item)
                        texts.append(a)
                        print("START PUSH " + repr(count) + " list to texts!!")
                    else:
                        break

print("Pushing Complete!!")

test = str(texts)
with open('data/test.txt', 'w', encoding='utf-8') as f:
    f.write(test)
    f.close()
