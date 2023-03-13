import pandas as pd
from datetime import datetime

# 读取数据
data = pd.read_csv("../FilteredData/encoded_data_file.csv")

# 将 seg_dep_time 字段转换为日期时间格式，并提取小时数作为新特征 hour
# ！！！这个hour不是需要的特征，只是临时使用的一个样板！！！！
data['seg_dep_time'] = data['seg_dep_time'].apply(lambda x: datetime.strptime(x, '%Y/%m/%d %H:%M'))
data['hour'] = data['seg_dep_time'].apply(lambda x: x.hour)

# 对类别特征使用 LabelEncoder 进行编码转换
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
categorical_features = ['seg_route_from', 'seg_route_to', 'seg_cabin', 'gender', 'residence_country', 'nation_name']

for feature in categorical_features:
    data[feature] = le.fit_transform(data[feature])

# 删除原始的 seg_dep_time 字段
data = data.drop(['seg_dep_time'], axis=1)

data.to_csv("encoded_data_final.csv", encoding='utf-8', index=False)
