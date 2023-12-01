
def main(file_path: str):
    sum = 0
    with open(file_path) as file:
        for line in file:
            nums = []
            for char in line:
                if char.isdigit():
                    nums.append(char)
            print(nums)
            sum += int(str(nums[0]) + str(nums[-1]))
    return sum


if __name__ == '__main__':
    print(main('input.txt'))
