import math
import string
import numpy as np
import random
from queue import PriorityQueue

from numpy.core.fromnumeric import size


# class for grid element

class GridElement:
    def __init__(self, number, locationType, edges, neighbours, cost, heuristic):
        self.number = number
        self.locationType = locationType
        self.edges = edges
        self.neighbours = neighbours
        self.cost = cost
        self.heuristic = heuristic

    def printElement(self):
        print("Cell Number:" + str(self.number) + "\n" +
              "Location Type:" + self.locationType + "\n" +
              "Nodes:" + str(self.edges) + "\n" +
              "Cell Neighbours:" + str(self.neighbours) + "\n" +
              "Edge Costs:" + str(self.cost) + "\n" +
              "Heuristic Amount:" + str(self.heuristic))

    def getNumber(self):
        return str(self.number)

    def getLocationType(self):
        return self.locationType


def createGridElement(number):
    locationChoices = ["Q", "V", "P", "E"]
    # Q for quarantine, V for vaccine, P for playground, E for empty
    locationType = random.choice(locationChoices)  # chooses random location type
    element = GridElement(number, locationType, [], [], [], "0")
    return element


print("\n======================================================================")
#############   STEP 1 -- User inputs to make map
print("Program Begins:")
userRows = int(input("\nEnter amount of Rows? "))
userColumns = int(input("Enter amount of Columns? "))

print("========================================================================")
#############   STEP 2 -- List all items in list with theyre appropriate edges
print("Information of each cell:\n")
gridSize = userRows * userColumns
l = 0
k = 4
gridList = []
for i in range(1, gridSize + 1):  # iterate over all items in grid
    e = createGridElement(i)
    gridList.append(e)
    '''
    e.printElement()
    print("_________________________")
    '''

print("=========================================================================")
#############   STEP 3 -- Visual of map locations
print("Generated Map:\n")
genMap = []
for i in range(0, len(gridList)):
    if gridList[i].locationType == "E":
        genMap.append(gridList[i].number)
    else:
        genMap.append(gridList[i].locationType)
########### Create edges for each grid element
for i in range(0, len(gridList)):
    if gridList[i].locationType == "E":
        genMap.append(gridList[i].number)
    else:
        genMap.append(gridList[i].locationType)

edgeList = (list(string.ascii_letters))  # list of alphabetical edges (lowercase then uppercase)

rc = 0
for i in range(0, len(gridList)):
    if gridList[i].number % userColumns == 1 and gridList[i].number != 1:
        gridList[i].edges = [edgeList[rc + 1], edgeList[rc + 2], edgeList[rc + userColumns + 2],
                             edgeList[rc + userColumns + 3]]
        rc += 2
    else:
        gridList[i].edges = [edgeList[rc], edgeList[rc + 1], edgeList[rc + userColumns + 1],
                             edgeList[rc + userColumns + 2]]
        rc += 1

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
role = (input("Choose the Role C or the Role V by entering C or V: "))

cellWidth = 0.1
cellLength = 0.2

gridWidth = cellWidth * userColumns
gridLength = cellLength * userRows


def startElement(rows, columns):
    startCell = (rows * 2 + columns)
    return gridList[startCell].locationType


if role == 'c' or role == 'C':
    startCellxInput = float(input("\nEnter an x coordinate as the starting point/state (Choose between 0 and " + str(
        round(gridWidth, 2)) + "): "))
    startCellyInput = float(input(
        "Enter a y coordinate as the starting point/state (Choose between 0 and " + str(round(gridLength, 2)) + "): "))

    startRow = (math.floor(startCellyInput / cellLength)) + 1
    print("Start state is in row: " + str(startRow))
    startColumn = (math.floor(startCellxInput / cellWidth)) + 1
    print("Start state is in column: " + str(startColumn))

    print(startElement(startRow, startColumn))

    startX = round((startColumn * 0.1), 2)
    startY = round(((startRow - 1) * 0.2), 2)

    print("Start Cell Coordinates: " + str(startX) + "," + str(startY))

    goalStateList = []
    goalXList = []
    goalYList = []
    distanceList = []
    for j in range(0, len(gridList)):
        if "Q" in gridList[j].locationType:
            goalStateList.append(gridList[j].number)

    for i in range(0, len(goalStateList)):
        goalStateRow = math.ceil(goalStateList[i] / userRows)
        goalStateColumn = goalStateList[i] % userColumns
        if goalStateColumn == 0:
            goalStateColumn = userColumns
        goalYList.append((goalStateRow - 1) * 0.2)
        goalXList.append(goalStateColumn * 0.1)

    for i in range(0, len(goalStateList)):
        distanceList.append(
            math.sqrt((abs((goalXList[i] - startX)) ** 2) + (abs((goalYList[i] - startY)) ** 2)))

    for p in range(0, len(distanceList)):
        goalDistanceIndex = distanceList.index(min(distanceList))

    goalState = goalStateList[goalDistanceIndex]
    print("Goal State Cell Number: " + str(goalState))
    goalStateX = goalXList[goalDistanceIndex]
    goalStateY = goalYList[goalDistanceIndex]

