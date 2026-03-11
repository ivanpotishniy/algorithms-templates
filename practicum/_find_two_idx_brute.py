def find_two_indexes(data, expected_sum):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == expected_sum:
                return (i, j)
    return None


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
