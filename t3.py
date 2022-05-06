from edx_io import edx_io

def insertion_sort(arr):
  res = [None] * len(arr)
  for i in range(1, len(arr)):
    j = i - 1
    while j >= 0 and arr[j + 1] < arr[j]: 
      tmp = arr[j + 1]
      arr[j + 1] = arr[j]
      arr[j] = tmp
      j = j - 1

    res[i] = j + 1
    
   
  return res
      

with edx_io() as io:
    n = io.next_int()
    list = []

    for i in range(0, n):
      list.append(io.next_int())

    res = insertion_sort(list)
    for i in range(0, len(list)):
      io.write("{} ".format(list[i]))

    io.writeln("")

    for i in range(0, len(res)):
      io.write("{} ".format(res[i]))
