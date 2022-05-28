a = int(input())
b = int(input())
c = int(input())

if a == 0 and b == c**2:
    print("MANY SOLUTIONS")
elif a == 0 or c < 0:
    print("NO SOLUTION")
else:
    x = (c**2 - b) / a
    if x.is_integer():
        print(int(x))
    else:
        print("NO SOLUTION")
