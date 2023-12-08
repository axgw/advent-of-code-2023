# lines = [
#     "123",
#     "4x5",
#     "678"
# ]
# def get_numbers(line: str, pos: int):
#     num = "0"
#     for i in range(pos, len(line)):
#         if line[i].isdigit():
#             num += line[i]
#         else:
#             break
#     return int(num)


def gear_ratios(file_input: str):
    with open(file_input, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
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
                    print("end")


gear_ratios('test.txt')
