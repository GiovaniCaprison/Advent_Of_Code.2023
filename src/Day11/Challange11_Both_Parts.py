class Grid:
    def __init__(self):
        self.grid = {}

    def x_range(self):
        return range(max(x for x, _ in self.grid.keys()) + 1)

    def y_range(self):
        return range(max(y for _, y in self.grid.keys()) + 1)

    @classmethod
    def from_text(cls, text):
        grid = cls()
        for y, line in enumerate(text):
            for x, char in enumerate(line):
                grid.grid[(x, y)] = char
        return grid


def calc(values, mode):
    grid = Grid.from_text(values)

    empty_col = []
    empty_row = []

    for x in grid.x_range():
        if sum(0 if grid.grid[(x, y)] == "." else 1 for y in grid.y_range()) == 0:
            empty_col.append(x)
    for y in grid.y_range():
        if sum(0 if grid.grid[(x, y)] == "." else 1 for x in grid.x_range()) == 0:
            empty_row.append(y)

    stars = []
    for (x, y), val in grid.grid.items():
        if val == "#":
            stars.append((x, y))

    ret = 0
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            ax, ay = stars[i]
            bx, by = stars[j]

            ax, bx = min(ax, bx), max(ax, bx)
            ay, by = min(ay, by), max(ay, by)

            count = 0
            count -= 1
            for x in range(ax, bx + 1):
                if x in empty_col:
                    count += 1 if mode == 1 else (1000000 - 1)
                count += 1
            count -= 1
            for y in range(ay, by + 1):
                if y in empty_row:
                    count += 1 if mode == 1 else (1000000 - 1)
                count += 1
            ret += count

    return ret


fp = '/example/file/path.txt'

with open(fp, 'r') as file:
    data = file.readlines()

initial_grid = [line.strip() for line in data]

print(calc(initial_grid, mode=1))
print(calc(initial_grid, mode=1000000))
