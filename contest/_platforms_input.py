# ID посылки: 158377416.
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


if __name__ == '__main__':
    weights_input = list(map(int, input().split()))
    limit_input = int(input())

    result = min_platforms(weights_input, limit_input)
    print(result)
