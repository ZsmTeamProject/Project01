import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# 读取数据集
data = pd.read_csv("E:/A MNIST/data1/data_cleaned.csv", low_memory=False)

# 定义输入和输出
X = data.drop(['emd_lable2'], axis=1).values
y = data['emd_lable2'].values
X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)
X = np.nan_to_num(X, nan=0.0)

# 创建相同的神经网络模型
model = Sequential()
model.add(Dense(64, input_dim=656, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 加载模型权重
model.load_weights('my_model_weights.h5')

# 测试预测
new_passenger = np.random.rand(1, 656).astype(np.float32)
prediction = model.predict(new_passenger)

if prediction[0] > 0.5:
    print("这个新的乘客可能会选择您的服务")
else:
    print("这个新的乘客可能不会选择您的服务")
