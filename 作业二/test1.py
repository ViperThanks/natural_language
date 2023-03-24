from bs4 import BeautifulSoup
import re

# 读取HTML文件
with open('../data/学院首页.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 匹配中文字符
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

# 遍历HTML文档中的所有内容，并将中文内容写入TXT文件
with open('output2.txt', 'w', encoding='utf-8') as f:
    for tag in soup.recursiveChildGenerator():  # 遍历所有元素
        if hasattr(tag, 'name') and tag.name in ['script', 'style']:  # 忽略 script 和 style 标签
            continue
        if hasattr(tag, 'string') and isinstance(tag.string, str):  # 忽略空白和空行
            text = tag.string.strip()
            if text:
                match = zh_pattern.search(text)
                if match:
                    f.write(match.group() + '\n')
                    if tag.name == 'p':  # 如果是段落，则在后面添加换行符
                        f.write('\n')
                elif tag.name == 'br':  # 如果是换行符，则在前面添加空行
                    f.write('\n\n')
