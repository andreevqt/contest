def solution(seq):
    max1, max2, *rest = sorted(seq[:2], reverse=True)
    min1, min2 = max2, max1
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
        elif seq[i] < min1:
            min2 = min1
            min1 = seq[i]
        elif seq[i] < min2:
            min2 = seq[i]

    return (max1, max2, min1, min2)


seq = list(map(int, input().split()))
max1, max2, min1, min2 = solution(seq)
if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)
