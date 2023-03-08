import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# 读取数据
data = pd.read_csv("../FilteredData/FilteredData.csv")

# 创建LabelEncoder对象
le = LabelEncoder()

# 对特征列进行编码转换
data['seg_route_from'] = le.fit_transform(data['seg_route_from'])
data['seg_route_to'] = le.fit_transform(data['seg_route_to'])
data['seg_cabin'] = le.fit_transform(data['seg_cabin'])
data['gender'] = le.fit_transform(data['gender'])
data['residence_country'] = le.fit_transform(data['residence_country'])
data['nation_name'] = le.fit_transform(data['nation_name'])

# 打印转换后的数据
print(data.head())

# 保存转换后的数据
data.to_csv("encoded_data_file.csv", encoding='utf-8', index=False)


































# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import json
#
# # 读取数据
# data = pd.read_csv("../data/smallTest.csv")
#
# # 创建LabelEncoder对象
# le = LabelEncoder()
#
# # 对特征列进行编码转换
# data['seg_route_from'] = le.fit_transform(data['seg_route_from'])
# data['seg_route_to'] = le.fit_transform(data['seg_route_to'])
# data['seg_cabin'] = le.fit_transform(data['seg_cabin'])
# data['gender'] = le.fit_transform(data['gender'])
# data['residence_country'] = le.fit_transform(data['residence_country'])
# data['nation_name'] = le.fit_transform(data['nation_name'])
#
# # 打印转换后的数据
# print(data.head())
#
# # 获取编码字典
# label_dict = {}
# for col in ['seg_route_from', 'seg_route_to', 'seg_cabin', 'gender', 'residence_country', 'nation_name']:
#     le.fit(data[col])
#     le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
#     label_dict[col] = label_dict = {str(k): v for k, v in label_dict.items()}
#
# # 将编码字典保存为json文件
# with open("label_dict.json", "w") as f:
#     json.dump(label_dict, f, ensure_ascii=False, indent=4)

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd
# import json
#
# # # 读取数据
# data = pd.read_csv("../data/smallTest.csv")
#
# # 创建LabelEncoder对象
# le = LabelEncoder()
#
# # 对特征列进行编码转换，并保存编码字典
# le_dict = {}
# data['seg_route_from'] = le.fit_transform(data['seg_route_from'])
# le_dict['seg_route_from'] = dict(zip(le.classes_, le.transform(le.classes_)))
# data['seg_route_to'] = le.fit_transform(data['seg_route_to'])
# le_dict['seg_route_to'] = dict(zip(le.classes_, le.transform(le.classes_)))
# data['seg_cabin'] = le.fit_transform(data['seg_cabin'])
# le_dict['seg_cabin'] = dict(zip(le.classes_, le.transform(le.classes_)))
# data['gender'] = le.fit_transform(data['gender'])
# le_dict['gender'] = dict(zip(le.classes_, le.transform(le.classes_)))
# data['residence_country'] = le.fit_transform(data['residence_country'])
# le_dict['residence_country'] = dict(zip(le.classes_, le.transform(le.classes_)))
# data['nation_name'] = le.fit_transform(data['nation_name'])
# le_dict['nation_name'] = dict(zip(le.classes_, le.transform(le.classes_)))
#
# # 将编码字典写入文件
# with open("le_dict.json", "w") as f:
#     json.dump(le_dict, f)
#
# # 打印转换后的数据
# print(data.head())
