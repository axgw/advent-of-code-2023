def conundrum(input_file):
    total = 0
    with open(input_file, 'r', encoding='UTF-8') as file:
        for i, line in enumerate(file):
            game_num, games = line.split(':')
            games = games.strip().split(';')
            blue = green = red = 0
            for game in games:
                game_dict = {color: int(number) for number, color in (string.split() for string in game.split(','))}
                if game_dict.get('blue', 0) > blue:
                    blue = game_dict.get('blue')
                if game_dict.get('red', 0) > red:
                    red = game_dict.get('red')
                if game_dict.get('green', 0) > green:
                    green = game_dict.get('green')
            power = red * blue * green
            total += power
        return total
