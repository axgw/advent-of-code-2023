def scratchcard(input_file):
    total = 0
    with open(input_file, 'r', encoding='UTF=8') as file:
        for line in file:
            title, numbers = line.split(':')
            your_num, win_num = numbers.strip().split('|')
            winning_nums = [num for num in your_num.split() if num in win_num.split()]
            if winning_nums:
                for n in winning_nums:
                    points = 2**(len(winning_nums)-1)
            total += points
    return total
