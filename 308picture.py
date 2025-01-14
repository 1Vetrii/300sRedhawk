option = int(input())

if option == 1:
  r = int(input())
  c = int(input())
  picture = [[" "]*c for x in range(r)]
  pairs = int(input())
  for x in range(pairs):
    pair = input().split(",")
    picture[(int(pair[0])-1)][(int(pair[1])-1)] = "*"

  print(picture)
    
  for y in range(r):
    for x in range(c):
      print(picture[y][x],end="")
    print()


if option == 2:
  r = int(input())
  c = int(input())
  count = 0
  picture = [[' ']*c for x in range(r)]
  pairs = []
  for x in range(r):
    stars = input()
    for i in range(c):
      if stars[i] == "*":
        count += 1
        picture[x][i] = "*"
        pairs.append(f"{x+1},{i+1}")
  print(count)
  print(picture)
  for x in pairs:
    print(x)

if option == 3:
  with open(f"data/{input()}.txt") as infile:
    c=0
    r=0
    picture = []
    pairs = 0
    for line,text in enumerate(infile):
      if line == 0:
        r = int(text)
      if line==1:
        c=int(text)
      if line == 2:
        picture = [[" "]*c for x in range(r)]
        pairs = int(text)
      if line > 2:
        pair = text.split(",")
        picture[(int(pair[0])-1)][(int(pair[1])-1)] = "*"
    for y in range(r):
      for x in range(c):
        print(picture[y][x],end="")
      print()

if option == 4:
  with open(f"data/{input()}.txt") as infile:
    c=0
    r=0
    picture = []
    pairs = 0
    for line,text in enumerate(infile):
      if line == 0:
        r = int(text)
      if line==1:
        c=int(text)
      if line == 2:
        picture = [[" "]*c for x in range(r)]
        pairs = int(text)
      if line > 2:
        pair = text.split(",")
        picture[(int(pair[0])-1)][(int(pair[1])-1)] = pair[2].strip()
    for y in range(r):
      for x in range(c):
        print(picture[y][x],end="")
      print()