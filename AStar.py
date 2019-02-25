import math

class AStar:
	def __init__(self, openList, closedList, pathList):
		self.openList = openList
		self.closedList = closedList
		self.pathList = pathList

	def run(self):
		map = Mappy(3,3,(0,0),(2,2),[(1,1), (2,0), (0,2)])
		openList = []
		isFinished = False
		while not isFinished:
			self.aStarLoop(map, openList)

			#Node.printPath(map.currentPath, "Test")
			#print(map)

			#if map.currentPath is None:
				#print("currentPath is None")
			#else:
				#print("currentPath is Not None")
			if map.currentPath[len(map.currentPath) -1 ].x == map.endPoint[0] and map.currentPath[len(map.currentPath) - 1].y == map.endPoint[1]:
				isFinished = True
			print('::::: Run Loop End ::::::')
		Node.printPath(map.currentPath, "Solution")
		#print(pathList)

	def aStarLoop(self, map, openList):
		cursor = map.currentPath[len(map.currentPath) - 1]
		#print(map.currentPath)
		neighborList = [(cursor.x,cursor.y+1), (cursor.x +1, cursor.y), (cursor.x,cursor.y-1), (cursor.x -1,cursor.y)]
		#print(neighborList)
		for i in range(4):
			if not neighborList[i] in map.blockedList:
				if not neighborList[i] in openList:
					if not self.tupleInClosedList(self.closedList, neighborList[i]):
						nextNode = Node(neighborList[i][0], neighborList[i][1], len(map.currentPath) + 1,
							self.distance(neighborList[i], map.endPoint), map.currentPath[-1])
						if not (nextNode.x == map.startPoint[0] and nextNode.y == map.startPoint[1]):
							openList.append(nextNode)
							#nextNode.printLoc("AStarLoop(Fitness): " + str(nextNode.f))
		mostFitNeighbor = openList[self.getLowestF(openList)]
		mostFitNeighbor.printLoc("aStarLoop: most fit neighbor")
		openList.remove(mostFitNeighbor)
		self.closedList.append(mostFitNeighbor)
		if (mostFitNeighbor.x, mostFitNeighbor.y) in neighborList:
			map.currentPath.append(mostFitNeighbor)
		else:
			map.currentPath = self.rebuildCurrentPath(map.currentPath, mostFitNeighbor)
			# add everyone that's not in closed or outside the map or blocked to openList
			# pick the lowest f value of all open openList
			# rebuild currentPath if necessary
			# pop selection from openList and add it to closedList and currentPath
		#print('::::: AStar Loop End ::::::')

	def distance(self, firstPoint, secondPoint):
		returnVal = math.sqrt(((firstPoint[0] - secondPoint[0])**2) + ((firstPoint[1] - secondPoint[1])**2))
		return returnVal
	def rebuildCurrentPath(self, currentPath, nextCursor):
		newPath = [nextCursor]
		#nextCursor.printLoc("rebuildCurrentPath: nextCursor")
		nextParent = nextCursor.p
		while nextParent is not None:
			#nextParent.printLoc("rebuildCurrentPath")
			newPath.append(nextParent)
			nextParent = nextParent.p
		newPath.reverse()
		#Node.printPath(newPath, "rebuildCurrentPath")
		return newPath
			#is currentpath[i] a neighbor to nextCursor

	def tupleInClosedList(self, closedList, tuple):
		for i in range(len(closedList)):
			if closedList[i].x == tuple[0] and closedList[i].y == tuple[1]:
				return True
		return False

	def getLowestF(self,openList):
		currentLowest = 1000000000
		lowestIndex = -1
		#for n in openList:
		#	n.printLoc("openList")
		for i in range(len(openList)):
			#print(openList[i].f)
			if openList[i].f < currentLowest:
				currentLowest= openList[i].f
				lowestIndex = i
		return lowestIndex

class Mappy:
	def __init__(self, width, length, startPoint, endPoint, blockedList):
		openList = []
		self.closedList = [startPoint]
		self.currentPath = [Node(startPoint[0],startPoint[1],0,0,None)]
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.blockedList = blockedList



	def run(self):
		isFinished = False
        #while(!isFinished):
            #for i in range(4):
                # 0 = top neighbor, go clockwise
                # add everyone that's not in closed or outside the map or blocked to openList
                # pick the lowest f value of all open openList
                # rebuild currentPath if necessary
                # pop selection from openList and add it to closedList and currentPath

class Node:
	def __init__(self, x, y, g, h, p):
		self.f = g + h
		self.x = x
		self.y = y
		self.g = g
		self.h = h
		self.p = p

	def neighborOf(self, otherNode):
		otherTuple = (otherNode.x, otherNode.y)
		selfTuple = (self.x, self.y)
		neighborList = [(selfTuple[0],selfTuple[1]+1), (selfTuple[0] +1, selfTuple[1]), (selfTuple[0],selfTuple[1]-1), (selfTuple[0] -1,selfTuple[1])]
		if otherTuple in neighborList:
			return True
		else:
			return False

	def printLoc(self, tag):
		print(tag + " Node(" + str(self.x) + ", " + str(self.y) + ")")

	def printPath(currentPath, tag):
		print(tag)
		for i in range(len(currentPath)):
			print(currentPath[i].printLoc(tag + "/" + str(i)))

myAStarFirstTry = AStar([],[],[])
myAStarFirstTry.run()
