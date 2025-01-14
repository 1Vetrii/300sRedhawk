import math
option = int(input())
first = input()

if option == 1:
  num1 = float(first)
  num2 = float(input())
  try:
    ans = num1/num2
    print(ans)
  except:
    print("Second number must be non-zero")
elif option == 2:
  try:
    sqrt = math.sqrt(int(first))
    print(f"{sqrt:.1f}")
  except:
    print("Number must be positive")
elif option == 3:
  place = int(input())
  try:
    print(first[place-1])
  except:
    print("There is no letter at that position in the word")
elif option == 4:
  try:
    with open(f"data/{first}") as infile:
      for x in infile:
        print(x)
  except:
    print("File does not exist")