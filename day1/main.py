import csv

# PART ONE

resultingFrequency = 0

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        if line[0] == '+':
            resultingFrequency += int(line[1:])
        elif line[0] == '-':
            resultingFrequency -= int(line[1:])

print(resultingFrequency)

# PART TWO

resultingFrequency = 0
seenFrequencies = set()

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()
    i = 0
    while True:
        line = lines[i]
        if line[0] == '+':
            resultingFrequency += int(line[1:])
        elif line[0] == '-':
            resultingFrequency -= int(line[1:])

        if resultingFrequency in seenFrequencies:
            break
        else:
            seenFrequencies.add(resultingFrequency)

        i = (i + 1) % len(lines)


print(resultingFrequency)