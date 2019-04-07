class Node:
	def __init__(self, outgoingNodes, name):
		self.outgoingNodes = outgoingNodes
		self.incomingNodes = []
		self.name = name
		self.fitness = 0

	def process(self):
		if self.outgoingNodes is not None:
			print(self.outgoingNodes[0][0].name)
			self.outgoingNodes.sort(key=comparator)
			self.fitness = self.outgoingNodes[0][0].fitness + self.outgoingNodes[0][1]
		else:
			self.fitness = 0

		for incomingNode in self.incomingNodes:
			incomingNode.process()

	def traversal(self):
		print(self.name)
		if self.outgoingNodes:
			self.outgoingNodes[0][0].traversal()


def main(tailNode, startNode):
	tailNode.process()
	print("total length = " + str(startNode.fitness))
	startNode.traversal()

def comparator(val):
	return val[0].fitness + val[1]

#Main Logic
tailNode = Node(None, "final")
anotha = Node([(tailNode, 3)], "anotha")
bruh = Node([(tailNode, 5)], "bruh")
clan = Node([(tailNode, 1)], "culwhch")
dragon = Node([(tailNode, 5)], "uther")
newMexico = Node([(clan, 1), (dragon, 2)], "desert")
newPath = Node([(newMexico, 3)], "nuPont")
middleGuy = Node([(anotha, 7), (bruh, 2)], "middlin")
startNode = Node([(middleGuy, 2), (newPath, 2)], "starter")

tailNode.incomingNodes = [anotha, bruh, clan, dragon]
anotha.incomingNodes = [middleGuy]
bruh.incomingNodes = [middleGuy]
middleGuy.incomingNodes = [startNode]
clan.incomingNodes = [newMexico]
dragon.incomingNodes = [newMexico]
newMexico.incomingNodes = [newPath]
newPath.incomingNodes = [startNode]
main(tailNode, startNode)