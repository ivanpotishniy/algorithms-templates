def main(array: list[int], n: int) -> int:
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] < n:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        array = list(map(int, file_in.readline().strip().split()))
        n = int(file_in.readline().strip())

    result = main(array, n)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
