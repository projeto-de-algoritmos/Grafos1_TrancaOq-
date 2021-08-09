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

    def egde_exists(self, edge:tuple): #Devolse se uma aresta existe no grafo ou não
        return edge[0] in self.neighbors and edge[1] in self.neighbors[edge[0]]




def rec_dfs(graph, vertex):
   
    visited = {key:False for key in graph.get_vertices()}
    
    def DFS(graph, vertex, parent):

        visited[vertex] = True

        for neighbor in graph.neighbors[vertex]:
    
            if not visited[neighbor]:
                if DFS(graph, neighbor, vertex):
                    return True
    
            # SACADA: SE O VIZINHO JA FOI VISITADO MAS NÃO É SEU PAI (não está voltando), ENTÃO EXISTE UM CICLO AQUI
            elif neighbor != parent:
                return True
  
        return False
        
    if DFS(graph, vertex, 'aaa'):
      print("Ciclo encontado")
    else:
      print("Nenhum ciclo encontrado")




grafo  = Graph(edges=[
  ('A','B'),
  ('B','C'),
  ('C','D'),
  ('D','E')
#  ,('E', 'A') #comentar ou descomentar esta aresta para tornar o grafo aciclico ou ciclico
])

rec_dfs(grafo, vertex='A')