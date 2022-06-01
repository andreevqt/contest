def solution(seq):
    max1, max2, max3, *rest = sorted(seq[:3], reverse=True)
    min1, min2 = max3, max2
    for i in range(3, len(seq)):
        if seq[i] > max1:
            max3 = max2
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max3 = max2
            max2 = seq[i]
        elif seq[i] > max3:
            max3 = seq[i]
        elif seq[i] < min1:
            min2 = min1
            min1 = seq[i]
        elif seq[i] < min2:
            min2 = seq[i]
    return (max1, max2, max3, min1, min2)


seq = list(map(int, input().split()))
max1, max2, max3, min1, min2 = solution(seq)
if max1 * max2 * max3 > min1 * min2 * max1:
    print(max1, max2, max3)
else:
    print(min1, min2, max1)
