
def maxTime(a, n):
    return a * (n + 1) + n


def minTime(a, n):
    return a * (n - 1) + n


a = int(input())
b = int(input())
n = int(input())
m = int(input())

min1 = minTime(a, n)
max1 = maxTime(a, n)

min2 = minTime(b, m)
max2 = maxTime(b, m)

finalMin = max(min1, min2)
finalMax = min(max1, max2)

if finalMin <= finalMax:
  print("{} {}".format(max(min1, min2), min(max1, max2)))
else:
  print(-1)


