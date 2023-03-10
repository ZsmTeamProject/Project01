import pandas as pd

# 读取 CSV 文件并选取需要处理的列
df = pd.read_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\test.csv", low_memory=False)

columns_to_process = df.columns[13]
# 使用 str 属性和字符串的切片方法删除对应列的月份和日期
df[columns_to_process] = df[columns_to_process].astype(str).apply(lambda x: x[:4])

# 将处理后的数据写入新的 CSV 文件中
df.to_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\test2.csv", index=False)
