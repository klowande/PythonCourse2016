# hw5 ksl 8-24-2016 "singly linked list"


class Node(object):
	def __init__(self, _value=None, _point=None, _id=None):
		self.value = _value
		self.point = _point
		self.id = _id
	
	def __str__(self):
		return str(self.value)
		
class sll(object):

# functionality requirements:

	def __init__(self, value): # O(1), yes
		self.head = Node(value)
		self.end = self.head
		self.count = 1
		
	def length(self): # get the length of the list, # O(1), yes
		return self.count
		
	def addNode(self, new_value): # add a node to the end, # O(1), yes
		node = Node(new_value)
		self.connect(self.end,node)
		self.end = node
		self.count +=1
		
	def __str__(self): # print all the nodes, # O(N), yes
		sllist = ''
		start = self.head
		while start:
			sllist += str(start) + ' --> '
			start = start.point
		return sllist
	
	def addNodeAfter(self, new_value, after_node): # add node after particular node, # O(N), yes
		after = self.find(after_node)
		next_node = after.point
		added_node = Node(new_value)
		self.connect(after,added_node)
		self.connect(added_node,next_node)
		self.newEnd()
	
	def addNodeBefore(self, new_value, before_node): # add node before particular node, # O(N), yes
		before = self.findprevious(before_node)
		next_node = before.point
		added_node = Node(new_value)
		self.connect(before,added_node)
		self.connect(added_node,next_node)

	def removeNode(self, node_to_remove): # remove the first occurrence of a particular node, # O(N), yes
		remove = self.find(node_to_remove)
		previous = self.findprevious(node_to_remove)
		previous.point = remove.point
		self.newEnd()
		
	def removeNodesByValue(self, value): # remove all nodes of a particular value, # O(N), yes
		while self.find(value) != None:
			self.removeNode(value)
		self.newEnd()

	def reverse(self): # print a reversed list, # O(N^2), yes
		reversed = sll(self.end)
		before = self.findprevious(self.end.value)
		while before != self.head:
			reversed.addNode(before)
			before = self.findprevious(before.value)
		reversed.addNode(self.head)
		print reversed
		
# helper functions:
	
	def connect(self,first_node,second_node): # helper function that connects two nodes
		first_node.point = second_node	
	
	def find(self,node_value): # helper function that finds a node
		try:
			start = self.head
			while start.value != node_value:
				start = start.point
			return start
		except AttributeError:
			print 'The node requested does not exist.'
			return None
			
	def findprevious(self,node_value): # helper function that finds the previous node
		try:
			start = self.head
			while start.value != node_value:
				previous = start
				start = start.point
			return previous
		except AttributeError:
			print 'The node requested does not exist.'
			return None
	
	def newEnd(self): # helper function that sets the new end
		start = self.head
		while start:
			end = start
			start = start.point
		self.end = end
	
# test code		
a = sll(1)
a.length()
a.addNode(4)
a.addNode(5)
a.addNode(6)
a.addNodeAfter(19,5)
a.addNodeBefore(12,5)
print a
a.removeNode(5)
print a
a.addNode(12)
print a
a.removeNodesByValue(12)
print a
print a.end
a.reverse()	
