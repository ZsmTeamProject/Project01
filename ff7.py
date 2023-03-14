from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import pandas as pd
import pickle

# 导入数据文件并将其转换为DataFrame格式
data = pd.read_csv('E:/A MNIST/data/encoded_train.csv')

# 分离特征列和目标变量列
n_targets = 2
X = data.iloc[:, :-n_targets]
y = data.iloc[:, -n_targets:]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 定义决策树分类器并用训练数据拟合模型
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 使用训练后的模型预测测试数据的目标变量
y_pred = clf.predict(X_test)

# 计算预测结果的准确率
accuracy = accuracy_score(y_test.values.argmax(axis=1), y_pred.argmax(axis=1))

print("Accuracy:", accuracy)

# 保存决策树模型到文件
with open('decision_tree_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# 从文件中加载决策树模型
with open('decision_tree_model.pkl', 'rb') as f:
    clf_loaded = pickle.load(f)

# 使用加载的模型预测新的导入文件的目标变量
X_new = pd.read_csv('E:/A MNIST/data/encoded_test.csv')


imputer = SimpleImputer(strategy='mean')
imputer.fit(X_train)
X_new = imputer.transform(X_new)


y_new_pred = clf_loaded.predict(X_new)

# 输出预测结果
print("Predicted targets:", y_new_pred)
