numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def trebuchet(input_file):
    total = 0
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file:
            final = []
            for i, number in enumerate(numbers):
                if number in line:
                    line = line.replace(number, f'{number[0]}{i+1}{number[-1]}')
            num = [int(char) for char in line if char.rstrip().isdigit()]
            final.append(num[0] * 10 + num[0]) if len(num) == 1 else final.append(num[0] * 10 + num[-1])
            total += sum([k for k in final])
    return total
