import re
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# 读取HTML文件
with open('../data/test.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

# 将HTML文档转换为BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 打开输出文件
with open('output1.xml', 'w', encoding='utf-8') as f:

    # 创建根节点
    root = ET.Element('document')

    # 提取段落
    for p in soup.find_all('p'):

        # 创建段落节点
        section = ET.SubElement(root, 'section')

        # 创建id节点
        id = ET.SubElement(section, 'id')
        id.text = str(p.get('id'))

        # 创建content节点
        content = ET.SubElement(section, 'content')
        content.text = p.get_text(strip=True)

        # 创建link节点
        link = ET.SubElement(section, 'link')
        link.text = str(p.find('a').get('href')) if p.find('a') else ''

    # 将结果写入输出文件
    f.write(ET.tostring(root, encoding='unicode', method='xml'))
