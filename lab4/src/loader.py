from catboost.datasets import titanic
import os


# Создание переменной с путем корневой директории lab1
dirname = os.path.dirname(os.path.dirname(__file__))

# Загрузка датасета
data_df, _ = titanic()

# Сохранение в CSV
data_df.to_csv(os.path.join(dirname, 'datasets/titanic/titanic_data.csv'), index=False)
