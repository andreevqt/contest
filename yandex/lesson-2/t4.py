def determine_elements(seq):
  count = 0
  for i in range(1, len(seq) - 1):
    if (seq[i] > seq[i - 1] and seq[i] > seq[i + 1]):
      count = count + 1
  return count

seq = list(map(int, input().split(" ")))
print(determine_elements(seq))
