# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, a=","): # задана функция
    group1 = str1.split(a) # делю первую группу
    group2 = str2.split(a) # делю вторую группу
    obsh = set(group1) & set(group2) # нахожу общих участников
    return sorted(obsh) # возвращаем отсортированный список

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, a='-'))