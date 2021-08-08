from itertools import permutations, groupby, combinations
from math import floor

class Graph :

    def __init__(self, edges, directed=False): # Espera => edges = [('A', 'B'), ('B', 'C'), ('A','C')]
        self.directed = directed
        self.neighbors = {}
        self.add_edges(edges)

    def add_edges(self, edges): #Adiciona as arestas em forma de dicionario de listas  
        for x, y, in edges:
            self.neighbors.setdefault(x, []).append(y)
            if self.directed:
                self.neighbors.setdefault(y, [])
            else:
                self.neighbors.setdefault(y, []).append(x)

    def get_edges(self): #Devolve todas as arestas do grafo
        edges = []
        for key in self.neighbors.keys():
            for value in self.neighbors[key]:
                edges.append((key, value))
        return edges

    def get_vertices(self): #Devolve todos os vertices
        return list(self.neighbors.keys())

    def egde_exists(self, edge:tuple): #Devolve se uma aresta existe no grafo ou não
        return edge[0] in self.neighbors and edge[1] in self.neighbors[edge[0]]

def topological_ordering(graph):

  visited = {key:False for key in graph.get_vertices()}  
  time = 0
  topological_order = []

  def sub_rec_dfs(graph, vertex):
    nonlocal time
    visited[vertex] = True
    for neighbor in graph.neighbors[vertex]:
      if not visited[neighbor]:
        sub_rec_dfs(graph, neighbor)
    time += 1
    topological_order.append(vertex)

  for vertex in graph.get_vertices():
    if not visited[vertex]:
      sub_rec_dfs(graph, vertex)

  #print(f'Ordem topologica: {topological_order[::-1]}')
  return topological_order[::-1]


# main ->

starting_edges = [
  ('a','b'),
  ('a','d')
]

commom_edges = [
  ('b','c'),
  ('c','f'),
  ('d','e'),
  ('e','f')
]

result = []

grafo = Graph(edges=starting_edges, directed=True)

perms_starting = list(permutations(starting_edges))

perms_commom = list(permutations(commom_edges))

for i in perms_starting:

  for x in perms_commom:
    grafo = Graph(edges = list(i) + list(x), directed=True)
    result.append(topological_ordering(grafo))

result.sort()

result = list(result for result,_ in groupby(result))

print('Resultado gerado pelo algoritmo de ordenação topológica:')

for res in result:
  print(res)

print('Resultado gerado via permutação:')

start = 1
stop = len(commom_edges)+1

for z in list(permutations(result[0][start:stop])):
  sub = list(combinations(z, 2))
  score = 0
  for x in sub:
    if grafo.egde_exists(x):
      score+=1
  if score >=floor((stop-start)/2):
    print([result[0][0]]+list(z)+[result[0][-1]])

