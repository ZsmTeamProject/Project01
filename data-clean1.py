import pandas as pd

# 读取 CSV 文件并选取需要处理的列范围
df = pd.read_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\train-checkpoint.csv", low_memory=False)
cols = df.columns[362:372]

# 定义将大写字母转换为小写字母的函数
def convert_lower_case(x):
    if isinstance(x, str):
        return x.lower()
    else:
        return x

# 使用 applymap() 方法将指定列范围内的数据中的大写字母转换为小写字母
df[cols] = df[cols].applymap(convert_lower_case)

# 将处理后的数据写入新的 CSV 文件中
df.to_csv("C:\\Users\\19678\\Desktop\\data\\.ipynb_checkpoints\\test.csv", index=False)
