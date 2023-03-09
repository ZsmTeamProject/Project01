import pandas as pd

# 读取数据
data = pd.read_csv("version_0.0.1.csv")

# 找到重复数据
duplicated_data = data[data.duplicated()]

# 清洗重复数据
cleaned_data = data.drop_duplicates()

# 保存转换后的数据
data.to_csv("version_0.0.2.csv", index=False)

# 输出清洗后的数据
print(cleaned_data)


