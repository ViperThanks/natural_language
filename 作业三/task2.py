from collections import Counter
import re

# 读取两个语料文件
with open('../作业二/output1.txt', 'r', encoding='utf-8') as f1, \
        open('../作业二/output2.txt', 'r', encoding='utf-8') as f2:
    corpus1 = f1.read()
    corpus2 = f2.read()


# 定义一个函数，用于生成二元语法模型
def generate_2gram_model(corpus):
    tokens = re.findall(u'[\u4e00-\u9fa5]+', corpus)  # 利用正则表达式分词
    pairs = zip(tokens[:-1], tokens[1:])  # 生成二元组
    return Counter(pairs)  # 返回二元组计数结果


# 生成两个语料的二元语法模型
model1 = generate_2gram_model(corpus1)
model2 = generate_2gram_model(corpus2)

# 将结果按词频从大到小排序并输出到文件
with open('2gram.txt', 'w', encoding='utf-8') as f:
    for pair, count in model1.most_common() + model2.most_common():
        f.write(pair[0] + ' ' + pair[1] + '\t' + str(count) + '\n')