if role == 'v' or role == 'V':
    startCellx = float(input("\nEnter an x coordinate as the starting point/state (Choose between 0 and " + str(
        round(gridWidth, 2)) + "): "))
    startCelly = float(input(
        "Enter a y coordinate as the starting point/state (Choose between 0 and " + str(round(gridLength, 2)) + "): "))

    startRow = math.floor(startCelly / cellLength)
    print("Start state is in row: " + str(startRow + 1))
    startColumn = math.floor(startCellx / cellWidth)
    print("Start state is in column: " + str(startColumn + 1))

# print("\nStarting State: ", genMap[startCell - 1], "(Cell: ", startCell, ")" "  ------->  Goal State: ", goalCell)

#############   STEP 5 -- Cost

# find neighbours for each gridElement
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

    # gridList[i].printElement()

# find cost for each grid Element dependent on what role is chosen
# fill cost list with -1s as default
for i in range(0, len(gridList)):
    gridList[i].cost = [-1, -1, -1, -1]
# for role c: cost = (left,top,right,bottom)
for i in range(0, len(gridList)):
    # if there are no neighbours on the left
    if gridList[i].neighbours[0] == "0":
        if gridList[i].locationType == "Q":
            gridList[i].cost[0] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[0] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[0] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[0] = 3
    # if there are no neighbours on the top
    if gridList[i].neighbours[1] == "0":
        if gridList[i].locationType == "Q":
            gridList[i].cost[1] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[1] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[1] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[1] = 3
    # if there are no neighbours on the right
    if gridList[i].neighbours[2] == "0":
        if gridList[i].locationType == "Q":
            gridList[i].cost[2] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[2] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[2] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[2] = 3
    # if there are no neighbours on the bottom
    if gridList[i].neighbours[3] == "0":
        if gridList[i].locationType == "Q":
            gridList[i].cost[3] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[3] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[3] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[3] = 3
    ######### if there is a neighbour that is a quarantine place
    if gridList[i].neighbours[0] == "Q":
        if gridList[i].locationType == "Q":
            gridList[i].cost[0] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[0] = 0.5
        if gridList[i].locationType == "V":
            gridList[i].cost[0] = 1
        if gridList[i].locationType == "P":
            gridList[i].cost[0] = 1.5
    if gridList[i].neighbours[1] == "Q":
        if gridList[i].locationType == "Q":
            gridList[i].cost[1] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[1] = 0.5
        if gridList[i].locationType == "V":
            gridList[i].cost[1] = 1
        if gridList[i].locationType == "P":
            gridList[i].cost[1] = 1.5
    if gridList[i].neighbours[2] == "Q":
        if gridList[i].locationType == "Q":
            gridList[i].cost[2] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[2] = 0.5
        if gridList[i].locationType == "V":
            gridList[i].cost[2] = 1
        if gridList[i].locationType == "P":
            gridList[i].cost[2] = 1.5
    if gridList[i].neighbours[3] == "Q":
        if gridList[i].locationType == "Q":
            gridList[i].cost[3] = 0
        if gridList[i].locationType == "E":
            gridList[i].cost[3] = 0.5
        if gridList[i].locationType == "V":
            gridList[i].cost[3] = 1
        if gridList[i].locationType == "P":
            gridList[i].cost[3] = 1.5

    ############## if there is a neighbour that is a vaccine place
    if gridList[i].neighbours[0] == "V":
        if gridList[i].locationType == "Q":
            gridList[i].cost[0] = 1
        if gridList[i].locationType == "E":
            gridList[i].cost[0] = 1.5
        if gridList[i].locationType == "V":
            gridList[i].cost[0] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[0] = 2.5
    if gridList[i].neighbours[1] == "V":
        if gridList[i].locationType == "Q":
            gridList[i].cost[1] = 1
        if gridList[i].locationType == "E":
            gridList[i].cost[1] = 1.5
        if gridList[i].locationType == "V":
            gridList[i].cost[1] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[1] = 2.5
    if gridList[i].neighbours[2] == "V":
        if gridList[i].locationType == "Q":
            gridList[i].cost[2] = 1
        if gridList[i].locationType == "E":
            gridList[i].cost[2] = 1.5
        if gridList[i].locationType == "V":
            gridList[i].cost[2] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[2] = 2.5
    if gridList[i].neighbours[3] == "V":
        if gridList[i].locationType == "Q":
            gridList[i].cost[3] = 1
        if gridList[i].locationType == "E":
            gridList[i].cost[3] = 1.5
        if gridList[i].locationType == "V":
            gridList[i].cost[3] = 2
        if gridList[i].locationType == "P":
            gridList[i].cost[3] = 2.5

    ############## if there is a neighbour that is a playground
    if gridList[i].neighbours[0] == "P":
        if gridList[i].locationType == "Q":
            gridList[i].cost[0] = 1.5
        if gridList[i].locationType == "E":
            gridList[i].cost[0] = 2
        if gridList[i].locationType == "V":
            gridList[i].cost[0] = 2.5
        if gridList[i].locationType == "P":
            gridList[i].cost[0] = 3
    if gridList[i].neighbours[1] == "P":
        if gridList[i].locationType == "Q":
            gridList[i].cost[1] = 1.5
        if gridList[i].locationType == "E":
            gridList[i].cost[1] = 2
        if gridList[i].locationType == "V":
            gridList[i].cost[1] = 2.5
        if gridList[i].locationType == "P":
            gridList[i].cost[1] = 3
    if gridList[i].neighbours[2] == "P":
        if gridList[i].locationType == "Q":
            gridList[i].cost[2] = 1.5
        if gridList[i].locationType == "E":
            gridList[i].cost[2] = 2
        if gridList[i].locationType == "V":
            gridList[i].cost[2] = 2.5
        if gridList[i].locationType == "P":
            gridList[i].cost[2] = 3
    if gridList[i].neighbours[3] == "P":
        if gridList[i].locationType == "Q":
            gridList[i].cost[3] = 1.5
        if gridList[i].locationType == "E":
            gridList[i].cost[3] = 2
        if gridList[i].locationType == "V":
            gridList[i].cost[3] = 2.5
        if gridList[i].locationType == "P":
            gridList[i].cost[3] = 3

        ############## if there is a neighbour that is EMPTY
    if gridList[i].neighbours[0] == "E":
        if gridList[i].locationType == "Q":
            gridList[i].cost[0] = 0.5
        if gridList[i].locationType == "E":
            gridList[i].cost[0] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[0] = 1.5
        if gridList[i].locationType == "P":
            gridList[i].cost[0] = 2
    if gridList[i].neighbours[1] == "E":
        if gridList[i].locationType == "Q":
            gridList[i].cost[1] = 0.5
        if gridList[i].locationType == "E":
            gridList[i].cost[1] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[1] = 1.5
        if gridList[i].locationType == "P":
            gridList[i].cost[1] = 2
    if gridList[i].neighbours[2] == "E":
        if gridList[i].locationType == "Q":
            gridList[i].cost[2] = 0.5
        if gridList[i].locationType == "E":
            gridList[i].cost[2] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[2] = 1.5
        if gridList[i].locationType == "P":
            gridList[i].cost[2] = 2
    if gridList[i].neighbours[3] == "E":
        if gridList[i].locationType == "Q":
            gridList[i].cost[3] = 0.5
        if gridList[i].locationType == "E":
            gridList[i].cost[3] = 1
        if gridList[i].locationType == "V":
            gridList[i].cost[3] = 1.5
        if gridList[i].locationType == "P":
            gridList[i].cost[3] = 2

