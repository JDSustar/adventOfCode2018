import re
from collections import defaultdict


class Claim:
    def __str__(self):
        return "#" + self.id + " @ " + str(self.left) + "," + str(self.top) + ": " + str(self.wide) + "x" + str(
            self.tall)

    def __init__(self, id, left, top, wide, tall):
        self.id = id
        self.left = int(left)
        self.top = int(top)
        self.wide = int(wide)
        self.tall = int(tall)

    def inSquareInch(self, left, top):
        return self.left <= left <= self.left + self.wide and self.top <= top <= self.top + self.tall


regex = re.compile('\#(?P<id>\d+)\s+\@\s+(?P<left>\d+),(?P<top>\d+)\:\s+(?P<wide>\d+)x(?P<tall>\d+)')

claims = []
squareInchClaims = defaultdict(int)

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()

    for line in lines:
        match = regex.match(line)

        claim = Claim(match.group('id'), match.group('left'), match.group('top'), match.group('wide'),
                      match.group('tall'))
        claims.append(claim)

        cleanClaim = True

        for topPosition in range(0, claim.tall):
            for leftPosition in range(0, claim.wide):
                squareInchClaims[str(claim.top + topPosition) + 'x' + str(claim.left + leftPosition)] += 1

numOverlaps = sum(x > 1 for x in squareInchClaims.values())

print(numOverlaps)

# Part Two

for claim in claims:
    cleanClaim = True
    for topPosition in range(0, claim.tall):
        for leftPosition in range(0, claim.wide):
            claimPosition = str(claim.top + topPosition) + 'x' + str(claim.left + leftPosition)
            if squareInchClaims[claimPosition] != 1:
                cleanClaim = False

    if cleanClaim:
        print("CLEAN CLAIM:" + claim.id)
