# Skipping for now
def gear_ratios(file_input):
    with open(file_input, 'r', encoding='UTF-8') as file:
        for i, line in enumerate(file):
            print(i, line)
            for j, char in enumerate(line):
                # print(j, char)
                if char.isdigit():
                    print(i,j,char)


gear_ratios('test.txt')
