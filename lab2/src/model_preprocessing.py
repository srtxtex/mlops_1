import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler


# Создание переменной с путем корневой директории lab2
dirname = os.path.dirname(os.path.dirname(__file__))


# Загрузка данных
train_data = pd.read_csv(os.path.join(dirname, 'data/train/train_data.csv'))
test_data = pd.read_csv(os.path.join(dirname, 'data/test/test_data.csv'))


# Предобработка данных
scaler = MinMaxScaler()
train_data['temperature'] = scaler.fit_transform(train_data[['temperature']])
test_data['temperature'] = scaler.transform(test_data[['temperature']])


# Сохранение предобработанных данных
train_data.to_csv(os.path.join(dirname, 'data/train/train_data_preprocessed.csv'), index=False)
test_data.to_csv(os.path.join(dirname, 'data/test/test_data_preprocessed.csv'), index=False)
