def main(nums: list):
    result = []
    n = len(nums)

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        nums = list(map(int, file_in.readline().strip().split()))
    result = main(nums)

    result_str = ' '.join(map(str, result))

    with open('output.txt', 'w') as file_out:
        file_out.write(result_str)
