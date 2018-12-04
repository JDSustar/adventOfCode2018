import re
from collections import defaultdict


class Guard:
    def __init__(self, guardId):
        self.guardId = guardId
        self.minutesAsleep = defaultdict(int)

    def addTimeAsleep(self, start, end):
        for i in range(start, end):
            self.minutesAsleep[i] += 1

    def totalMinutesAsleep(self):
        return sum(self.minutesAsleep.values())

    def __str__(self):
        string = 'GUARD ID ' + str(self.guardId) + ': '
        for i in range(0, 59):
            if i in self.minutesAsleep:
                string = string + str(self.minutesAsleep[i])
            else:
                string = string + 'X'

        string = string + "\t TOTAL MINUTES ASLEEP: " + str(self.totalMinutesAsleep())

        return string


class Event:
    def __init__(self, fullText):
        match = re.match(
            '\[(?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2})\s+(?P<hour>\d+)\:(?P<minute>\d+)\]\s+(?P<eventText>.*)',
            fullText)
        self.year = int(match.groupdict()['year'])
        self.month = int(match.groupdict()['month'])
        self.day = int(match.groupdict()['day'])
        self.hour = int(match.groupdict()['hour'])
        self.minute = int(match.groupdict()['minute'])
        self.eventText = match.groupdict()['eventText']
        self.guardId = None
        self.isFallsAsleepEvent = None
        self.isWakesUpEvent = None
        self.parseEventText()

    def parseEventText(self):
        if '#' in self.eventText:
            self.guardId = int(''.join(re.findall('\d', self.eventText)))
        elif 'falls asleep' in self.eventText:
            self.isFallsAsleepEvent = True
        elif 'wakes up' in self.eventText:
            self.isWakesUpEvent = True

    def __str__(self):
        return "[" + str(self.year) + "-" + '{:02d}'.format(self.month) + '-' + '{:02d}'.format(
            self.day) + '] ' + '{:02d}'.format(self.hour) + ':' + '{:02d}'.format(self.minute) + ' ' + self.eventText


events = []

with open("input.txt", 'r') as inputfile:
    lines = inputfile.readlines()
    for line in lines:
        event = Event(line)
        events.append(event)

sortedEvents = sorted(events, key=lambda x: (x.year, x.month, x.day, x.hour, x.minute))
guards = {}
currentGuard = None
currentSleepTime = None

for event in sortedEvents:
    if event.guardId is not None:
        currentGuard = event.guardId
    elif event.isFallsAsleepEvent:
        currentSleepTime = event.minute
    elif event.isWakesUpEvent:
        if currentGuard not in guards:
            guards[currentGuard] = Guard(currentGuard)

        guards[currentGuard].addTimeAsleep(currentSleepTime, event.minute)

maxGuard = sorted(guards.values(), key=lambda x: x.totalMinutesAsleep(), reverse=True)[0]
maxMinute = max(maxGuard.minutesAsleep.keys(), key=(lambda key: maxGuard.minutesAsleep[key]))

print(maxGuard)
print(maxMinute)

# Part Two

maxGuardId = 0
maxMinute = 0
maxMinuteValue = 0

for g in guards.values():
    gmaxMinute = max(g.minutesAsleep.keys(), key=(lambda key: g.minutesAsleep[key]))
    gmaxMinuteValue = max(g.minutesAsleep.values())
    if gmaxMinuteValue > maxMinuteValue:
        maxGuardId = g.guardId
        maxMinute = gmaxMinute
        maxMinuteValue = gmaxMinuteValue

print(maxGuardId, maxMinute, maxMinuteValue)
