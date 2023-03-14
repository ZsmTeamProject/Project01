import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

# 读取数据集
data = pd.read_csv("encoded_data_final.csv")

# 将年龄段特征进行独热编码
age = pd.get_dummies(data['age'], prefix='age')
data = pd.concat([data, age], axis=1)
data.drop('age', axis=1, inplace=True)

# 定义输入和输出
X = data.drop(['emd_lable2'], axis=1).values.astype('float32')
y = data['emd_lable2'].values.astype('float32')

# 创建神经网络模型
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 训练模型
model.fit(X, y, epochs=20, batch_size=32)
new_passenger = [[...]]  # 一个新的乘客的输入特征
prediction = model.predict(new_passenger)

if prediction > 0.5:
    print("这个新的乘客可能会选择您的服务")
else:
    print("这个新的乘客可能不会选择您的服务")

modle