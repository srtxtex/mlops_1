import joblib
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error


# Создание переменной с путем корневой директории lab2
dirname = os.path.dirname(os.path.dirname(__file__))


# Загрузка предобработанных данных
data = pd.read_csv(os.path.join(dirname, 'data/train/train_data_preprocessed.csv'))
X = data[['day']]
y = data['temperature']


# Разделение данных на обучающую и валидационную выборки
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=37)


# Создание и обучение модели
model = LinearRegression().fit(X_train, y_train)


predictions = model.predict(X_train)
rmse = root_mean_squared_error(y_train, predictions)


print(f'Root mean squared error for the train set: {rmse}')


# Сохранение модели
joblib.dump(model, os.path.join(dirname, 'data/model/model.pkl'))
