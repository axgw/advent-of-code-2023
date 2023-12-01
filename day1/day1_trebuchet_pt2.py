numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def trebuchet(input_file):
    final = []
    with open(input_file, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            final = []
            for word, value in numbers.items():
                if word in line or str(value) in line:
                    final.append(value)
            print(final)

trebuchet('input.txt')
