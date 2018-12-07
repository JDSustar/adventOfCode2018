import re
import pprint


class Step():
    def __init__(self, letter):
        self.letter = letter
        self.prereqs = []
        self.postreqs = []

    def addPrereq(self, step):
        self.prereqs.append(step)
        step.postreqs.append(self)

    def __str__(self):
        return 'STEP ' + self.letter + ': Requires ' + str([x.letter for x in self.prereqs]) + ' And Permits ' + str(
            [x.letter for x in self.postreqs])

    def __repr__(self):
        return 'STEP ' + self.letter


steps = {}

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()

    regex = re.compile('Step (\w) must be finished before step (\w) can begin')

    for line in lines:
        match = regex.match(line)
        stepLetter = match.group(2)
        prereqLetter = match.group(1)

        if stepLetter not in steps:
            steps[stepLetter] = Step(stepLetter)

        if prereqLetter not in steps:
            steps[prereqLetter] = Step(prereqLetter)

        steps[stepLetter].addPrereq(steps[prereqLetter])

orderString = ''
completedSteps = set()

availableSteps = [x for x in steps.values() if len(x.prereqs) == 0]

while len(availableSteps) != 0:
    minStep = availableSteps[0]
    for step in availableSteps:
        if step.letter < minStep.letter:
            minStep = step

    orderString += minStep.letter
    availableSteps.remove(minStep)
    completedSteps.add(minStep)

    for step in minStep.postreqs:
        if all(x in completedSteps for x in step.prereqs):
            availableSteps.append(step)

print(orderString)
