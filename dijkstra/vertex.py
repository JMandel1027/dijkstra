import sys

class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = { }
	
	def __str__(self):
		