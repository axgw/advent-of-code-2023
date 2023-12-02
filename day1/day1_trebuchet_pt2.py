numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def trebuchet(input_file):
    final2 = []
    s = []
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file:
            final = []
            temp = line.strip('\n')
            for word, value in numbers.items():
                temp = temp.replace(word, value)
            # if temp.strip().isdigit():
            final.append(temp)
            s = []
            for i in range(len(final)):
                for j in final[i]:
                    if j.isdigit():
                        s.append(int(j))
            final2.append(s[0] * 10 + s[0]) if len(s) == 1 else final2.append(s[0] * 10 + s[-1])
        print(final2)
    total = sum(final2[k] for k in range(len(final2)))
    print(total)

trebuchet('test.txt')
