# TODO решите задач

import json # импортируем
def task() -> float:
    with open('input.json', 'r') as f: #открываем файл с данными
        data = json.load(f) # десериализация данных из файла
    total = 0 # вводим счётчик суммы
    for item in data:
        total += item.get('score', 0) * item.get('weight', 0) # считаем произведение значений очков и веса, найденных по ключам(если нет значения, то 0)
        round_ = round(total, 3) # округляем до 3 знаком после запятой
    return round_ # возвращаемся к итоговому значению
print(task())