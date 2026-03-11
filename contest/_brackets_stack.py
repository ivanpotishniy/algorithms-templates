def main(sequence):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets_map[char]:
                return False
    return not stack


if __name__ == "__main__":
    with open('input.txt', 'r') as file_in:
        sequence = file_in.readline().strip()
    result = main(sequence)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
