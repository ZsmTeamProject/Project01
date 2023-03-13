import pandas as pd

# 读取Excel文件
df = pd.read_excel("DataDictionary.xlsx")


for idx, row in df.iterrows():
    # 选中需要筛选的字段
    name = row.loc["字段名"]
    if name.endswith('_cnt'):
        # 改为_y3
        df.at[idx, "字段名"] = name + '_y3'
        print(df.loc[idx, "字段名"])


# 获取被选中的字段名
# selected_columns = df['字段名'].tolist()
selected_columns = df['字段名']
selected_columns.to_csv("SelectedFeatures.csv", index=False)

