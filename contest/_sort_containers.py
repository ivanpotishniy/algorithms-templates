def sort_containers(containers, pattern):
    # Подсчитываем частоту каждого контейнера с помощью обычного словаря
    freq = {}
    for num in containers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []

    # Обрабатываем контейнеры в порядке шаблона
    for num in pattern:
        if num in freq:
            # Добавляем все экземпляры числа num в результат
            result.extend([num] * freq[num])
            # Удаляем число из словаря частот, чтобы не обрабатывать его позже
            del freq[num]

    # Оставшиеся числа (не упомянутые в шаблоне) сортируем по возрастанию
    remaining = []
    for num, count in freq.items():
        # Расширяем список оставшимися числами с учётом их частоты
        remaining.extend([num] * count)
    # Сортируем оставшиеся числа
    remaining.sort()

    # Добавляем их в конец результата
    result.extend(remaining)

    return result


# Чтение ввода
if __name__ == '__main__':
    n = int(input())  # Количество чисел для сортировки
    containers = list(map(int, input().split()))  # Массив контейнеров
    m = int(input())  # Длина массива-шаблона
    pattern = list(map(int, input().split()))  # Шаблон-инструкция

    # Получаем отсортированный массив
    sorted_containers = sort_containers(containers, pattern)
    # Выводим результат через пробел
    print(' '.join(map(str, sorted_containers)))
