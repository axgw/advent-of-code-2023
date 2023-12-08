def wait_for_it(file_input):
    total = 1
    with open(file_input, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
    time, distance = lines[0].split(':')[1].split(), lines[1].split(':')[1].split()
    for t in range(len(time)):
        count = 0
        for i in range(int(time[t])):
            ms = (int(time[t]) - i) * i
            if ms > int(distance[t]):
                count += 1
        total *= count
    return total
