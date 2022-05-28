
def sort(a, b):
    if a < b:
        return (a, b)
    return (b, a)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b = sort(a, b)
b, c = sort(b, c)
# a - min, e - max
a, b = sort(a, b)
# d - min, e - max
d, e = sort(d, e)
if a <= d and b <= e:
    print("YES")
else:
    print("NO")
