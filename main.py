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
        print("Element Number:" + str(self.number) + "\n" +
              "Location Type:" + self.locationType + "\n" +
              "Element Edges:" + str(self.edges))

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

print("\n=================================================================")
print("Program Begins:")
userRows = int(input("\nEnter amount of Rows? "))
userColumns = int(input("Enter amount of Columns? "))

print("=================================================================")
print("Information of each cell:\n")
edges = (list(string.ascii_letters))  # list of alphabetical edges (lowercase then uppercase)
gridSize = userRows * userColumns
l = 0
k = 4
for i in range(1, gridSize + 1):  # iterate over all items in grid
    gridList = []
    e = createGridElement(i, edges[l:k])
    gridList.append(e)
    e.printElement()
    print("_________________________")
    l = l + 4  # increment to next 4 edge elements
    k = k + 4

print("=================================================================")
print("Generated Map:\n")
map = [["|   |" for a in range(userColumns)] 
    for b in range(userRows)]
xCoord = userColumns
yCoord = userRows
for i in range(0,xCoord):
    for j in range(0,yCoord):
        map[i][j] = "|   |"
#map[xCoord][yCoord] = "| A |"
#print(map)
for i in map:
    #print("--- --- ---")
    print(" ".join(i))
    #print("--- --- ---")


print("\n=================================================================")
#selectedRow = int(input(print("Enter the row of starting point/state: ")))
#selectedCol= int(input(print("Enter the column of starting point/state: ")))
