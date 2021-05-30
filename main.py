import string
import numpy as np
import random

# class for grid element
class GridElement:
    def __init__(self, number, locationType, edges, heuristic):
        self.number = number
        self.locationType = locationType
        self.edges = edges
        self.heuristic = heuristic

    def printElement(self):
        print("Cell Number:" + str(self.number) + "\n" +
              "Location Type:" + self.locationType + "\n" +
              "Cell Edges:" + str(self.edges))

    def getNumber(self):
        return str(self.number)

    def getLocationType(self):
        return self.locationType

def createGridElement(number, edges):
    locationChoices = ["Q", "V", "P", "E"]
    # Q for quarantine, V for vaccine, P for playground, E for empty
    locationType = random.choice(locationChoices)  # chooses random location type
    element = GridElement(number, locationType, edges, "0")
    return element

print("\n======================================================================")
#############   STEP 1 -- User inputs to make map
print("Program Begins:")
userRows = int(input("\nEnter amount of Rows? "))
userColumns = int(input("Enter amount of Columns? "))

print("========================================================================")
#############   STEP 2 -- List all items in list with theyre appropriate edges
print("Information of each cell:\n")
edges = (list(string.ascii_letters))  # list of alphabetical edges (lowercase then uppercase)
gridSize = userRows * userColumns
l = 0
k = 4
gridList = []
for i in range(1, gridSize + 1):  # iterate over all items in grid
    #gridList = []
    e = createGridElement(i, edges[l:k])
    gridList.append(e)
    e.printElement()
    print("_________________________")
    l = l + 4  # increment to next 4 edge elements
    k = k + 4

print("=========================================================================")
#############   STEP 3 -- Visual of map locations
print("Generated Map:\n")
genMap = []
for i in range(0, len(gridList)):
    genMap.append(gridList[i].locationType)

counter = 0
for j in range(0,len(gridList)):
    print("| ", genMap[j], " |", end= '')
    counter += 1
    if(counter == userColumns):
        print(" ")
        counter =0

print("\n=======================================================================")
#############   STEP 4 --  User choosing the Role C or Role V and inputs start state
print("Role C (Covid Patients)\nRole V (People Getting Vaccinated)\n")
role = (input("Choose the Role C or the Role V: "))

if(role == 'c' or role == 'C'):
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if(startCell <= gridSize):
        print("You have selected the start state to be: ", genMap[startCell-1])
    else:
        startCell = int(input("Number out of range of grid: Enter the number of the cell that is the starting point/state: "))
    goalCell = 'Q'
elif(role == 'v' or role == 'V'):
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if(startCell <= gridSize):
        print("You have selected the start state to be: ", genMap[startCell-1])
    else:
        startCell = int(input("Number out of range of grid: Enter the number of the cell that is the starting point/state: "))
    goalCell = 'V'
else:
    print("Choose C or V")
    role = string(input("Choose the Role C or the Role V:"))

print("\nStarting State: ", genMap[startCell-1],"(Cell: ",startCell,")" "  ------->  Goal State: ", goalCell)

print("\n=========================================================================")
#############   STEP 5 -- Heuristic and A* Algorithms


