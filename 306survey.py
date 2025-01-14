option = int(input())
ver = int(input())

participants = []
popsi = []
kola = []
none = []

#Make Tables
with open(f"data/participants{ver}.txt") as infile:
  for x in infile:
    participants.append(x.strip("\n"))
with open(f"data/popsi{ver}.txt") as infile:
  for x in infile:
    popsi.append(x.strip("\n"))
with open(f"data/kola{ver}.txt") as infile:
  for x in infile:
    kola.append(x.strip("\n"))

#Set Variables
either = 0
both = 0
onlypopsi = 0
onlykola = 0
onlyone = 0
neither = 0

#Calculations (Using Counters)
for x in participants:
  if (x in popsi) or (x in kola):
    either += 1
  if (x in popsi) and (x in kola):
    both += 1
  if (x in popsi) and (x not in kola):
    onlypopsi += 1
  if (x in kola) and (x not in popsi):
    onlykola += 1
  if (x not in kola) and (x not in popsi):
    neither += 1
    none.append(int(x))
  onlyone = onlykola+onlypopsi
    
if option == 1:
  print(f"total: {len(participants)}\neither: {either}\nboth: {both}\nonly Popsi: {onlypopsi}\nonly Kola: {onlykola}\nonly one: {onlyone}\nneither: {neither}")
elif option == 2:
  for x in sorted(none):
    print(x)