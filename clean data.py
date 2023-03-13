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
# ffp_nbr→ffp_cfm
df = df.rename(columns={'ffp_nbr': 'ffp_cfm'})


# 创建一个函数，转换非0为1
def replace_values(x, specified_value):
    if x == specified_value:
        return x
    else:
        return 1


# 使用 apply 方法应用该函数到指定列
df['ffp_cfm'] = df['ffp_cfm'].apply(lambda x: replace_values(x, 0))

# 从seg_dep_time列中提取小时数并替换原来的数据
df['seg_dep_time'] = df['seg_dep_time'].str.split(' ').str[1].str.split(':').str[0]

# 将所有非'yyyy/mm/dd'格式的数据全部转换为'0000/00/00'
df['birth_date'] = df['birth_date'].apply(lambda x: '0000/00/00' if not str(x).startswith('19') and not str(x).startswith('20') else x)

# 将缺失值NaN也填补为'0000/00/00'
df['birth_date'] = df['birth_date'].fillna('0000/00/00')

# 从birth_date列中提取年份并替换原来的内容
df['birth_date'] = df['birth_date'].str.extract(r'(\d{4})', expand=False)  # 从日期字符串中提取4个数字作为年份部分

# 将year列中的所有值转换为整数类型
df['birth_date'] = df['birth_date'].astype(int)

# 将hour列中的所有值转换为整数类型
df['seg_dep_time'] = df['seg_dep_time'].astype(int)

# 从recent_flt_day列中提取年份并替换原来的内容
df['recent_flt_day'] = df['recent_flt_day'].str.split('/').str[0]

# 将recent_flt_day列中的所有值转换为整数类型
df['recent_flt_day'] = df['recent_flt_day'].astype(int)

# 删除重复行数据
df.drop_duplicates(inplace=True)

# 分离训练集和测试集
train_encoded = df[:train_len]
test_encoded = df[train_len:]

# 保存转换后的文件
train_encoded.to_csv('encoded_train.csv', index=False)
test_encoded.to_csv('encoded_test.csv', index=False)
