import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# 读取数据集
data = pd.read_csv("zcc.csv")

le = LabelEncoder()
data['age'] = le.fit_transform(data['age'])
# 定义输入和输出
X = data.drop(['emd_lable2'], axis=1).values
y = data['emd_lable2'].values

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建决策树模型
# 创建决策树模型
model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)


# 训练模型
model.fit(X_train, y_train)

# 在测试集上评估模型
test_acc = model.score(X_test, y_test)
print('测试集上的准确率:', test_acc)

# 保存模型
joblib.dump(model, 'my_model2.pkl')
