# Extracting the grid from the test cases
G = test_cases_lines
H = len(G)
W = len(G[0])

# Initialize the output grid for part 2
O = [[0]*W for _ in range(H)]

# Finding the position of 'S'
ax, ay = -1, -1
for i in range(H):
    for j in range(W):
        if "S" in G[i]:
            ax = i
            ay = G[i].find("S")
            break
    if ax != -1:
        break

# Defining directions and checking valid directions from 'S'
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # rightward, downward, leftward, upward
happy = ["-7J", "|LJ", "-FL", "|F7"]
Sdirs = []
for i in range(4):
    pos = dirs[i]
    bx = ax + pos[0]
    by = ay + pos[1]
    if 0 <= bx < H and 0 <= by < W and G[bx][by] in happy[i]:
        Sdirs.append(i)
Svalid = 3 in Sdirs  # part 2

# Transformations based on current direction and pipe type
transform = {
    (0, "-"): 0,
    (0, "7"): 1,
    (0, "J"): 3,
    (2, "-"): 2,
    (2, "F"): 1,
    (2, "L"): 3,
    (1, "|"): 1,
    (1, "L"): 0,
    (1, "J"): 2,
    (3, "|"): 3,
    (3, "F"): 0,
    (3, "7"): 2,
}

# Traversing the loop
curdir = Sdirs[0]
cx = ax + dirs[curdir][0]
cy = ay + dirs[curdir][1]
ln = 1
O[ax][ay] = 1  # Part 2
while (cx, cy) != (ax, ay):
    O[cx][cy] = 1  # Part 2
    ln += 1
    curdir = transform[(curdir, G[cx][cy])]
    cx = cx + dirs[curdir][0]
    cy = cy + dirs[curdir][1]

# Counting the enclosed area
ct = 0
for i in range(H):
    inn = False
    for j in range(W):
        if O[i][j]:
            if G[i][j] in "|JL" or (G[i][j] == "S" and Svalid):
                inn = not inn
        else:
            ct += inn

print(ln // 2, ct)
