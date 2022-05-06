from edx_io import edx_io


def insertion_sort(arr):
    res = list(range(1, len(arr) + 1))
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]
          j = j - 1
        res[i] = j + 2
    return res


with edx_io() as io:
    n = io.next_int()
    arr = []

    for i in range(0, n):
        arr.append(io.next_int())

    res = insertion_sort(arr)
    io.writeln(" ".join(str(x) for x in res))
    io.writeln(" ".join(str(x) for x in arr))
