wins = [1, 3, 5, 6]
target = 5


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""

    left = 0
    right = len(sorted_numbers)

    # Пока левая граница меньше правой или равна ей:
    while left < right:
        mid = (left + right) // 2

        if sorted_numbers[mid] == element:
            return mid

        if sorted_numbers[mid] < element:
            left = mid + 1
        else:
            right = mid

    # Если левая граница оказалась больше правой,
    # значит, элемент не найден. Возвращаем None.
    return None


print(find_element(wins, target))
