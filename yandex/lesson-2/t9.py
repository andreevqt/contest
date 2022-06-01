from dataclasses import field


def make_field(n, m, mines):
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)
    field = []
    for k in range(n + 2):
        field.append([0] * (m + 2))
    for x, y in mines:
        for k in range(len(dx)):
            field[x + dx[k]][y + dy[k]] += 1
    for x, y in mines:
        field[x][y] = '*'
    return field


n, m, k = map(int, input().split(" "))
mines = []
for i in range(k):
    mines.append(tuple(map(int, input().split())))
field = make_field(n, m, mines)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(field[i][j], end=' ')
    print()
