import myFunc

x = myFunc.calcSum(1, 2)
print("1+2=", x)
if x != 3:
  print("Test Failed!")
  exit(1)
else:
  print("Test Passed!")
