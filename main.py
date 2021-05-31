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
              "Edges:" + str(self.edges) + "\n" +
              "Cell Neighbours:" + str(self.neighbours) + "\n" +
              "Edge Costs:" + str(self.cost))

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
    e.printElement()
    print("_________________________")
    l = 0
    k = 4

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
l = 0
k = 4
for i in range(0, len(gridList)):
    gridList[i].edges = [edgeList[i], edgeList[i + 1], edgeList[i + userColumns + 1], edgeList[i + userColumns + 2]]
    #gridList[i].printElement()

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

if role == 'c' or role == 'C':
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if startCell <= gridSize:
        print("You have selected the start state to be: ", genMap[startCell - 1])
    else:
        startCell = int(
            input("Number out of range of grid: Enter the number of the cell that is the starting point/state: "))
    goalCell = 'Q'
elif role == 'v' or role == 'V':
    startCell = int(input("\nEnter the number of the cell that is the starting point/state: "))
    if startCell <= gridSize:
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
    gridList[i].printElement()

print("\n=========================================================================")
#############   STEP 6 -- Heuristic and A* Algorithms for Optimal Path
print("Optimal Path:")
optimalPath = PriorityQueue()

for i in range(0,len(gridList)):
    if role == 'c' or role == 'C':
        optimalPath.put(gridList[startCell-1].locationType, 1)

    if role == 'v' or role == 'V':
        optimalPath.put(gridList[startCell-1].locationType, 1)

print(optimalPath.queue)

'''
parents = []

def search(start, target, graph, cost, parents):
    nextNode = start

    while nextNode != target:
        for neighbor in graph[nextNode]:
            if graph[nextNode][neighbor] + cost[nextNode] < cost[neighbor]:
                cost[neighbor] = graph[nextNode][neighbor] + cost[nextNode]
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]
        del cost[nextNode]
        nextNode = min(cost, key=cost.get)
    return parents

result = search(startCell, goalCell, gridList, cost, parents)
'''

'''
def searchOptimal(slist, start, goal):
    visited = []
    queue = [[start]]

    if start == goal:
        print("Already at the desired location.")
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighb = list(node)

            for i in neighb:
                new_path = list(path)
                new_path.append(i)
                queue.append(new_path)

                if i == goal:
                    print("Path found = ", *new_path)
                    return
            visited.append(node)
    
    print("No path found.")
    return

searchOptimal(genMap,startCell,"Q")
'''

'''
for i in range(0,len(gridList)):
    if role == 'c' or role == 'C':
        optimalPath.put(gridList[startCell-1].locationType, 1)
        if gridList[startCell-1].neighbours[i] == "E":
            optimalPath.put(gridList[startCell].locationType, 2)



for i in range(optimalPath.qsize()):
    print(optimalPath.get())

'''

'''
optimalPath.put(1, gridList[startCell-1].cost[3])

for i in range(optimalPath.qsize()):
    print(optimalPath.get())
'''


