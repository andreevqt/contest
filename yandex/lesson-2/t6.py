def find_min(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while i < len(seq) and j >= 0 and seq[i] == seq[j] and i <= j:
            i = i + 1
            j = j - 1
        if i > j:
            return seq[:start][::-1]


n = int(input())
seq = list(map(int, input().split()))

res = find_min(seq)
print(len(res))
print(*res)
