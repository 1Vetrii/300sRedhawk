alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
option = int(input())
if option == 1:
  table = []
  word = input()
  while word != "q":
    table.append(word)
    word = input()
  reversetable = table[::-1]
  tbs = ""
  for x in table:
    tbs += (x+" ")
  print(tbs.rstrip())
  tvt = ""
  for x in reversetable:
    tvt += (x+" ")
  print(tvt.rstrip())
  sentence = ""
  for x in table:
    sentence += (x + " ")
  insentence = list(set(sentence))
  insentence.remove(" ")
  isn = ""
  for x in sorted(insentence):
    isn += (x+" ")
  print(isn.rstrip())
  for x in insentence:
    if x in alphabet:
      alphabet.remove(x)
  abs = ""
  for x in sorted(alphabet):
    abs += (x+" ")
  print(abs.rstrip())

if option == 2:
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  sentencea = input()
  sentenceb = input()
  sentencec = input()
  sorteda = sorted(list(set(sentencea.lower())))
  sortedb = sorted(list(set(sentenceb.lower())))
  sortedc = sorted(list(set(sentencec.lower())))

  try:
    sorteda.remove(" ")
  except:
    pass
  try:
    sorteda.remove("!")
  except:
    pass
  try:
    sorteda.remove(".")
  except:
    pass
  try:
    sorteda.remove("?")
  except:
    pass
  try:
    sorteda.remove(":")
  except:
    pass
  try:
    sorteda.remove('"')
  except:
    pass
  try:
    sorteda.remove(",")
  except:
    pass
  try:
    sortedb.remove(" ")
  except:
    pass
  try:
    sortedb.remove("!")
  except:
    pass
  try:
    sortedb.remove(".")
  except:
    pass
  try:
    sortedb.remove("?")
  except:
    pass
  try:
    sortedb.remove(":")
  except:
    pass
  try:
    sortedb.remove('"')
  except:
    pass
  try:
    sortedb.remove(",")
  except:
    pass
  try:
    sortedc.remove(" ")
  except:
    pass
  try:
    sortedc.remove("!")
  except:
    pass
  try:
    sortedc.remove(".")
  except:
    pass
  try:
    sortedc.remove("?")
  except:
    pass
  try:
    sortedc.remove(":")
  except:
    pass
  try:
    sortedc.remove('"')
  except:
    pass
  try:
    sortedc.remove(",")
  except:
    pass


  print(sentencea)
  print(sentenceb)
  print(sentencec)
  sortedas = ""
  for x in sorteda:
    sortedas+=(x+" ")
  print(sortedas.rstrip())

  sortedbs = ""
  for x in sortedb:
    sortedbs+=(x+" ")
  print(sortedbs.rstrip())

  sortedcs = ""
  for x in sortedc:
    sortedcs+=(x+" ")
  print(sortedcs.rstrip())
  
  aandb = sorted(set(sorteda) | set(sortedb))
  aandbs = ""
  for x in sorted(aandb):
    aandbs+= (x+" ")
  print(aandbs.rstrip())
  
  bandc = sorted(set(sortedb) | set(sortedc))
  bandcs = ""
  for x in sorted(bandc):
    bandcs+= (x+" ")
  print(bandcs.rstrip())

  aandc = sorted(set(sorteda) | set(sortedc))
  aandcs = ""
  for x in sorted(aandc):
    aandcs+= (x+" ")
  print(aandcs.rstrip())
  
  aandbandc = sorted(set(sorteda) | set(sortedb) | set(sortedc))
  aandbandcs = ""
  for x in sorted(aandbandc):
    aandbandcs+= (x+" ")
  print(aandbandcs.rstrip())
  
  aorb = sorted(set(sorteda) & set(sortedb))
  aorbs = ""
  for x in sorted(aorb):
    aorbs+= (x+" ")
  print(aorbs.rstrip())

  
  borc = sorted(set(sortedb) & set(sortedc))
  borcs = ""
  for x in sorted(borc):
    borcs+= (x+" ")
  print(borcs.rstrip())
  
  aorc = sorted(set(sorteda) & set(sortedc))
  aorcs = ""
  for x in sorted(aorc):
    aorcs+= (x+" ")
  print(aorcs.rstrip())
  
  aorborc = sorted(set(sorteda) & set(sortedb) & set(sortedc))
  aorborcs = ""
  for x in sorted(aorborc):
    aorborcs+= (x+" ")
  print(aorborcs.rstrip())

  niab = ""
  for x in alphabet:
    if x not in sorteda and x not in sortedb and x not in sortedc:
      niab += (x+" ")
  print(niab.rstrip())