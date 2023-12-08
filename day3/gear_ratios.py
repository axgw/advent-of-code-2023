# lines = [
#     "123",
#     "4x5",
#     "678"
# ]
def get_indexes(line: str, pos: int):
    first = second = 0
    # movida
    return (first, second)


def get_number_from_indexes(line: str, first: int, second: int) -> int:
    pass


def get_numbers(line: str, pos: int):
    num = "0"
    for i in range(pos, len(line)):
        if line[i].isdigit():
            num += line[i]
        else:
            break
    return int(num)


def gear_ratios(file_input: str):
    with open(file_input, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
        counter = 0
        for i in range(len(lines)):
            for j in range(len(lines)):
                if lines[i][j].isdigit():
                    adjacent = [
                        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1),                     (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
                    ]
                    for ai, aj in adjacent:
                        if 0 <= ai < len(lines) and 0 <= aj < len(lines[0]):
                            print(lines[ai][aj])
                        # if digit
                        #   check what number is using left and right
                        #   numbers
                        #   add that number to counter
                    print("end")


gear_ratios('test.txt')
