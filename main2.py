class Node:
    def __init__(self, number, letter, neighbours, moveCost, heuristicCost, algorithmCost):
        self.number = number
        self.letter = letter
        self.neighbours = neighbours  # left,up,right,down
        self.moveCost = moveCost  # left,up,right,down
        self.heuristicCost = heuristicCost  # left,up,right,down
        self.algorithmCost = algorithmCost  # left,up,right,down

    def printElement(self):
        print("Node Number:" + str(self.number) + "\n" +
              "Node Letter:" + str(self.letter) + "\n" +
              "Neighbours:" + str(self.neighbours) + "\n" +
              "Edge Costs:" + str(self.moveCost) + "\n" +
              "Heuristic Costs:" + str(self.heuristicCost) + "\n"
              + "Algorithm Costs:" + str(self.moveCost))


def createGridElement(number):
    locationChoices = ["Q", "V", "P", "E"]
    # Q for quarantine, V for vaccine, P for playground, E for empty
    locationType = random.choice(locationChoices)  # chooses random location type
    element = GridElement(number, locationType, [], [], [], [], "0")
    return element


print("\n======================================================================")
#############   STEP 1 -- User inputs to make map
print("Program Begins:")
userRows = int(input("\nEnter amount of Rows? "))
userColumns = int(input("Enter amount of Columns? "))

# print("========================================================================")
#############   STEP 2 -- List all items in list with theyre appropriate edges
# print("Information of each cell:\n")
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

letterList = (list(string.ascii_letters))  # list of alphabetical edges (lowercase then uppercase)

rc = 0
for i in range(0, len(gridList)):
    if gridList[i].number % userColumns == 1 and gridList[i].number != 1:
        gridList[i].nodes = [letterList[rc + 1], letterList[rc + 2], letterList[rc + userColumns + 2],
                             letterList[rc + userColumns + 3]]
        rc += 2
    else:
        gridList[i].nodes = [letterList[rc], letterList[rc + 1], letterList[rc + userColumns + 1],
                             letterList[rc + userColumns + 2]]
        rc += 1

counter = 0
for j in range(0, len(gridList)):
    print("| ", genMap[j], " |", end='')
    counter += 1
    if counter == userColumns:
        print(" ")
        counter = 0
'''
nodeAmount = (userColumns * userRows) + (userColumns + userRows + 1)

def createNodeElement(number):
    nodeElement = Node(number, letterList[number], [], [], [], [])
    return nodeElement


nodeList = []
for m in range(0, nodeAmount):
    n = createNodeElement(m)
    nodeList.append(n)

# find neighboring nodes
for i in range(len(nodeList)):
    nodeList[i].moveCost = [0, 0, 0, 0]
    nodeList[i].heuristicCost = [0, 0, 0, 0]
    nodeList[i].algorithmCost = [0, 0, 0, 0]
    if nodeList[i].number == 0:
        nodeList[i].neighbours = [-1, -1, letterList[i + 1], letterList[i + userColumns + 1]]
    elif nodeList[i].number == nodeAmount - 1:
        nodeList[i].neighbours = [letterList[i - 1], letterList[i - userColumns - 1],
                                  -1, -1]
    elif nodeList[i].number > nodeAmount - userColumns:
        nodeList[i].neighbours = [letterList[i - 1], letterList[i - userColumns - 1],
                                  letterList[i + 1], -1]
    else:
        nodeList[i].neighbours = [letterList[i - 1], letterList[i - userColumns - 1],
                                  letterList[i + 1], letterList[i + userColumns + 1]]
for i in range(0, len(nodeList)):
    # check if there are no left neighbours
    if nodeList[i].number % (userColumns + 1) == 0:
        nodeList[i].neighbours[0] = -1
        nodeList[i].moveCost[0] = -1
        nodeList[i].heuristicCost[0] = -1
        nodeList[i].algorithmCost[0] = -1
    # check if there are no upper neighbours
    if nodeList[i].number <= userColumns:
        nodeList[i].neighbours[1] = -1
        nodeList[i].moveCost[1] = -1
        nodeList[i].heuristicCost[1] = -1
        nodeList[i].algorithmCost[1] = -1
    # check if there are no right neighbours
    if nodeList[i].number % (userColumns + 1) == 4:
        nodeList[i].neighbours[2] = -1
        nodeList[i].moveCost[2] = -1
        nodeList[i].heuristicCost[2] = -1
        nodeList[i].algorithmCost[2] = -1
    # check if there are no bottom neighbours
    if nodeList[i].number >= nodeAmount - userColumns - 1:
        nodeList[i].neighbours[3] = -1
        nodeList[i].moveCost[3] = -1
        nodeList[i].heuristicCost[3] = -1
        nodeList[i].algorithmCost[3] = -1
'''

print("\n=======================================================================")
#############   STEP 4 --  User choosing the Role C or Role V and inputs start state
print("Role C (Covid Patients)\nRole V (People Getting Vaccinated)\n")
role = (input("Choose the Role C or the Role V by entering C or V: "))

cellWidth = 0.1
cellLength = 0.2

gridWidth = cellWidth * userColumns
gridLength = cellLength * userRows

# For role C
if role == 'c' or role == 'C':
    # user input for x and y
    startCellxInput = float(input("\nEnter an x coordinate as the starting point/state (Choose between 0 and " + str(
        round(gridWidth, 2)) + "): "))
    startCellyInput = float(input(
        "Enter a y coordinate as the starting point/state (Choose between 0 and " + str(round(gridLength, 2)) + "): "))

    # finding the row and column obased on the user input
    startRow = (math.floor(startCellyInput / cellLength)) + 1
    print("Start state is in row: " + str(startRow))
    startColumn = (math.floor(startCellxInput / cellWidth)) + 1
    print("Start state is in column: " + str(startColumn))

    # finding the start cell number based on the row and column
    startCell = ((startRow - 1) * userColumns) + startColumn
    print("Start State Cell Number: " + str(startCell))

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

    print("Goal Cell Coordinates: " + str(goalStateX) + "," + str(goalStateY))

    print("\nStarting State: ", genMap[startCell - 1], "(Cell: ", startCell, ")   ------->  Goal State: Q ", "(Cell: ",
          goalState, ")")

# For role V
if role == 'v' or role == 'V':
    # user input for x and y
    startCellxInput = float(input("\nEnter an x coordinate as the starting point/state (Choose between 0 and " + str(
        round(gridWidth, 2)) + "): "))
    startCellyInput = float(input(
        "Enter a y coordinate as the starting point/state (Choose between 0 and " + str(round(gridLength, 2)) + "): "))

    # finding the row and column obased on the user input
    startRow = (math.floor(startCellyInput / cellLength)) + 1
    print("Start state is in row: " + str(startRow))
    startColumn = (math.floor(startCellxInput / cellWidth)) + 1
    print("Start state is in column: " + str(startColumn))

    # finding the start cell number based on the row and column
    startCell = ((startRow - 1) * userColumns) + startColumn
    print("Start State Cell Number: " + str(startCell))

    startX = round(((startColumn - 1) * 0.1), 2)
    startY = round((startRow * 0.2), 2)

    print("Start Cell Coordinates: " + str(startX) + "," + str(startY))
