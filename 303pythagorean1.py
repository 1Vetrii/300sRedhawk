from math import sqrt
num1 = int(input())
num2 = int(input())

if num1 >=0 and num2 >=0:
  hyp = round(sqrt(float(num1**2)+float(num2**2)),1)
  print(f"The hypotenuse is {hyp}")
else:
  print("Both numbers must be positive")