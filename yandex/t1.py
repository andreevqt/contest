troom, tcond = list(map(int, input().split(" ")))
mode = input()

if mode == "freeze":
  print(troom if troom <= tcond  else tcond)
elif mode == "heat":
  print(troom if troom >= tcond  else tcond)
elif mode == "fan":
  print(troom)
elif mode == "auto":
  print(tcond)