print("\n=========================================================================")

#############   STEP 6 -- Heuristic and A* Algorithms for Optimal Path
for l in range(0, len(gridList)):
    gridList[l].heuristic = [-1, -1, -1, -1]  # left,top,right,bottom
for i in range(0, len(gridList)):
    # get row and column for current gridList element
    currentRow = math.ceil(gridList[i].number / userRows)
    currentColumn = gridList[i].number % userColumns
    if currentColumn == 0:
        currentColumn = userColumns
    # get x and y coordinate for current element
    topRightX = round((currentColumn * 0.1), 2)
    topRightY = round(((currentRow - 1) * 0.2), 2)

    topLeftX = round(((currentColumn - 1) * 0.1), 2)
    topLeftY = topRightY

    bottomRightX = topRightX
    bottomRightY = round((currentRow * 0.2), 2)

    bottomLeftX = topLeftX
    bottomLeftY = bottomRightY

    # get distance to goal state
    topRightDistance = math.sqrt((abs((goalStateX - topRightX)) ** 2) + (abs((goalStateY - topRightY)) ** 2))
    topLeftDistance = math.sqrt((abs((goalStateX - topLeftX)) ** 2) + (abs((goalStateY - topLeftY)) ** 2))
    bottomRightDistance = math.sqrt((abs((goalStateX - bottomRightX)) ** 2) + (abs((goalStateY - bottomRightY)) ** 2))
    bottomLeftDistance = math.sqrt((abs((goalStateX - bottomLeftX)) ** 2) + (abs((goalStateY - bottomLeftY)) ** 2))
    '''
    print("TopLeft: " + str(topLeftDistance) +"TopRight: " + str(topRightDistance) + ",BottomRight: " + str(
        bottomRightDistance) + ",BottomLeft: " + str(bottomLeftDistance) + " for number: " + str(gridList[i].number))
    '''
    # rate Distances for heuristic
    heuristicDistanceList = [topLeftDistance, topRightDistance, bottomRightDistance,
                             bottomLeftDistance]  # topleft,topright,bottomright,bottomleft
    hAmount = 0
    for p in range(0, len(heuristicDistanceList)):
        heuristicIndex = heuristicDistanceList.index(min(heuristicDistanceList))
        heuristicDistanceList[heuristicIndex] = 100
        gridList[i].heuristic[heuristicIndex] = hAmount
        hAmount += 1

    gridList[i].printElement()


def calHeuristic(element):
    print("Optimal Path:")
    optimalPath = PriorityQueue()
