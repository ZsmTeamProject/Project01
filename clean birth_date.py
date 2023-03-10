import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\pytorch\data3.csv', low_memory=False)

# 从birth_date列中提取年份并替换原来的内容
df['birth_date'] = df['birth_date'].str.split('/').str[0]

# 将year列中的所有值转换为整数类型
df['birth_date'] = df['birth_date'].astype(int)

# 保存更新后的CSV文件
df.to_csv('data4.csv', index=False)
