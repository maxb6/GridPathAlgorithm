import string
import numpy as np
import random


# class for grid element
class GridElement:
    def __init__(self, number, locationType, neighbours, heuristic):
        self.number = number
        self.locationType = locationType
        self.neighbours = neighbours
        self.heuristic = heuristic

    def printElement(self):
        print("Cell Number:" + str(self.number) + "\n" +
              "Location Type:" + self.locationType + "\n" +
              "Cell Neighbours:" + str(self.neighbours))

    def getNumber(self):
        return str(self.number)

    def getLocationType(self):
        return self.locationType


def createGridElement(number, neighbours):
    locationChoices = ["Q", "V", "P", "E"]
    # Q for quarantine, V for vaccine, P for playground, E for empty
    locationType = random.choice(locationChoices)  # chooses random location type
    element = GridElement(number, locationType, neighbours, "0")
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
    if gridList[i].locationType == "E":
        genMap.append(gridList[i].number)
    else:
        genMap.append(gridList[i].locationType)

counter = 0
for j in range(0, len(gridList)):
    print("| ", genMap[j], " |", end='')
    counter += 1
    if counter == userColumns:
        print(" ")
        counter = 0

print("\n=======================================================================")
#############   STEP 4 --  User choosing the Role C or Role V and inputs start state
print("Role C (Covid Patients)\nRole V (People Getting Vaccinated)\n")
role = (input("Choose the Role C or the Role V: "))

if (role == 'c' or role == 'C'):
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if (startCell <= gridSize):
        print("You have selected the start state to be: ", genMap[startCell - 1])
    else:
        startCell = int(
            input("Number out of range of grid: Enter the number of the cell that is the starting point/state: "))
    goalCell = 'Q'
elif (role == 'v' or role == 'V'):
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if (startCell <= gridSize):
        print("You have selected the start state to be: ", genMap[startCell - 1])
    else:
        startCell = int(
            input("Number out of range of grid: Enter the number of the cell that is the starting point/state: "))
    goalCell = 'V'
else:
    print("Choose C or V")
    role = string(input("Choose the Role C or the Role V:"))

print("\nStarting State: ", genMap[startCell - 1], "(Cell: ", startCell, ")" "  ------->  Goal State: ", goalCell)

print("\n=========================================================================")

#############   STEP 5 -- Cost

# if role c
for i in range(0, len(gridList)):
    try:
        if gridList[i].number == gridSize:
            gridList[i].neighbours = [gridList[i - 1].locationType, gridList[i - userColumns].locationType,
                                      "0", "0"]
        elif gridList[i].number > gridSize - userColumns:
            gridList[i].neighbours = [gridList[i - 1].locationType, gridList[i - userColumns].locationType,
                                      gridList[i + 1].locationType, "0"]
        else:
            gridList[i].neighbours = [gridList[i - 1].locationType, gridList[i - userColumns].locationType,
                                      gridList[i + 1].locationType, gridList[i + userColumns].locationType]
    except IndexError:
        print("No neighbour for element: " + str(gridList[i].number))

for i in range(0, len(gridList)):
    # check if there are no left neighbours
    if gridList[i].number % userColumns == 1:
        gridList[i].neighbours[0] = "0"
    # check if there are no upper neighbours
    if gridList[i].number <= userColumns:
        gridList[i].neighbours[1] = "0"
    # check if there are no right neighbours
    if gridList[i].number % userColumns == 0:
        gridList[i].neighbours[2] = "0"
    # check if there are no bottom neighbours
    if gridList[i].number > gridSize - userColumns:
        gridList[i].neighbours[3] = "0"

    gridList[i].printElement()

#############   STEP 5 -- Heuristic and A* Algorithms
