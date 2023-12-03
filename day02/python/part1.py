import re


def main(file_path: str):
    with open(file_path) as file:
        viable_games = []
        for idx, line in enumerate(file):
            viable_games.append(idx+1)
            for split in re.split(';|,', line.split(':')[1]):
                split = split.strip()
                if 'red' in split:
                    if int(split.split()[0]) > 12:
                        viable_games.remove(idx+1)
                        break
                elif 'green' in split:
                    if int(split.split()[0]) > 13:
                        viable_games.remove(idx+1)
                        break
                elif 'blue' in split:
                    if int(split.split()[0]) > 14:
                        viable_games.remove(idx+1)
                        break
    return sum(viable_games)


if __name__ == '__main__':
    print(main('files/input.txt'))
