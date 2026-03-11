# ID посылки: 158377868.
# Ссылка на Google-документ: https://docs.google.com/document/d/1tg40PjFCJAkSKY3bR1R-MKkvJY_2mv7qhxAsaXVv8vI/edit?usp=sharing
# Доступ открыт.


def min_platforms(weights: list[int], limit: int) -> int:
    """
    Определяет минимальное количество транспортных платформ.
    """
    weights.sort()
    n = len(weights)
    platforms = 0
    left = 0
    right = n - 1

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
            platforms += 1
        else:
            right -= 1
            platforms += 1

    return platforms


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        weights = list(map(int, file_in.readline().strip().split()))
        limit = int(file_in.readline().strip())
    result = min_platforms(weights, limit)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
