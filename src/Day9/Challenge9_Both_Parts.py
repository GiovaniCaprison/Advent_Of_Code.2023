def next_val(x, d='next'):
    s = [x]

    while not all(v == 0 for v in s[-1]):
        ns = [s[-1][i + 1] - s[-1][i] for i in range(len(s[-1]) - 1)]
        s.append(ns)

    if d == 'next':
        for i in range(len(s) - 2, -1, -1):
            s[i].append(s[i][-1] + s[i + 1][-1])
        return s[0][-1]
    else:
        for i in range(len(s) - 1, 0, -1):
            s[i].insert(0, 0)
            s[i - 1].insert(0, s[i - 1][0] - s[i][1])
        return s[0][0]


fp = '/example/file/path.txt'

with open(fp, 'r') as file:
    h = file.readlines()

h = [list(map(int, line.strip().split())) for line in h]

ans1 = sum(next_val(line, 'next') for line in h)
ans2 = sum(next_val(line, 'prev') for line in h)

print(ans1, ans2)
