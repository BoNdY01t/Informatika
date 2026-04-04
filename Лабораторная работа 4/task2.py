# TODO импортировать необходимые молули
import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_:  # читаем csv файл
        csv_data = [row for row in csv.DictReader(csv_)] # десериализуем  данные из csv формата
    with open(OUTPUT_FILENAME, 'w') as json_: # открываем json файл и записываем в него данные
        json.dump(csv_data, json_, indent=4) # сериализуем данные с отступом 4
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
