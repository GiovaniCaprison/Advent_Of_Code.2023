def parse_game_data(file_path):
    with open(file_path, 'r') as file:
        game_lines = file.readlines()

    games = {}
    for line in game_lines:
        parts = line.split(': ')
        game_id = int(parts[0].split(' ')[1])
        draws = parts[1].split('; ')
        cube_draws = []

        for draw in draws:
            cubes = draw.strip().split(', ')
            cube_count = {'red': 0, 'green': 0, 'blue': 0}
            for cube in cubes:
                count, color = cube.split(' ')
                cube_count[color] = int(count)
            cube_draws.append(cube_count)

        games[game_id] = cube_draws
    return games


def find_possible_games(games, red_cubes, green_cubes, blue_cubes):
    possible_game_ids = []
    for game_id, draws in games.items():
        possible = True
        for draw in draws:
            if draw['red'] > red_cubes or draw['green'] > green_cubes or draw['blue'] > blue_cubes:
                possible = False
                break
        if possible:
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)


def find_minimum_cubes(games):
    min_cubes_per_game = {}
    for game_id, draws in games.items():
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws:
            min_cubes['red'] = max(min_cubes['red'], draw['red'])
            min_cubes['green'] = max(min_cubes['green'], draw['green'])
            min_cubes['blue'] = max(min_cubes['blue'], draw['blue'])
        min_cubes_per_game[game_id] = min_cubes
    return min_cubes_per_game


def calculate_power_of_sets(min_cubes_per_game):
    total_power = 0
    for min_cubes in min_cubes_per_game.values():
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += power
    return total_power


# Main execution
file_path = '/example/file/path.txt'
games = parse_game_data(file_path)

# Task 1: Find the sum of the IDs of the possible games
sum_possible_game_ids = find_possible_games(games, 12, 13, 14)
print(f'Sum of IDs of possible games: {sum_possible_game_ids}')

# Task 2: Find the minimum cubes and calculate the power of these sets
min_cubes_per_game = find_minimum_cubes(games)
sum_power_of_sets = calculate_power_of_sets(min_cubes_per_game)
print(f'Sum of the power of the minimum sets: {sum_power_of_sets}')
