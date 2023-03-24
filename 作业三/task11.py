from collections import Counter

# 读取目标文件并分词
with open('../作业二/output1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()
tokens1 = text1.split()

with open('../作业二/output2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()
tokens2 = text2.split()

# 计算词频并排序
counter1 = Counter(tokens1)
sorted1 = sorted(counter1.items(), key=lambda x: x[1], reverse=True)

counter2 = Counter(tokens2)
sorted2 = sorted(counter2.items(), key=lambda x: x[1], reverse=True)

# 将结果输出到文件
with open('1gram.txt', 'w', encoding='utf-8') as f:
    f.write('Target1\n')
    for word, count in sorted1:
        f.write(f'{word} {count}\n')
    f.write('\nTarget2\n')
    for word, count in sorted2:
        f.write(f'{word} {count}\n')
