import pandas as pd

# 加载CSV文件
df = pd.read_csv(r'D:\pytorch\converted.csv', low_memory=False)

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

df.to_csv('data2.csv', encoding='utf-8', index=False)
