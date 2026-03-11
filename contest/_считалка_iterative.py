def find_winner_iterative(n, k):
    # Создаём список претендентов: [1, 2, ..., n]
    participants = list(range(1, n + 1))
    current_index = 0  # Начинаем с первого претендента

    while len(participants) > 1:
        # Вычисляем индекс выбывающего: сдвигаем на (k−1) шагов вперёд с учётом круга
        elimination_index = (current_index + k - 1) % len(participants)
        # Удаляем выбывшего претендента
        participants.pop(elimination_index)
        # Следующий старт — элемент сразу после выбывшего (или первый, если вышли за конец)
        current_index = elimination_index % len(participants)

    return participants[0]


# Чтение ввода и вывод результата
if __name__ == '__main__':
    n = int(input())  # Количество претендентов
    k = int(input())  # Количество тактов в считалке
    print(find_winner_iterative(n, k))
