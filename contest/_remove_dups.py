def main(n: int, array: list):
    if n == 0:
        return array

    write_index = 1

    for read_index in range(1, n):
        if array[read_index] != array[write_index - 1]:
            array[write_index] = array[read_index]
            write_index += 1

    for i in range(write_index, n):
        array[i] = '_'

    return array


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline().strip())
        array = list(map(int, file_in.readline().strip().split()))
    result = main(n, array)

    result_str = ' '.join(map(str, result))

    with open('output.txt', 'w') as file_out:
        file_out.write(result_str)
