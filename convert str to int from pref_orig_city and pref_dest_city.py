import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 加载CSV文件
df = pd.read_csv(r'D:\data\data\.ipynb_checkpoints\train-checkpoint.csv', low_memory=False)

# 指定保留的列
cols_to_keep = ['birth_date', 'seg_dep_time', 'recent_flt_day']

# 创建LabelEncoder对象
le = LabelEncoder()

# 获取要处理的列名列表并转换
for col in df.columns:
    if col not in cols_to_keep and df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# 显示结果
df.to_csv('converted.csv', encoding='utf-8', index=False)
