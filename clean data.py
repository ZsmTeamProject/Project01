import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 加载CSV文件
df = pd.read_csv(r'D:\data\data\.ipynb_checkpoints\train-checkpoint.csv', low_memory=False)

# 指定需要修改的列
cols_to_keep = ['birth_date', 'seg_dep_time', 'recent_flt_day']

# 创建LabelEncoder对象
le = LabelEncoder()

# 获取要处理的列名列表并转换
for col in df.columns:
    if col not in cols_to_keep and df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

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

# 将hour列中的所有值转换为整数类型
df['seg_dep_time'] = df['seg_dep_time'].astype(int)

# 从birth_date列中提取年份并替换原来的内容
df['birth_date'] = df['birth_date'].str.split('/').str[0]

# 将year列中的所有值转换为整数类型
df['birth_date'] = df['birth_date'].astype(int)

# 从recent_flt_day列中提取年份并替换原来的内容
df['recent_flt_day'] = df['recent_flt_day'].str.split('/').str[0]

# 将recent_flt_day列中的所有值转换为整数类型
df['recent_flt_day'] = df['recent_flt_day'].astype(int)

# 删除重复行数据
df.drop_duplicates(inplace=True)

# 保存更新后的CSV文件
df.to_csv('data_cleaned.csv', index=False)
