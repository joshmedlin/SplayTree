class TreeNode:
	def __init__(self, leftChild, rightChild, parent, value):
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.value = value
		self.parent = parent

	def isTopLevel(self):
		return self.parent is None

	def insertWithRotate(self, value):
		print("entry: insertWithRotate")
		if(value < self.value):
			if(self.leftChild is None):
				self.leftChild = TreeNode(None, None, self, value)
				return self.leftChild.rotate()
			else:
				return self.leftChild.insertWithRotate(value)
		else:
			if(self.rightChild is None):
				self.rightChild = TreeNode(None, None, self, value)
				return self.rightChild.rotate()
			else:
				return self.rightChild.insertWithRotate(value)

	def insertPostRotate(self, node):
		print("entry: insertPostRotate")
		if(node.value < self.value):
			if(self.leftChild is None):
				self.leftChild = node
			else:
				self.leftChild.insertPostRotate(node)
		else:
			if(self.rightChild is None):
				self.rightChild = node
			else:
				self.rightChild.insertPostRotate(node)

	def rotate(self):
		print("entry: rotate (parent = " + str(self.parent.value) + " )")
		#return self
		if(self.parent is None):
			return self
		if(self.value > self.parent.value):
			#self.insertPostRotate(TreeNode(self.parent.leftChild, None, self, self.parent.value))
			self.parent.rightChild = None
			self.leftChild = self.parent
		else:
			self.parent.leftchild = None
			self.rightChild = self.parent
			#self.insertPostRotate(TreeNode(None, self.parent.rightChild, self, self.parent.value))
		tempNode = self.parent
		self.parent = self.parent.parent
		tempNode.parent = self
		if(not self.isTopLevel()):
			print("rotate again!")
			self.rotate()
		return self

	def traceTraversal(self):
		if( not self.leftChild is None):
			self.leftChild.traceTraversal()
		print(self.value)
		if( not self.rightChild is None):
			self.rightChild.traceTraversal()

	def printRoot(self):
		rootVal = str(self.value)
		if not self.parent is None:
			parentVal = str(self.parent.value)
		else:
			parentVal = "None"
		if not self.leftChild is None:
			leftVal = str(self.leftChild.value)
		else:
			leftVal = "None"
		if not self.rightChild is None:
			rightVal = str(self.rightChild.value)
		else:
			rightVal = "None"

		print("Rootvalue: " + rootVal + " parentVal: " + parentVal + " leftVal: " + leftVal + " rightVal: " + rightVal)

myTree = TreeNode(None, None, None, 12)
myTree = myTree.insertWithRotate(8)
#myTree.printRoot()
myTree = myTree.insertWithRotate(5)
myTree.printRoot()
myTree.traceTraversal()