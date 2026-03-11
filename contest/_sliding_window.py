def longest_unique_substring(s):
    seen = set()  # Множество символов в текущем окне
    left = 0  # Левый указатель окна
    max_length = 0  # Максимальная длина найденной подстроки

    for right in range(len(s)):  # Правый указатель движется по строке
        # Если символ уже в окне, сдвигаем left, пока не уберём дубликат
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Добавляем текущий символ в окно
        seen.add(s[right])

        # Обновляем максимальную длину, если текущее окно больше
        max_length = max(max_length, right - left + 1)

    return max_length


# Чтение ввода и вывод результата
if __name__ == '__main__':
    input_string = input().strip()
    print(longest_unique_substring(input_string))
