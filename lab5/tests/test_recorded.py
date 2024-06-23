
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# Функция для генерации данных
def generate_data(n_samples, noise_factor=0.0):
    X = np.random.rand(n_samples, 1) * 10
    y = 2 * X.squeeze() + 3 + np.random.randn(n_samples) * noise_factor
    return X, y


# Функция для тестирования модели
def check_model(X_test, y_test, model):
    y_pred = model.predict(X_test)
    return root_mean_squared_error(y_test, y_pred)


# Функция для тестирования модели с выводом информации о датасете
def test_model_performance():
    # Создание модели линейной регрессии
    model = LinearRegression()

    # Генерация трех датасетов с качественными данными и шумового датасета
    quality_datasets = [generate_data(100, noise_factor=0.5) for _ in range(3)]
    noisy_dataset = generate_data(100, noise_factor=5)

    # Обучение модели на одном из датасетов с качественными данными
    model.fit(*quality_datasets[0])

    # Вычисление максимального RMSE на качественных данных
    max_rmse_quality = max(root_mean_squared_error(y, model.predict(X)) for X, y in quality_datasets)

    # Функция для проверки RMSE каждого датасета
    def check_rmse(X_test, y_test, dataset_name):
        rmse = check_model(X_test, y_test, model)
        assert rmse <= max_rmse_quality, f"Датасет {dataset_name} является шумовым: RMSE: {rmse}"

    # Проверяем RMSE для каждого датасета
    for idx, (X, y) in enumerate(quality_datasets, start=1):
        check_rmse(X, y, f"датасет {idx}")
    check_rmse(*noisy_dataset, "датасет 4")
