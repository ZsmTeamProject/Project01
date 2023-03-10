import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\pytorch\data2.csv', low_memory=False)

# 从seg_dep_time列中提取小时数并替换原来的数据
df['seg_dep_time'] = df['seg_dep_time'].str.split(' ').str[1].str.split(':').str[0]

# 将hour列中的所有值转换为整数类型
df['seg_dep_time'] = df['seg_dep_time'].astype(int)

# 保存更新后的CSV文件
df.to_csv('data3.csv', index=False)
