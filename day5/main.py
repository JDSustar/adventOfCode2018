import pprint


def reactPolymer(polymerString):
    # This is really slow. Don't use this.
    #
    # i = 0
    #
    # while True:
    #     if i == len(polymerString) - 2:
    #         break
    #
    #     indexCharValue = ord(polymerString[i])
    #     nextCharValue = ord(polymerString[i + 1])
    #     if abs(indexCharValue - nextCharValue) == 32:
    #         polymerString = polymerString[:i] + polymerString[i + 2:]
    #         i = 0
    #     else:
    #         i += 1
    #
    # return polymerString

    reaction = True

    while reaction:
        incomingLength = len(polymerString)
        for chrIndex in range(65, 65 + 26):
            uppercaseChar = chr(chrIndex)
            lowercaseChar = chr(chrIndex + 32)

            polymerString = polymerString.replace(uppercaseChar + lowercaseChar, '')
            polymerString = polymerString.replace(lowercaseChar + uppercaseChar, '')

        if len(polymerString) != incomingLength:
            reaction = True
        else:
            reaction = False

    return polymerString


with open("input.txt", 'r') as inputfile:
    line = inputfile.readline()

basicReactString = line

basicResult = reactPolymer(basicReactString)

print(len(basicResult))

# PART TWO

bestLength = {}

for chrIndex in range(65, 65 + 26):
    uppercaseChar = chr(chrIndex)
    lowercaseChar = chr(chrIndex + 32)

    charReactString = line
    charReactString = charReactString.replace(uppercaseChar, '')
    charReactString = charReactString.replace(lowercaseChar, '')

    charReactString = reactPolymer(charReactString)

    bestLength[uppercaseChar] = len(charReactString)

pprint.pprint(bestLength)
