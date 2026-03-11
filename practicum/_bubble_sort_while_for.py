example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    # Устанавливаем значение last_index равным индексу последнего элемента.
    last_index = len(data) - 1
    # Чтобы цикл while мог стартовать, устанавливаем флаг в значение True.
    swapped = True
    # Цикл будет выполняться, если флаг swapped = True. Это значение
    # устанавливается при первом проходе и в случае, если на предыдущем проходе
    # были перестановки. Если перестановок не было, то цикл
    # перестанет выполняться.
    while swapped:
        # Для текущего прохода сбрасываем значение флага на False.
        swapped = False
        # Внутренний цикл - такой же, как и в предыдущем листинге.
        # Формируем внутренний цикл от 0 до last_index (исключая last_index).
        for item_index in range(last_index):
            # Сравниваем значения элементов списка.
            if data[item_index] > data[item_index + 1]:
                # Если значения надо поменять местами - меняем.
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                # Выставляем флаг "выполнена перестановка".
                swapped = True
        # Уменьшаем значение last_index на единицу.
        last_index -= 1
    # Возвращаем отсортированный список.
    return data


print(bubble_sort(example_array))
