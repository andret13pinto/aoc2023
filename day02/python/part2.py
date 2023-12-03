import re

from functools import reduce
from operator import mul


def main(file_path: str):
    sum = 0
    with open(file_path) as file:
        for _, line in enumerate(file):
            max_dict = {'red': 0, 'green': 0, 'blue': 0}
            for split in re.split(';|,', line.split(':')[1]):
                split = split.strip()
                for key, value in max_dict.items():
                    cand = int(split.split()[0])
                    if key in split and cand > value:
                        max_dict[key] = cand
            curr_sum = reduce(mul, list(max_dict.values()))
            sum += curr_sum
    return sum


if __name__ == '__main__':
    print(main('files/input.txt'))
