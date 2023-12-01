string_chars = ['one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']


def main(file_path: str):
    sum = 0
    with open(file_path) as file:
        for line in file:
            nums = []
            for i, char in enumerate(line):
                if char.isdigit():
                    nums.append(char)
                for d, val in enumerate(string_chars):
                    if line[i:].startswith(val):
                        nums.append(str(d+1))
            sum += int(str(nums[0]) + str(nums[-1]))
    return sum


if __name__ == '__main__':
    print(main('files/input.txt'))
