import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
# 加载模型
model = joblib.load(filename= 'my_model2.pkl')
# 划分训练集和测试集
X = data.drop('emd_lable2', axis=1)
y = data['emd_lable2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 建立决策树模型，注意在特征集中删除了“emd_lable2”
model = HistGradientBoostingClassifier(max_iter=1000)
model.fit(X_train, y_train)
# 读取 CSV 文件
data = pd.read_csv('zmc.csv')
le = LabelEncoder()
data['age'] = le.fit_transform(data['age'])
# 提取特征
X = data.values

# 进行预测
y_pred = model.predict(X)

# 输出预测结果
print(y_pred)
