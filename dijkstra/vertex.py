import sys

class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = { }
	
	def __str__(self):
		return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
	
	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight