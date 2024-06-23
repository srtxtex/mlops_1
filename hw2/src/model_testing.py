from sklearn.metrics import root_mean_squared_error
import pandas as pd
import joblib
import os


# Создание переменной с путем корневой директории hw1
dirname = os.path.dirname(os.path.dirname(__file__))


# Загрузка модели
model = joblib.load(os.path.join(dirname, 'data/model/model.pkl'))


# Загрузка тестовых данных
test_data = pd.read_csv(os.path.join(dirname, 'data/test/test_data_preprocessed.csv'))
X_test = test_data[['day']]
y_test = test_data['temperature']


# Предсказание и оценка модели
predictions = model.predict(X_test)
rmse = root_mean_squared_error(y_test, predictions)


print(f'Root mean squared error for the test set: {rmse}')
