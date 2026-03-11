def main(nums: list):
    # Создаём пары (значение, исходный индекс)
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    # Сортируем по значениям
    indexed_nums.sort()

    result = [0] * len(nums)
    count = 0  # счётчик уникальных меньших значений

    for i in range(len(indexed_nums)):
        # Если текущее значение больше предыдущего, увеличиваем счётчик
        if i > 0 and indexed_nums[i][0] > indexed_nums[i-1][0]:
            count = i
        # Записываем количество меньших элементов по исходному индексу
        original_index = indexed_nums[i][1]
        result[original_index] = count
    return result


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        nums = list(map(int, file_in.readline().strip().split()))
    result = main(nums)

    result_str = ' '.join(map(str, result))
    print(result_str)

    with open('output.txt', 'w') as file_out:
        file_out.write(result_str)
