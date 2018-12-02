from collections import Counter

twoLetterOccurrences = 0
threeLetterOccurrences = 0

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        c = Counter(line)
        if 2 in c.values():
            twoLetterOccurrences += 1

        if 3 in c.values():
            threeLetterOccurrences += 1

print(twoLetterOccurrences, " * ", threeLetterOccurrences, " = ", twoLetterOccurrences * threeLetterOccurrences)

# PART TWO

seenBoxIds = set()
duplicateBoxId = None

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        for i in range(0, len(line) - 1):
            # Python strings are immutable, so have to convert list in order to end the chars
            lineCharList = list(line[:-1])  # Remove new line character
            lineCharList[i] = "_"

            blankedBoxId = "".join(list(lineCharList))

            if blankedBoxId in seenBoxIds:
                duplicateBoxId = blankedBoxId.replace("_", "")
            else:
                seenBoxIds.add(blankedBoxId)

print(duplicateBoxId)
