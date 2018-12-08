numbers = []
topNode = None


class Node:
    def __init__(self, numChildren, numData, remainingNumbers):
        self.numChildren = numChildren
        self.numData = numData
        self.metadata = []
        self.children = []

        for i in range(0, self.numChildren):
            childNumChildren = remainingNumbers.pop(0)
            childNumData = remainingNumbers.pop(0)
            self.children.append(Node(childNumChildren, childNumData, remainingNumbers))

        for i in range(0, self.numData):
            self.metadata.append(remainingNumbers.pop(0))

    def getRecursiveMetadataSum(self):
        nodeSum = sum(self.metadata)

        for child in self.children:
            nodeSum += child.getRecursiveMetadataSum()

        return nodeSum

    def getNodeValue(self):
        value = 0

        if len(self.children) > 0:
            for data in self.metadata:
                if len(self.children) > data - 1:
                    value += self.children[data - 1].getNodeValue()
        else:
            value = sum(self.metadata)

        return value


with open("input.txt", 'r') as inputfile:
    line = inputfile.readline()

    for numberString in line.split(' '):
        number = int(numberString)
        numbers.append(number)

topNodeNumChildren = numbers.pop(0)
topNodeNumData = numbers.pop(0)
topNode = Node(topNodeNumChildren, topNodeNumData, numbers)

print(topNode.getRecursiveMetadataSum())

print(topNode.getNodeValue())
