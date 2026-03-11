def main(arr):
    n = len(arr)

    # Условие 1: длина массива должна быть не менее 3
    if n < 3:
        return False

    i = 0

    # Этап 1: подъём — идём, пока высоты строго возрастают
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Проверяем, что вершина не первая и не последняя
    # Если i == 0 — не было подъёма
    # Если i == n - 1 — вершина в конце, нет спуска
    if i == 0 or i == n - 1:
        return False

    # Этап 2: спуск — идём, пока высоты строго убывают
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # Если дошли до конца массива — гора правильная
    return i == n - 1


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        arr = list(map(int, file_in.readline().strip().split()))

    result = main(arr)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
