# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def naxod_element(spisock,slovo):
    for i in range(len(spisock)):
        if spisock[i]==slovo:
            return i
    return None




for find_item in ['банан', 'груша', 'персик']:
    index_item =  naxod_element(items_list,find_item)# TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
