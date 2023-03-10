from sklearn.model_selection import train_test_split
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
import numpy as np

# 读取数据集
data = pd.read_csv("version_0.0.1.csv")

# 定义输入和输出
X = data.drop(['emd_lable2'], axis=1).values
y = data['emd_lable2'].values

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据类型转换
X_train = np.asarray(X_train).astype(np.float32)
y_train = np.asarray(y_train).astype(np.float32)

# 打印训练集和测试集的形状
print("训练集的形状：", X_train.shape, y_train.shape)
print("测试集的形状：", X_test.shape, y_test.shape)

# 将输入数据转换成三维张量（样本数，时间步，特征维度）
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# 创建卷积神经网络模型
model = Sequential()
model.add(Conv1D(32, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))
model.add(Conv1D(64, kernel_size=3, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 训练模型
history = model.fit(X_train, y_train, epochs=50, batch_size=64, validation_split=0.2)

# 输出训练进度
print(history.history)

# 在测试集上评估模型
test_loss, test_acc = model.evaluate(X_test, y_test)
print('测试集上的准确率:', test_acc)

# 保存模型
model.save('my_model.h5')
