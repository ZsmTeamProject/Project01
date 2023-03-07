import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据集
data = pd.read_csv('data/.ipynb_checkpoints/train-checkpoint.csv')

# 计算相关系数矩阵
corr_matrix = data.corr()

# 可视化相关系数矩阵
sns.heatmap(corr_matrix, annot=True)
plt.show()
