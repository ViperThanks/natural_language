from bs4 import BeautifulSoup
import re

# 读取HTML文件
with open('../data/学院介绍.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 匹配中文字符
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

# 遍历HTML文档中的所有元素，并将中文内容写入XML文件
with open('output2.xml', 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    for element in soup.descendants:
        if element.name and element.string and zh_pattern.search(element.string):
            f.write('<{}>'.format(element.name))
            for sentence in re.split('[。！？]', element.string):
                sentence = sentence.strip()
                if not sentence:
                    continue
                match = zh_pattern.search(sentence)
                if match:
                    f.write(match.group())
            f.write('</{}>\n'.format(element.name))
