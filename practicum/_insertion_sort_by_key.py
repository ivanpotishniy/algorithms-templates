# Длины слов "ноль", "один", "два", "три", "четыре" - и так до двенадцати.
digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]


def card_strength(idx):
    # Получаем количество букв для числа idx.
    return digit_lengths[idx]


# Добавляем в функцию параметр key,
# в него будет передана функция, получающая значение ключа сортировки.
def insertion_sort_by_key(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        # При сравнении элементов вызываем функцию, переданную в параметр key,
        # она вернёт значение ключа.
        while prev >= 0 and key(arr[prev]) > key(current):
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current


cards = [2, 9, 11, 7, 1]
# При вызове сортировки передаём в параметры функцию,
# возвращающую значение ключа.
insertion_sort_by_key(cards, card_strength)
# Для контроля - напечатаем результат:
print(cards)
