import random

chairParts = [
"leg A",
"leg B",
"leg C",
"leg D",
"seat",
"back",
"left arm",
"right arm",
]

tableParts = [
"leg A",
"leg B",
"leg C",
"leg D",
"support 1",
"support 2",
"tabletop section A",
"tabletop section B",
]

sofaParts = [
"base",
"body",
"back",
"left armrest",
"right armrest",
"cushion A",
"cushion B",
"cushion C",
]

hardware = [
"duct tape",
"screws",
"nails",
"bolts",
]

tools = [
"screwdriver",
"hammer",
"wrench",
  ]

directions = [
"upside down",
"on its side",
"90 degrees clockwise",
"90 degrees counterclockwise",
]

inputQuestions = [ 
"For CHAIR, type 0",
"For TABLE, type 1",
"For SOFA, type 2",
"If you don't want to build anything, type 3",
]

instructions = []

def main():
  printHeader()
  printInstructions()

def printHeader():
  print("What kind of furniture do you want to assemble?")

def printInstructions():
  while True:
    isChair = False
    isTable = False
    selection = int(getUserSelection())  
    if selection == 0:
  	  isChair = True
  	  generateInstructions(instructions, isChair, isTable)
    elif selection == 1:
  	  isTable = True
  	  generateInstructions(instructions, isChair, isTable)
    elif selection == 2:
      generateInstructions(instructions, isChair, isTable)
    elif selection == 3:
  	  print ("Okay, goodbye!")
  	  break
    else:
      print ("")
      print ("I'm sorry, that's not one of the options. Please type either 0, 1, 2, or 3. ")

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  return input("Type selection and press enter: ")

def generateInstructions(instructions, isChair, isTable):
  if isChair:
    x = "Chair"
  elif isTable:
    x = "Table"
  else:
    x = "Sofa"
  for i in range (0,2):
    for i in range (0,3):
  	  appendAttatchInstruction(instructions, isChair, isTable)
    appendTurnInstruction(instructions)
  for i in range (0,2):
  	appendAttatchInstruction(instructions, isChair, isTable)
  print ("")
  print (x + " Assembly Instructions:")
  for instruction in instructions:
    print (instruction)
  print ("")
  instructions [:] = []

def appendTurnInstruction(instructions):
  instructions.append("Turn assembly " + random.choice(directions) + ". ")

def appendAttatchInstruction(instructions, isChair, isTable):
  if isChair:
    x = chairParts
  elif isTable:
    x = tableParts
  else:
    x = sofaParts
  partsList = random.sample(x, 2)
  instructions.append("Attatch " + partsList[0] + " to " + partsList[1] + " with " + random.choice(hardware) + " and " + random.choice(tools) + ". ")

main()