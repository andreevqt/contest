def determine_highest(seq):
    top = max(seq)

    maximum = 0
    pos = 0
    for i in range(1, len(seq) - 1):
        if seq[i] % 10 == 5 and seq[i + 1] < seq[i] and seq[i] > maximum:
            pos = 1
            for j in range(i):
                if seq[j] > seq[i]:
                    pos = pos + 1
                if seq[j] == top:
                    maximum = seq[i]
                    break

    if maximum == 0:
        return 0

    if pos:
        return pos

    return 1

    for i in range(len(top)):
        if top[i] == maximum:
            return i + 1


""" n = int(input())
seq = list(map(int, input().split(" ")))
print(determine_highest(seq)) """


res = determine_highest([10, 20, 15, 10, 30, 5, 1])
print(res)

res = determine_highest([15, 15, 10])
print(res)

res = determine_highest([10, 15, 20])
print(res)

res = determine_highest([30, 5, 15, 1])
print(res)

res = determine_highest([30, 5, 5, 15, 1])
print(res)
