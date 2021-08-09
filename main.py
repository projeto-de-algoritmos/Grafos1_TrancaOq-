from pandas import read_csv 
from graphutils import Graph, get_dependents, get_dependencies

Df = read_csv('grade_software.csv').values.tolist()

edges = []

for lista in Df:
  lista[1] = eval(lista[1])
  for dependencie in lista[1]:
    edges.append((lista[0], dependencie))
    
grafo = Graph(edges = edges, directed = True)

target = 'Engenharia de Produto de Software'

result = get_dependents(grafo, target)

result2 = get_dependencies(grafo, target)

print(f'{target} tranca as seguintes matérias:\n{result[0]}\n e tem como pré requisitos as seguintes matérias:\n{result2}')
