import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 导入所需数据集
train = pd.read_csv(r'D:/data/data/train.csv', low_memory=False)
test = pd.read_csv(r'D:/data/data/test.csv', low_memory=False)

# 记录训练集的长度
train_len = len(train)

# 组合两组数据集
df = pd.concat([train, test], axis=0, ignore_index=True)

# 指定保留的列
cols_to_keep = ['birth_date', 'seg_dep_time', 'recent_flt_day']

# 将混合类型的列转换为字符串
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str)

# 创建LabelEncoder对象
le = LabelEncoder()

# 对要处理的列进行编码转换
for col in df.columns:
    if col not in cols_to_keep and df[col].dtype == 'object':
        le.fit(df[col])
        df[col] = le.transform(df[col])

# 分离训练集和测试集
train_encoded = df[:train_len]
test_encoded = df[train_len:]

# 保存转换后的文件
train_encoded.to_csv('encoded_train.csv', index=False)
test_encoded.to_csv('encoded_test.csv', index=False)
