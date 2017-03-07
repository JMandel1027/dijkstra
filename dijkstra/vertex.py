import sys

class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = { }
	
	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
	
	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight
		
	'''
		create a priority queue/ heap to manage vertex progressions
		
		key = id aka node
		adjacent = neighbors
		key h[] = the number of neigbors with the key of id/node
		heap array h[] with be inside of heap obj
		
		insert(node):
			h[++neighbors] = node
			siftUp( node) number of adjacent nodes in heap
	'''