from typing import List
h = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}
def parse(ms: List[str]) -> List[List[str]]:
    return [list(row) for row in ms]
def move(x: int, y: int, grid: List[List[str]], v: set) -> bool:
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in v
def main(x: int, y: int, arr: List[List[str]], v: set, len: int) -> int:
    if x == len(arr) - 1:
        return len
    v.add((x, y))
    lp = len
    for dx, dy in h.values():
        xx, yy = x + dx, y + dy
        if move(xx, yy, arr, v) and arr[xx][yy] != '#':
            if arr[x][y] in h and (dx, dy) != h[arr[x][y]]:
                continue
            lp = max(lp, main(xx, yy, arr, v, len + 1))
    v.remove((x, y))
    return lp
with open("/example/file/path.txt", "r") as file:
    map = file.readlines()
arr = parse(map)
x, y = 0, arr[0].index('.')
ans = main(x, y, arr, set(), 0)
print(ans)
