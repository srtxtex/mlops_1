# MLOps. Практическое задание №4


### Выполнено практическое задание
    В рамках данного задания выполнены все основные операции с dvc. 
    Полученные теоретические знания, закрепленены, практическими действиями.

### Ссылки
- [Репозиторий с кодом](https://github.com/srtxtex/mlops_1/tree/main/lab4)
- [README](https://github.com/srtxtex/mlops_1/tree/main/lab4/README.md)
- [Функции для предобработки данных](https://github.com/srtxtex/mlops_1/tree/main/lab4/src)
- [Облачное хранилище датасетов](https://drive.google.com/drive/folders/1PvJ4t8kA0r0PnPSAi2AYVc0fDBQasxeO?usp=sharing)
- [файл DVC для отслеживания версий данных](https://github.com/srtxtex/mlops_1/tree/main/lab4/datasets.dvc)

### Коммиты
```
$ git log --oneline
eae6db3 (HEAD -> main, origin/main) Update titanic dataset: "Add one-hot-encoding for sex field"
3d94bc1 Update titanic dataset: nan values replace to mean
53cc195 Update info Passenger 1. Change Pclass, Sex, Age
d6547e9 improvements scripts
79f4ade load titanic dataset
4f01c10 hw4
e95a0ab hw4
30b4300 hw4
```
### Дополнения
Для переключения между версиями датасета использовал следующую конструкцию
```
git log --oneline
git checkout <commit_id>
dvc pull
```
Для возвращения к текущей актуальной версии датасета
```
git checkout main
dvc pull
```