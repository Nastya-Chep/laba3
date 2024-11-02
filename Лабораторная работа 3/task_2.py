# TODO Напишите функцию find_common_participants

def find_common_participants(first, second, parametr=','):
    first_list = first.split(parametr)
    second_list = second.split(parametr)
    first_list_set = set(first_list)
    second_list_set = set(second_list)

    result = list(first_list_set.intersection(second_list_set))
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, parametr="|")
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
