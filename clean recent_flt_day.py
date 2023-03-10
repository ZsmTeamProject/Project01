import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\pytorch\data4.csv', low_memory=False)

# 从recent_flt_day列中提取年份并替换原来的内容
df['recent_flt_day'] = df['recent_flt_day'].str.split('/').str[0]

# 将recent_flt_day列中的所有值转换为整数类型
df['recent_flt_day'] = df['recent_flt_day'].astype(int)

# 保存更新后的CSV文件
df.to_csv('data5.csv', index=False)
