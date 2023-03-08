import pandas as pd

df = pd.read_csv("../data/SelectedFeatures.csv")
selected_columns = df['字段名'].tolist()

df_csv = pd.read_csv("../data/train.csv")


# 根据被选中的列生成新的数据集
df_selected = df_csv[selected_columns]

# 保存结果到CSV文件
df_selected.to_csv("testdata_output.csv", index=False)