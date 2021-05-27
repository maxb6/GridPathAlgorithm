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


userRows = int(input("\nAmount of Rows?"))
userColumns = int(input("Amount of Columns?"))

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

