def isIncreases(arr):
    prev = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] <= prev):
            return False
        prev = arr[i]
    return True

arr = list(map(int, input().split(" ")))

if isIncreases(arr):
    print("YES")
else:
    print("NO")
