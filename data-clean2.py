import pandas as pd

# 读取 CSV 文件并选取需要处理的列
df = pd.read_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\test.csv", low_memory=False)
col = "birth_date"

# 使用 str 属性和字符串的切片方法删除对应列的月份和日期
df[col] = df[col].astype(str).apply(lambda x: x[:13])

# 将处理后的数据写入新的 CSV 文件中
df.to_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\test2.csv", index=False)
