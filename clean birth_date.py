import pandas as pd
import re


# 读取CSV文件
df = pd.read_csv(r'D:\data\data\test.csv', low_memory=False)

# 将所有非'yyyy/mm/dd'格式的数据全部转换为'0000/00/00'
df['birth_date'] = df['birth_date'].apply(lambda x: '0000/00/00' if not str(x).startswith('19') and not str(x).startswith('20') else x)

# 将缺失值NaN也填补为'0000/00/00'
df['birth_date'] = df['birth_date'].fillna('0000/00/00')

# 从birth_date列中提取年份并替换原来的内容
df['birth_date'] = df['birth_date'].str.extract(r'(\d{4})', expand=False)  # 从日期字符串中提取4个数字作为年份部分

# 将year列中的所有值转换为整数类型
df['birth_date'] = df['birth_date'].astype(int)

# 保存更新后的CSV文件
df.to_csv('data_test1.csv', index=False)
