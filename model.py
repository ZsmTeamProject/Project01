import pandas as pd
from sklearn.decomposition import PCA

# 读取数据集
data = pd.read_csv(r"D:\pytorch\data_cleaned.csv", low_memory=False)
print(data.shape)

# 提取输入特征 X
X = data.drop(['emd_lable2'], axis=1).values

# 将数据降低到 100 维
pca = PCA(n_components=101)
X_pca = pca.fit_transform(X)

# 创建新的 DataFrame 对象
new_data = pd.DataFrame(X_pca, columns=['feature_{}'.format(i) for i in range(1, 102)])

# 添加目标变量
new_data['emd_lable2'] = data['emd_lable2'].values

# 将新数据集保存为 CSV 文件
new_data.to_csv('data_pca.csv', index=False)