import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

# 读取数据集
data1 = pd.read_csv(r"D:\pytorch\encoded_train.csv", low_memory=False)
data2 = pd.read_csv(r"D:\pytorch\encoded_test.csv", low_memory=False)

# 定义输入和输出
X1 = data1.drop(labels=['emd_lable2', 'emd_lable'], axis=1).values
y1 = data1['emd_lable2'].values
X2 = data2.drop(labels=['emd_lable', 'emd_lable2'], axis=1).values
y2 = data2['emd_lable2'].values

# 创建神经网络模型
model = Sequential()
model.add(Dense(64, input_dim=655, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 训练模型
model.fit(X1, y1, epochs=100, batch_size=64)

# 评估模型
score = model.evaluate(X2, y2)
print("测试集上的损失和准确率为：", score)

# 保存模型
model.save('my_model.h5')

# 进行预测
new_passenger = np.random.rand(3, 655)  # 生成一个随机的新乘客输入特征，维度为 (1, 51)
prediction = model.predict(new_passenger)
print("选座概率为：", prediction[0][0])

