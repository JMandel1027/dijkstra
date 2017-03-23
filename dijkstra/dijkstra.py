from collections import namedtuple, deque
from pprint import pprint as pp

inf = float('inf')
Edge = namedtuple('tinyEWD.txt', 'start, end, cost')


class Graph:
	def __init__(self, edges):
		# vertices are composed of 2 endpoints aka edges between graph and stored as list
		self.edges = edges2 = [Edge(*edge) for edge in edges]
		self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
	
	def dijkstra(self, source, dest):
		assert source in self.vertices
		if source not in self.vertices:
			print("vertices not in source")
			
		# dist is the distance between current vertex in vertices set
		dist = {vertex: inf for vertex in self.vertices}
		# previous vertex in vertices set
		previous = {vertex: None for vertex in self.vertices}
		dist[source] = 0
		queue = self.vertices.copy()
		neighbours = {vertex: set() for vertex in self.vertices}
		for start, end, cost in self.edges:
			# go through graph and check edges start, end and cost
			neighbours[start].add((end, cost))
		# pp(neighbours)
		
		while queue:
			# unreached queue set to vertex distances
			
			u = min(queue, key=lambda vertex: dist[vertex])
			queue.remove(u)
			# if graph traversed then break
			if dist[u] == inf or u == dest:
				break
			for v, cost in neighbours[u]:
				alt = dist[u] + cost
				if alt < dist[v]:  # Relax (u,v,a)
					dist[v] = alt
					previous[v] = u
		pp(previous)
		s, u = deque(), dest
		while previous[u]:
			s.appendleft(u)
			u = previous[u]
		s.appendleft(u)
		return s

com = ','
graph = Graph(open('tinyEWD.txt',mode='r',))
#graph = [int(e) if e.isdigit() else e for e in Graph.split(',')]
'''
Graph([("a", "b", 7),
                ("a", "c", 9),
                ("a", "f", 14),
                ("b", "c", 10),
                ("b", "d", 15),
                ("c", "d", 11),
                ("c", "f", 2),
                ("d", "e", 6),
                ("e", "f", 9)])
'''
pp(graph.dijkstra("10", "608"))