import pandas as pd

# 读取CSV文件
df = pd.read_csv(r'D:\pytorch\data5.csv', low_memory=False)

# 删除重复行
df.drop_duplicates(inplace=True)

# 保存更新后的CSV文件
df.to_csv('data6.csv', index=False)
