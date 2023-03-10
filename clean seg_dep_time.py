import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\pytorch\data2.csv', low_memory=False)

# 从seg_dep_time列中提取小时数并将其保存在新列seg_dep_hour中
df['seg_dep_hour'] = df['seg_dep_time'].str.split().str[1].str.split(':').str[0]

# 将hour列中的所有值转换为整数类型
df['seg_dep_hour'] = df['seg_dep_hour'].astype(int)

# 删除seg_dep_time列
df.drop(['seg_dep_time'], axis=1, inplace=True)

# 保存更新后的CSV文件
df.to_csv('data3.csv', index=False)
