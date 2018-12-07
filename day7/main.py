import re
import pprint


class Step():
    def __init__(self, letter):
        self.letter = letter
        self.prereqs = []
        self.postreqs = []
        self.timeRequired = 60 + ord(letter) - 64

    def addPrereq(self, step):
        self.prereqs.append(step)
        step.postreqs.append(self)

    def __str__(self):
        return 'STEP ' + self.letter + ': Requires ' + str(self.timeRequired)

    def __repr__(self):
        return 'STEP ' + self.letter + ' - ' + str(self.timeRequired) + ' sec'


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

# PART TWO

orderString = ''
completedSteps = set()
time = 0
availableSteps = [x for x in steps.values() if len(x.prereqs) == 0]
availableWorkers = 5
stepsInProgress = {}

while len(availableSteps) != 0 or len(stepsInProgress) != 0:
    for step, timeRemaining in stepsInProgress.items():
        stepsInProgress[step] -= 1

        if stepsInProgress[step] == 0:
            completedSteps.add(step)

    for step in completedSteps:
        if step in stepsInProgress:
            stepsInProgress.pop(step)
            completedSteps.add(step)
            for poststep in step.postreqs:
                if all(x in completedSteps for x in poststep.prereqs):
                    availableSteps.append(poststep)

            availableWorkers += 1

    while availableWorkers > 0 and len(availableSteps) > 0:
        minStep = availableSteps[0]
        for step in availableSteps:
            if step.letter < minStep.letter:
                minStep = step

        orderString += minStep.letter
        availableSteps.remove(minStep)
        stepsInProgress[minStep] = minStep.timeRequired
        availableWorkers -= 1

    time += 1

time -= 1

print(str(time))
