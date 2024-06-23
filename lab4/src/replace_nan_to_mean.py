import pandas as pd
import os


# Создание переменной с путем корневой директории lab1
dirname = os.path.dirname(os.path.dirname(__file__))

# Загрузка датасета
df = pd.read_csv(os.path.join(dirname, 'datasets/titanic/titanic_data.csv'))

# Заполнение пропущенных значений в поле "Age" средним значением
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Сохранение новой версии датасета
df.to_csv(os.path.join(dirname, 'datasets/titanic/titanic_data.csv'), index=False)
