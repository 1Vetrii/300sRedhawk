option = int(input())
if option == 1:
  board = [[0]*3 for x in range(3)]
  for y in range(3):
    for x in range(3):
      board[y][x] = input()

  #Print Board x,y
  s = False
  for y in range(3):
    if s:
      print()
    for x in range(3):
      print(board[y][x],end="")
      s = True
      if x == 2 and y == 2:
        print()
        
  print(board)

if option == 2:
  win = False
  board = [[0]*3 for x in range(3)]
  for y in range(3):
    for x in range(3):
      board[y][x] = input()
  #Print Board x,y
  s = False
  for y in range(3):
    if s:
      print()
    for x in range(3):
      print(board[y][x],end="")
      s = True
      if x == 2 and y == 2:
        print()

  #determine winner
  for x in range(3):
    if board[0][x] == board[1][x] == board[2][x]:
      win = True
      print(f"{board[0][x]} wins")
      print(f"Column {x+1}")
  if board[0][0] == board[1][1] == board[2][2]:
    win = True
    print(f"{board[0][0]} wins")
    print(f"Diagonal 1")
  if board[0][2] == board[1][1] == board[2][0]:
    win = True
    print(f"{board[0][2]} wins")
    print(f"Diagonal 2")
  if not win:
    print("No Winner")
  print(board)

if option == 3:
  board = [["b"]*3 for _ in range(3)]
  pos = ""
  x = True
  o = False
  while pos != "Q":
    pos = input()
    if pos == "TL":
      board[0][0] = "x" if x else "o"
    elif pos == "TM":
      board[0][1] = "x" if x else "o"
    elif pos == "TR":
      board[0][2] = "x" if x else "o"
    elif pos == "ML":
      board[1][0] = "x" if x else "o"
    elif pos == "MM":
      board[1][1] = "x" if x else "o"
    elif pos == "MR":
      board[1][2] = "x" if x else "o"
    elif pos == "BL":
      board[2][0] = "x" if x else "o"
    elif pos == "BM":
      board[2][1] = "x" if x else "o"
    elif pos == "BR":
      board[2][2] = "x" if x else "o"
    if x and not o:
      x = False
      o = True
    elif o and not x:
      x = True
      o = False
  #Print Board x,y
  s = False
  for y in range(3):
    if s:
      print()
    for x in range(3):
      print(board[y][x],end="")
      s = True
      if x == 2 and y == 2:
        print()
  print(board)

if option == 4:
  c=1
  win = False
  board = [["b"]*3 for _ in range(3)]
  pos = ""
  xb = True
  ob = False
  while not win:
    pos = input()
    if pos == "TL":
      board[0][0] = "x" if xb else "o"
    elif pos == "TM":
      board[0][1] = "x" if xb else "o"
    elif pos == "TR":
      board[0][2] = "x" if xb else "o"
    elif pos == "ML":
      board[1][0] = "x" if xb else "o"
    elif pos == "MM":
      board[1][1] = "x" if xb else "o"
    elif pos == "MR":
      board[1][2] = "x" if xb else "o"
    elif pos == "BL":
      board[2][0] = "x" if xb else "o"
    elif pos == "BM":
      board[2][1] = "x" if xb else "o"
    elif pos == "BR":
      board[2][2] = "x" if xb else "o"
    if xb and not ob:
      xb = False
      ob = True
    elif ob and not xb:
      xb = True
      ob = False


    #determine winner
    for x in range(3):
      if board[0][x] == board[1][x] == board[2][x] and board [0][x] != "b":
        win = True
        #Print Board x,y
        s = False
        for y in range(3):
          if s:
            print()
          for h in range(3):
            print(board[y][h],end="")
            s = True
            if h == 2 and y == 2:
              print()
        print(f"{board[0][x]} wins")
        print(f"Column {x+1}")
    if board[0][0] == board[1][1] == board[2][2] and board [0][0] != "b":
      win = True
      #Print Board x,y
      s = False
      for y in range(3):
        if s:
          print()
        for x in range(3):
          print(board[y][x],end="")
          s = True
          if x == 2 and y == 2:
            print()
      print(f"{board[0][0]} wins")
      print(f"Diagonal 1")
    if board[0][2] == board[1][1] == board[2][0] and board [0][2] != "b":
      win = True
      #Print Board x,y
      s = False
      for y in range(3):
        if s:
          print()
        for x in range(3):
          print(board[y][x],end="")
          s = True
          if x == 2 and y == 2:
            print()
      print(f"{board[0][2]} wins")
      print(f"Diagonal 2")
    c += 1
    if c == 10 and not win:
      win = True
      #Print Board x,y
      s = False
      for y in range(3):
        if s:
          print()
        for x in range(3):
          print(board[y][x],end="")
          s = True
          if x == 2 and y == 2:
            print()
      print("No Winner")

  print(board)