import pandas as pd

# 导入数据集
df = pd.read_csv(r'D:\data\data\.ipynb_checkpoints\train-checkpoint.csv', low_memory=False)

# 将指定列范围中的数据转换为字符串类型
df.iloc[:, 362:373] = df.iloc[:, 362:373].astype(str)

# 将指定列范围中的数据转换为小写
df.iloc[:, 362:373] = df.iloc[:, 362:373].apply(lambda x: x.str.lower())
