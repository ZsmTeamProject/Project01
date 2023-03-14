import pandas as pd

# 读取Excel文件
df = pd.read_excel("data_description.xlsx")

# 根据第四列的布尔值进行过滤
df = df[df.iloc[:, 3] == 1]

selected_columns = df[df['第一遍人工筛选 感兴趣的数据列'] == True]['字段名'].tolist()

df_csv = pd.read_csv("../data/train.csv", index_col=0)

df_selected = df_csv[selected_columns]

df_selected.to_csv("output.csv", index=False)

