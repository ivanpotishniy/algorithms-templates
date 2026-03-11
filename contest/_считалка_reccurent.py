def find_winner_recursive(n, k):
    # Базовый случай: если остался один претендент, он — победитель
    if n == 1:
        return 1
    else:
        # Рекурсивный вызов для n−1 претендентов
        # Корректируем результат, чтобы учесть сдвиг из‑за выбывания
        return (find_winner_recursive(n - 1, k) + k - 1) % n + 1


# Чтение ввода и вывод результата
if __name__ == '__main__':
    n = int(input())  # Количество претендентов
    k = int(input())  # Количество тактов в считалке
    print(find_winner_recursive(n, k))
