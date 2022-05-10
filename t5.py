from edx_io import edx_io


def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = j = i - 1
        swap_idx = -1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap_idx = j + 1  
            print(swap_idx)          
            j = j - 1
        if swap_idx > -1 :
            print("Swap elements at indices {} and {}".format(k, swap_idx))


with edx_io() as io:
    n = io.next_int()
    arr = []

    for i in range(0, n):
        arr.append(io.next_int())

    insertion_sort(arr)
    print("Result is {}".format(arr))
    io.writeln(" ".join(str(x) for x in arr))

# 0 1 2 3 4
# 3 1 4 2 2

# 1 2 3 4 5
# 1 2 2 3 4
# 1 -> 2 2-> 4 3-> 5
""" Swap elements at indices 1 and 2.
Swap elements at indices 2 and 4.
Swap elements at indices 3 and 5.
No more swaps needed. """
