# hw5 ksl 8-24-2016 "singly linked list"


class Node(object):
	def __init__(self, _value=None, _point=None):
		self.value = _value
		self.point = _point
		
	def __str__(self):
		return str(self.value)
		
class sll(object):
	def __init__(self, value):
		self.head = Node(value)
		self.end = self.head
		self.count = 1
		
	def length(self): # get the length of the list
		return self.count
		
	def addNode(self, new_value): # add a node to the end
		node = Node(new_value)
		self.end = node
		self.count +=1
		
	def __str__(self): # print all the nodes
		sllist = ''
		start = self.head
		while start:
			sllist += str(start) + ' --> '
			start = start.point
		sllist += str(self.end)
		return sllist
	
#	def addNodeAfter(self, new_value, after_node):
		
	
	
a = sll(1)
a.length()
a.addNode(4)
a.addNode(5)
a.addNode(6)
print a


# uncoded

	def addNodeAfter(self, new_value, after_node):
	
	def addNodeBefore(self, new_value, before_node):
	
	def removeNode(self, node_to_remove):
	
	def removeNodesByValue(self, value):
	
	def reverse(self):
		
	
# For each of the above methods, figure out what the computation complexity of your 
# implementation is and state whether or not you think that is the best possible complexity class.

# Make sure that your implementation is correct and robust to bad inputs.
