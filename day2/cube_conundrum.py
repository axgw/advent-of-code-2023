# Ugly af but I just want to finish
def conundrum(input_file):
    total = 0
    with open(input_file, 'r', encoding='UTF-8') as file:
        for i, line in enumerate(file):
            valid = False
            game_num, games = line.split(':')
            games = games.strip().split(';')
            for game in games:
                game_dict = {color: int(number) for number, color in (string.split() for string in game.split(','))}
                if all(game_dict.get(color, 0) <= limit for color, limit in {'blue': 14, 'red': 12, 'green': 13}.items()):
                    valid = True
                else:
                    valid = False
                    break
            if valid:
                total += i+1
    return total
