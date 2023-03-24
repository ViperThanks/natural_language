import pandas as pd
import numpy as np
from scipy.interpolate import lagrange

# 读取数据
df = pd.read_excel('D:/python/natural_language/big_data_explaining/ch04/data/catering_sale.xls')


# 定义插值函数
def interpolate_column(s):
    # 生成没有缺失值的索引
    notnull_index = s.notnull().nonzero()[0]
    # 如果所有值都缺失，则不进行插值
    if len(notnull_index) == 0:
        return s
    else:
        # 对缺失值进行插值
        return lagrange(notnull_index, s[notnull_index])(range(len(s)))


# 对所有列进行插值
for col in df.columns:
    df[col] = interpolate_column(df[col])

# 将结果输出到sales.xls文件中
df.to_excel('sales.xls', index=False)
