import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection  import train_test_split

import matplotlib.pyplot as plt


#预处理数据
dataset = pd.read_csv('studentscores.csv')
X = dataset.iloc[ : , : 1 ].values
Y = dataset.iloc[ : ,1].values

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)

regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)


Y_pred = regressor.predict(X_test)
plt.scatter(X_train, Y_train, color='red', label='Train Data')

# 测试集点
plt.scatter(X_test, Y_test, color='green', label='Test Data')

# 拟合直线（使用整个数据范围）
X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
plt.plot(X_line, regressor.predict(X_line), color='blue', label='Regression Line')

plt.title('Score vs Hours')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.legend()
plt.show()
