# TODO Напишите функцию find_common_participants
def find_common_participants(str1,str2,split=','):
    str1_list_set=set(str1.split(split))
    str2_list_set=set(str2.split(split))
    common_participants = str1_list_set.intersection(str2_list_set)
    return(list(common_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group,participants_second_group,split='|')