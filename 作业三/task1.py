from collections import Counter

# 读取文件内容
with open('../作业二/output.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 分割文本为单词列表
word_list = content.split()

# 统计单词出现次数
word_count = Counter(word_list)

# 按照词频从大到小排序
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 将结果写入到1gram.txt中
with open('1gram.txt', 'w', encoding='utf-8') as f:
    for item in sorted_word_count:
        f.write(f"{item[0]}\t{item[1]}\n")
