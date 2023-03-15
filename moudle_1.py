from sklearn.model_selection import train_test_split
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
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

# 创建神经网络模型
model = Sequential()
model.add(Dense(64, input_dim=50, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 定义 EarlyStopping 回调函数
early_stopping = EarlyStopping(monitor='val_loss', patience=8, verbose=1, mode='min')

# 训练模型
history = model.fit(X_train, y_train, epochs=1000, batch_size=8, validation_split=0.2, callbacks=[early_stopping])

# 输出训练进度
print(history.history)

# 在测试集上评估模型
test_loss, test_acc = model.evaluate(X_test, y_test)
print('测试集上的准确率:', test_acc)

# 保存模型
model.save('my_model.h5')


