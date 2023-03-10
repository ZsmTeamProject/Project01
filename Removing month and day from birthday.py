import pandas as pd

# 读取 CSV 文件
df = pd.read_csv(r'D:\data\data\.ipynb_checkpoints\train-checkpoint.csv', low_memory=False)

# 指定要处理的列
columns_to_process = df.columns[13]

# 对指定列的字符串数据保留前四位
df[columns_to_process] = df[columns_to_process].astype(str).apply(lambda x: x[:4])
