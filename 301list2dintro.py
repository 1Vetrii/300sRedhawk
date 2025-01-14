option = int(input())
if option == 1:
  list1 = [[0]*2 for x in range(3)]
 # list2 = [[0]*3 for x in range(2)]
  for y in range(3):
    for x in range(2):
      list1[y][x] = int(input())
  for i in range(3):
    for x in range(2):
      print(list1[i][x],end=" ")
    print()
  print(list1)

if option == 2:
  list1 = [[0]*2 for x in range(3)]
 # list2 = [[0]*3 for x in range(2)]
  for y in range(3):
    for x in range(2):
      list1[y][x] = int(input())
  scalar = int(input())
  list2 = []
  for x in list1:
    list2.append(x[:])
  for x in range(3):
    for i in range(2):
      list2[x][i] = int(list2[x][i])*scalar

  for i in range(3):
    for x in range(2):
      print(list1[i][x],end=" ")
    print()
  print("*****")
  for i in range(3):
    for x in range(2):
      print(list2[i][x],end=" ")
    print()
  print(list1)
  print(list2)

if option == 3:
  list1 = [[0]*2 for x in range(3)]
  list2 = [[0]*2 for x in range(3)]
  list3 = [[0]*2 for x in range(3)]
  for y in range(3):
    for x in range(2):
      a = int(input())
      list1[y][x] = a
  for y in range(3):
    for x in range(2):
      a = int(input())
      list2[y][x] = a
  for y in range(3):
    for x in range(2):
      list3[y][x] = list1[y][x] + list2[y][x]
  
  for i in range(3):
    for x in range(2):
      print(list1[i][x],end=" ")
    print()
  print("*****")
  for i in range(3):
    for x in range(2):
      print(list2[i][x],end=" ")
    print()
  print("*****")
  for i in range(3):
    for x in range(2):
      print(list3[i][x],end=" ")
    print()
  print(list1)
  print(list2)
  print(list3)

if option == 4:
  list1 = [[0]*2 for x in range(3)]
  list2 = [[0]*3 for x in range(2)]
  for y in range(3):
    for x in range(2):
      list1[y][x] = int(input())
  for x in range(2):
    for y in range(3):
      list2[x][y] = list1[y][x]

  for i in range(3):
    for x in range(2):
      print(list1[i][x],end=" ")
    print()
  print("*****")
  for i in range(2):
    for x in range(3):
      print(list2[i][x],end=" ")
    print()
  print(list1)
  print(list2)

if option == 5:
  list1 = [[0]*3 for x in range(3)]
  for y in range(3):
    for x in range(3):
      list1[y][x] = int(input())

  symm = False
  symcount = 0
  for i in range(3):
    for x in range(3):
      print(list1[i][x],end=" ")
    print()
  for y in range(3):
    for x in range(3):
      if list1[y][x] == list1[x][y] and y != x:
        symm = True
        symcount += 1
  print("Symmetrical" if symm and symcount == 6 else "Not Symmetrical")
  print(list1)
      