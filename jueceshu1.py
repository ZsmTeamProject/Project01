import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier

# 读取数据集
data = pd.read_csv('zcc.csv')

# 将年龄段转换为数字标签
le = LabelEncoder()
data['age'] = le.fit_transform(data['age'])

# 划分训练集和测试集
X = data.drop('emd_lable2', axis=1)
y = data['emd_lable2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立决策树模型
model = HistGradientBoostingClassifier(max_iter=1000)
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 输出模型准确率
accuracy = (y_pred == y_test).mean()
print(f'模型准确率为：{accuracy:.2%}')
