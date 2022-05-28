def extract_phone(str):
  str = str.replace("+", "")
  str = str.replace("-", "")
  str = str.replace("(", "")
  str = str.replace(")", "")
  code = "495"
  if len(str) == 11:
    code = str[1:4]
    number = str[4:]
  else:
    number = str
  return [code, number]

toFind = extract_phone(input())

for i in range(3):
  phone = extract_phone(input())
  if toFind[0] + toFind[1] == phone[0] + phone[1]:
    print("YES")
  else:
    print("NO")
