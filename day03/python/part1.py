
def exists_symbol_nearby(start_pos: tuple[int, int],
                         len_number: int,
                         map: dict[tuple[int, int], str],
                         current_number):
    for i in range(max(start_pos[0] - 1, 0), start_pos[0] + 2):
        for j in range(max(start_pos[1] - 1, 0), start_pos[1] + len_number + 1):
            if current_number == '253':
                print(start_pos, len_number)
                print(i, j, map.get((i, j)))
            if result := map.get((i, j)):
                if current_number == '253':
                    print(result)
                if not str.isnumeric(result) and result != '.':
                    return True
    return False


def main(file_path: str):
    sum = 0
    with open(file_path) as file:
        map = {}
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip() + '.'):
                map[i, j] = char
        current_number = ''
        for key, value in map.items():
            if str.isnumeric(value):
                if current_number == '':
                    start_pos = key
                current_number += value
            else:
                if current_number != '':
                    final_j = key[1]
                    number_lenght = final_j - start_pos[1]
                    if exists_symbol_nearby(start_pos, number_lenght, map, current_number):
                        sum += int(current_number)
                    current_number = ''
    return sum


if __name__ == '__main__':
    print(main('files/input.txt'))
