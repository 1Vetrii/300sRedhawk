option = int(input())

if option == 1:
  in1 = input()
  in2 = input()
  set1 = list(set(in1))
  set2 = list(set(in2))
  set1.remove(",")
  set2.remove(",")

  set1 = sorted(set1)
  set2 = sorted(set2)

  sset1 = ""
  sset2 = ""

  #convert to string
  for x in set1:
    sset1 = sset1 + x
    sset1 = sset1 + ","
  sset1 = sset1.strip(",")
  for x in set2:
    sset2 = sset2 + x
    sset2 = sset2 + ","
  sset2 = sset2.strip(",")

  
  print(f"Set A: {sset1}")
  print(f"Set B: {sset2}")

  union = []
  for x in set1:
    union.append(x)
  for x in set2:
    union.append(x)
  union = list(set(union))
  union = sorted(union)
  unions = ""
  for x in union:
    unions += x + ","
  unions = unions.strip(",")
  print(f"Union of sets: {unions}")
  inter = ""
  for x in sset1:
    if x in sset2:
      inter = inter + x
  for x in sset2:
    if x in sset1:
      inter = inter + x
  interset = list(set(inter))
  interset.remove(",")
  interset = sorted(interset)
  isstring = ""
  for x in interset:
    isstring = isstring + x
    isstring = isstring + ","
  isstring = isstring.strip(",")
  
  print(f"Intersection of sets: {isstring}")

  abstring = ""
  for x in sset1:
    if x not in sset2:
      abstring += x + ","
  abstring = abstring.strip(",")
  print(f"A-B: {abstring}")
  bastring = ""
  for x in sset2:
    if x not in sset1:
      bastring += x + ","
  bastring = bastring.strip(",")
  print(f"B-A: {bastring}")
  symdif = f"{abstring}" + "," if abstring != "" else ""
  print(f"Symmetric Difference: {symdif}{bastring}")

if option == 2:
  in1 = input()
  in2 = input()
  set1 = list(set(in1))
  set2 = list(set(in2))
  set1.remove(",")
  set2.remove(",")

  set1 = sorted(set1)
  set2 = sorted(set2)

  sset1 = ""
  sset2 = ""

  #convert to string
  for x in set1:
    sset1 = sset1 + x
    sset1 = sset1 + ","
  sset1 = sset1.strip(",")
  for x in set2:
    sset2 = sset2 + x
    sset2 = sset2 + ","
  sset2 = sset2.strip(",")

  setal = len(sset1.split(","))
  setbl = len(sset2.split(","))
  print(f"Set A: {setal}")
  print(f"Set B: {setbl}")

  union = []
  for x in set1:
    union.append(x)
  for x in set2:
    union.append(x)
  union = list(set(union))
  union = sorted(union)
  unions = ""
  for x in union:
    unions += x + ","
  unions = unions.strip(",")
  unionsl = len(unions.split(","))
  print(f"Union of sets: {unionsl}")
  inter = ""
  for x in sset1:
    if x in sset2:
      inter = inter + x
  for x in sset2:
    if x in sset1:
      inter = inter + x
  interset = list(set(inter))
  interset.remove(",")
  interset = sorted(interset)
  isstring = ""
  for x in interset:
    isstring = isstring + x
    isstring = isstring + ","
  isstring = isstring.strip(",")
  issl = len(isstring.split(","))
  print(f"Intersection of sets: {issl}")

  abstring = ""
  for x in sset1:
    if x not in sset2:
      abstring += x + ","
  abstring = abstring.strip(",")
  absl = len(abstring.split(","))
  print(f"A-B: {absl}")
  bastring = ""
  for x in sset2:
    if x not in sset1:
      bastring += x + ","
  bastring = bastring.strip(",")
  basl = len(bastring.split(","))
  print(f"B-A: {basl}")
  symdif = f"{abstring}" + "," if abstring != "" else ""
  sdl = len(f"{symdif}{bastring}".split(","))
  print(f"Symmetric Difference: {sdl}")