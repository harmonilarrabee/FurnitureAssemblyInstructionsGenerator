import random

def main():
  instructions = [
  "Attatch left side of chair leg C to tabletop with screwdriver. ",
  "Turn asssembly upside down. ",
  "Place seat of chair on right sofa arm and duct tape in place. ",
  "Attatch table leg A to chair back, using hammer and screws. ",
  "Use screwdriver and nails to attatch table leg B to sofa cushion. ",
  "Attatch right side of table leg A to section G of sofa frame with nails. ",
  "Turn asssembly 90 degrees clockwise. ",
  "Place chair back on left sofa arm and solder in place. ",
  "Attatch chair leg D to main table support, using wrench to apply duct tape. ",
  "Use hammer and screws to attatch sofa base to chair arm. ",
  ]

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printChairAssemblyInstructions(instructions)
  elif selection == 1:
    printTableAssemblyInstructions(instructions)
  elif selection == 2:
    printSofaAssemblyInstructions(instructions)
  else:
    print ("SELECTION NOT RECOGNIZED")

inputQuestions = [ 
  "For CHAIR, type 0",
  "For TABLE, type 1",
  "For SOFA, type 2",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  return input("Type selection and press enter: ")

def printHeader():
  print("Furniture Assembly Instructions")

def printChairAssemblyInstructions(instructions):
  print("Chair Assembly Instructions:")
  for i in range(0,5):
    print (random.choice(instructions))

def printTableAssemblyInstructions(instructions):
  print("Table Assembly Instructions:")
  for i in range(0,5):
    print (random.choice(instructions))

def printSofaAssemblyInstructions(instructions):
  print("Sofa Assembly Instructions:")
  for i in range(0,5):
    print (random.choice(instructions))

main()
