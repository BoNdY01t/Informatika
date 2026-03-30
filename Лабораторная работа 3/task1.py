# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_index(items_list, item): # функция поиска индекса товара
    for i in range(len(items_list)): # перебираем элементы списка
        if items_list[i] == item: # если найден нужный товар
            return i # возвращаем индекс, если товар найдет
    return None # если товар не найден, то возвращаем None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
