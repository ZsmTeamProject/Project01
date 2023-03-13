import pandas as pd


# 定义转换函数
def convert_age_range(x):
    if x == '21-30':
        return 1
    elif x == '31-40':
        return 2
    elif x == '41-50':
        return 3
    elif x == '51-60':
        return 4
    elif x == '60+':
        return 5
    else:
        return 0


# 读取数据
data = pd.read_csv(r'D:\data\data\train.csv', low_memory=False)

# 转换数据列
data['age'] = data['age'].apply(convert_age_range)

# 导出数据
data.to_csv("data_age2.csv", index=False)