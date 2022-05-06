from edx_io import edx_io


def sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1][0] < arr[j][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j = j - 1


with edx_io() as io:
    n = io.next_int()
    arr = []

    for i in range(1, n + 1):
        arr.append([io.next_float(), i])

    sort(arr)

    l = arr[0]
    m = arr[len(arr) // 2]
    r = arr[len(arr) - 1]

    io.writeln(l[1])
    io.writeln(m[1])
    io.writeln(r[1])
