from collections import defaultdict
import re
import sys
from statistics import mode
import copy


# This isn't my best work. I really don't do well with 2D or 3D space. Probably a lot of refactor potential
# here. I probably won't ever get to it. Just know that I'm not proud of this code, but it works. And it
# gets the right answer. If you're actually reading this, Hi!


def printGrid(grid):
    for i in range(0, 500):
        lineString = ''
        for j in range(0, 500):
            lineString = lineString + str(grid[i][j])
        print(lineString)


def getManhattanDistance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


grid = defaultdict(dict)

for i in range(0, 500):
    for j in range(0, 500):
        grid[i][j] = '.'

pointIndex = 0
points = {}

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()

    for line in lines:
        match = re.match('(\d+), (\d+)', line)
        x = int(match.group(1))
        y = int(match.group(2))

        grid[x][y] = pointIndex
        pointIndex += 1

        points[pointIndex] = (x, y)

closeGrid = copy.deepcopy(grid)

for i, jdict in grid.items():
    for j in jdict.keys():
        minDistance = sys.maxsize
        closestPointIndex = None

        for pointIndex, point in points.items():
            distance = getManhattanDistance(i, j, point[0], point[1])

            if distance < minDistance:
                closestPointIndex = pointIndex
                minDistance = distance
            elif distance == minDistance:
                closestPointIndex = None

        closeGrid[i][j] = closestPointIndex if closestPointIndex is not None else '.'

disqualifiedPointIndexes = set()

for i in range(0, 500):
    disqualifiedPointIndexes.add(closeGrid[i][0])
    disqualifiedPointIndexes.add(closeGrid[i][499])
    disqualifiedPointIndexes.add(closeGrid[0][i])
    disqualifiedPointIndexes.add(closeGrid[499][i])

print(disqualifiedPointIndexes)

closeGridAsList = []

for i in range(0, 500):
    for j in range(0, 500):
        closeGridAsList.append(closeGrid[i][j])

closeGridAsList = [x for x in closeGridAsList if x not in disqualifiedPointIndexes]
mode = mode(closeGridAsList)
count = closeGridAsList.count(mode)

print(mode, count)

# PART TWO

lessThanThreshold = 0

for i in range(0, 500):
    for j in range(0, 500):
        totalDistances = 0
        for point in points.values():
            totalDistances += getManhattanDistance(i, j, point[0], point[1])

        if totalDistances < 10000:
            lessThanThreshold += 1

print(lessThanThreshold)
