# hw5 ksl 8-24-2016 "singly linked list"


class Node(object):
	def __init__(self, _value=None, _point=None):
		self.value = _value
		self.point = _point
	
	def data(self):
		return self.value
		
	def pointer(self):
		return self.point
	
	def link(self,new_point):
		self.point = new_point
	
	def __str__(self):
		return str(self.value)
		
	def __repr__(self):
		return str(self.value)

class sll(object):
	def __init__(self, value):
		self.head = Node(value)
		self.end = self.head
		self.count = 1
		
	def length(self):
		return self.count
	
	def addNode(self, new_value):
		self.end.link(new_value)
		self.end = Node(new_value)
		self.count +=1

# in-progress
		
	def __str__(self):
		start = self.head
		while start.data != self.end.data:
			print str(start) + '-->'
			start = start.point

# uncoded
	
	def addNodeAfter(self, new_value, after_node):
	
	def addNodeBefore(self, new_value, before_node):
	
	def removeNode(self, node_to_remove):
	
	def removeNodesByValue(self, value):
	
	def reverse(self):
		
	
# For each of the above methods, figure out what the computation complexity of your 
# implementation is and state whether or not you think that is the best possible complexity class.

# Make sure that your implementation is correct and robust to bad inputs.


# test code
a = LinkedList(12)
a.head
a.addNode(13)
a.length()
print a # not functional