file_path = '/example/file/path.txt'

with open(file_path, 'r') as file:
    data = file.read()

data_array = data.strip().splitlines()
rocks = {
    (r, c): x
    for r, line in enumerate(data_array)
    for c, x in enumerate(line)
}

moved = True
while moved:
    moved = False
    for r in range(1, len(data_array)):
        for c in range(len(data_array[0])):
            if rocks[(r, c)] != 'O':
                continue
            if rocks[(r - 1, c)] == '.':
                moved = True
                rocks[(r - 1, c)] = 'O'
                rocks[(r, c)] = '.'

answer_a = sum(
    len(data_array) - r
    for (r, _), x in rocks.items()
    if x == 'O'
)

# PART 2: Implementing the tilt and cycle functions
def rocks_from_str(str):
    return {
        (r, c): x
        for r, line in enumerate(str.strip().splitlines())
        for c, x in enumerate(line)
    }

def str_from_rocks(rocks):
    return '\n'.join(
        ''.join(
            rocks[(r, c)]
            for c in range(len(data_array[0]))
        )
        for r in range(len(data_array))
    )

def tilt(rocks_str, dir):
    rocks = rocks_from_str(rocks_str)
    moved = True
    while moved:
        moved = False
        for r in range(0, len(data_array)):
            if r + dir[0] not in range(0, len(data_array)):
                continue
            for c in range(len(data_array[0])):
                if c + dir[1] not in range(0, len(data_array[0])):
                    continue
                if rocks[(r, c)] != 'O':
                    continue
                if rocks[(r + dir[0], c + dir[1])] == '.':
                    moved = True
                    rocks[(r + dir[0], c + dir[1])] = 'O'
                    rocks[(r, c)] = '.'
    return str_from_rocks(rocks)

def cycle(rocks_str):
    return tilt(tilt(tilt(tilt(rocks_str, (-1, 0)), (0, -1)), (1, 0)), (0, 1))

rocks_str = data
for _ in range(1000000000): 
    rocks_str += cycle(rocks_str)

answer_b = sum(
    len(data_array) - r
    for (r, _), x in rocks_from_str(rocks_str).items()
    if x == 'O'
)

print(answer_a, answer_b)
