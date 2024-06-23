import numpy as np
import pandas as pd
import os


# Создание переменной с путем корневой директории hw1
dirname = os.path.dirname(os.path.dirname(__file__))


# Создание папок для хранения данных
os.makedirs(os.path.join(dirname, 'data/train'), exist_ok=True)
os.makedirs(os.path.join(dirname, 'data/test'), exist_ok=True)


# Функция для генерации данных
def create_data(anomaly_prob=0.05, noise_std=0.5):
    np.random.seed(37)
    days = np.arange(1, 367)
    temperatures = np.sin(days / 366 * 2 * np.pi) * 30 + 10
    anomalies = np.random.choice([0, 1], size=len(days), p=[1 - anomaly_prob, anomaly_prob])
    temperatures[anomalies == 1] += np.random.normal(scale=noise_std, size=np.sum(anomalies))
    return days, temperatures


# Генерация данных для обучения и тестирования
train_days, train_temps = create_data()
test_days, test_temps = create_data()


# Сохранение данных в файлы
pd.DataFrame({'day': train_days, 'temperature': train_temps}).to_csv(os.path.join(dirname, 'data/train/train_data.csv'), index=False)
pd.DataFrame({'day': test_days, 'temperature': test_temps}).to_csv(os.path.join(dirname, 'data/test/test_data.csv'), index=False)
