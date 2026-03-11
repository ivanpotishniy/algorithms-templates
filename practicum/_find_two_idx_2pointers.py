def find_two_indexes(data, expected_sum):
    left = 0
    right = len(data) - 1

    while left < right:
        current_sum = data[left] + data[right]

        if current_sum == expected_sum:
            return (left, right)
        elif current_sum < expected_sum:
            left += 1  # Увеличиваем сумму, сдвигая левый указатель вправо
        else:
            right -= 1  # Уменьшаем сумму, сдвигая правый указатель влево

    return None  # Пара не найдена


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))  # Вывод: (2, 6)
