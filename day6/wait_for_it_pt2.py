def wait_for_it(file_input):
    total = 1
    with open(file_input, 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]
    time, distance = (int("".join(lines[0].split(":")[1].strip().split())),
                      int("".join(lines[1].split(":")[1].strip().split())))
    count = 0
    for i in range(time):
        ms = (time - i) * i
        if ms > int(distance):
            count += 1
    total *= count
    return total
