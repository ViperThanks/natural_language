from bs4 import BeautifulSoup
import re

# 读取HTML文件
with open('../data/学院介绍.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 匹配中文字符
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

# 遍历HTML文档中的所有段落、句子和短语，并将中文内容写入TXT文件
with open('output.txt', 'w', encoding='utf-8') as f:
    for p in soup.find_all('p'):  # 遍历所有段落
        text = p.get_text()
        for sentence in re.split('[。！？]', text):  # 遍历所有句子
            sentence = sentence.strip()
            if not sentence:
                continue
            for phrase in sentence.split('，'):  # 遍历所有短语
                phrase = phrase.strip()
                if not phrase:
                    continue
                match = zh_pattern.search(phrase)
                if match:
                    f.write(match.group() + '\n')
