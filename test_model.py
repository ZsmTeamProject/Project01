import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# 加载模型
loaded_model = load_model('my_model.h5')

# 读取数据集
data = pd.read_csv(r"D:\pytorch\encoded_test.csv", low_memory=False)

# 定义输入和输出
X = data.drop(['emd_lable2', 'emd_lable'], axis=1).values
y = data['emd_lable2'].values

# 评估模型
score = loaded_model.evaluate(X, y)
print("测试集上的损失和准确率为：", score)
