import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据集
data = pd.read_csv('../data/train.csv', low_memory=False)
# 读取字典
excel_data = pd.read_excel('data_description.xlsx', header=None)
# # 本次第三列为标注的感兴趣数据
# Select_Num = 3
# # 本次项目以字段名为索引
# Index = 1
# # 设置第一次人工筛选得到的数列
#
# column_list = []
# for row in excel_data.values:
#     row_list = row.tolist()
#     if row_list[Select_Num] == 1:
#         # 得到所需字段的字段名list
#         column_list.append(row_list[Index])
# column_list = pd.array(column_list)
# print("")
#
# selected_columns = [column for column in data.columns if column_list.get(column) == '1']
# selected_data = data.loc[:, selected_columns]
# # # 计算相关系数矩阵
# # corr_matrix = data.corr(numeric_only=True)
# # # 可视化相关系数矩阵
# # sns.heatmap(corr_matrix, annot=True)
# # plt.show()
