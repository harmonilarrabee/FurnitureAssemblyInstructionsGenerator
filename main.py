import random

import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

engine = create_engine('sqlite:///mydb.db', echo=True)

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
"To retrieve previoulsy generated instructions, type 3",
"If you don't want to build or retrieve anything, type 4",
]

instructions = []

def main():
  userName = str(getUserName())
  while True:
  	printHeader()
  	isChair = False
  	isTable = False
  	selection = int(getUserSelection())
  	while not selection in range(0, 5):
  	  selection = int(errorMessage())
  	if selection == 0:
  	  isChair = True
  	  printInstructions(instructions, isChair, isTable, userName)
  	elif selection == 1:
  	  isTable = True
  	  printInstructions(instructions, isChair, isTable, userName)
  	elif selection == 2:
  	  printInstructions(instructions, isChair, isTable, userName)
  	elif selection == 3:
  	  #retrieveInstructions()
  	  print ("")
  	  print ("Sorry, this function is still in progress. PLease try again later.")
  	  print("")
  	elif selection == 4:
  	  sayGoodbye()
  	  break

def printHeader():
  print ("What kind of furniture do you want to assemble?")

def getUserName():
  return input("Hello! Please type your name and press enter: ")

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  print (inputQuestions[4])
  return input("Type selection and press enter: ")

def printInstructions(instructions, isChair, isTable, userName):
  if isChair:
    furnitureType = "Chair"
  elif isTable:
    furnitureType = "Table"
  else:
    furnitureType = "Sofa"
  for i in range (0,2):
    for i in range (0,3):
  	  generateAttatchInstruction(instructions, isChair, isTable)
    generateTurnInstruction(instructions)
  for i in range (0,2):
  	generateAttatchInstruction(instructions, isChair, isTable)
  print ("")
  print (userName + "'s " + furnitureType + " Assembly Instructions:")
  for instruction in instructions:
    print (instruction)
  print ("")
  #saveToDatabase(instructions, userName, furnitureType)
  instructions [:] = []

def generateTurnInstruction(instructions):
  instructions.append("Turn assembly " + random.choice(directions) + ". ")

def generateAttatchInstruction(instructions, isChair, isTable):
  if isChair:
    x = chairParts
  elif isTable:
    x = tableParts
  else:
    x = sofaParts
  partsList = random.sample(x, 2)
  instructions.append("Attatch " + partsList[0] + " to " + partsList[1] + " with " + random.choice(hardware) + " and " + random.choice(tools) + ". ")

def errorMessage():
  print ("")
  return input("I'm sorry, that's not one of the options. Please type either 0, 1, 2, or 3: ")
  print ("")

def sayGoodbye():
  print ("")
  print ("Okay, goodbye!")

def saveToDatabase(instructions, userName, furnitureType):
  conn = engine.connect()
  metadata = MetaData()
  createTable(metadata, conn)
  statement = text("INSERT INTO instructions ('name', 'furnitureType', 'instructionOne', 'instructionTwo', 'instructionThree', 'instructionFour', 'instructionFive', 'instructionSix', 'instructionSeven', 'instructionEight', 'instructionNine', 'instructionTen')"
  " values (str(" + userName + "), str(" + furnitureType + "), str(" + instructions[0] + "), str(" + instructions[1] + "), str(" + instructions[2] + "), str(" + instructions[3] + "), str(" + instructions[4] + "), str(" + instructions[5] + "), str(" + instructions[6] + "), str(" + instructions[7] + "), str(" + instructions[8] + "), str(" + instructions[9] + ")")
  conn.execute(statement)

def retrieveInstructions():
  query = text("SELECT * from instructions")
  result = conn.execute(query).fetchall()
  print(result)

def createTable(metadata, conn):
  instructions = Table('instructions', metadata,
    Column('userName', String, primary_key=True),
    Column('furnitureType', String),
    Column('instructionOne', String),
    Column('instructionTwo', String),
    Column('instructionThree', String),
    Column('instructionFour', String),
    Column('instructionFive', String),
    Column('instructionSix', String),
    Column('instructionSeven', String),
    Column('instructionEight', String),
    Column('instructionNine', String),
    Column('instructionTen', String))
  metadata.create_all(engine)


main()