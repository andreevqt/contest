def closest(seq, x):
    c = seq[0]
    for i in range(1, len(seq)):
        if abs(seq[i] - x) < abs(c - x):
            c = seq[i]
    return c


n = int(input())
seq = list(map(int, input().split(" ")))
x = int(input())

print(closest(seq, x))
