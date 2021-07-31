from graph import Vertex, Graph

g = Graph()
g.add_vertex('Drogo','Male','Primula','-','Condado')
g.add_vertex('Primula','Female','Drogo','-','Condado')
g.add_vertex('Frodo','Male','-','-','Condado')
g.add_vertex('Sam','Male','-','-','Condado')
g.add_vertex('Bilbo','Male','-','-','Condado')
g.add_edge('Drogo','Primula','Esposo(a)')
g.add_edge('Drogo','Frodo','Pai')
g.add_edge('Primula','Frodo','Mae')
print(g.get_vertices())
print(g.get_vertex('Drogo'))

hobbit = g.get_vertex('Drogo')
for i in hobbit.get_connections():
    print(hobbit.get_kinship(i))
