def find_min_slice_sum_optimized(data, elements_in_slice):
    # Сумма первого окна
    current_sum = sum(data[:elements_in_slice])
    min_sum = current_sum

    # Скользящее окно: сдвигаем на 1 элемент вправо
    for i in range(elements_in_slice, len(data)):
        # Удаляем крайний левый элемент и добавляем новый правый
        current_sum += data[i] - data[i - elements_in_slice]
        # Обновляем минимальную сумму
        min_sum = min(min_sum, current_sum)

    return min_sum
