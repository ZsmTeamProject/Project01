import pickle

# 导入模型
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# 准备输入数据
sample = [[1, 2, 3, 4]] # 输入数据必须是二维数组

# 进行预测
prediction = model.predict(sample)

# 解释输出
print(prediction)
