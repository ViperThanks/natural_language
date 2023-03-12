import re
from bs4 import BeautifulSoup

debug_list1 = []
debug_list2 = []
# 读取HTML文件
with open('../data/学院介绍.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

# 将HTML文档转换为BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 定义中文正则表达式
zh_pattern = re.compile('[\u4e00-\u9fa5]+')

# 打开输出文件
with open('../target/output.xml', 'w', encoding='utf-8') as f:

    # 写入XML头
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<document>\n')

    # 提取段落
    for p in soup.find_all('p'):

        # 提取段落内容
        content = p.get_text(strip=True)
        debug_list1.append(content)


        # 提取句子
        sentences = re.split('[。！？]', content)
        debug_list2.append(sentences)

        # 拼接成段落形式，并写入XML
        if sentences:
            f.write('  <section>\n')
            f.write('    <id>' + str(p['id']) + '</id>\n')
            f.write('    <content>\n')
            for sentence in sentences:
                # 过滤掉非中文字符
                sentence = ''.join(re.findall(zh_pattern, sentence))
                if sentence:
                    f.write('      <sentence>' + sentence + '</sentence>\n')
            f.write('    </content>\n')
            f.write('    <link>' + p.find('a')['href'] + '</link>\n')
            f.write('  </section>\n')

    # 写入XML尾
    f.write('</document>\n')

print(debug_list1)
print("\n======\n")
print(debug_list2)
