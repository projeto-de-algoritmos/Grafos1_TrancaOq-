class Vertex:
    def __init__(self, name, gender, wiki, realm):
        self.name = name
        self.gender = gender
        self.realm = realm
        self.wiki = wiki
        self.adjacent = {}

    def add_neighbor(self, neighbor, kinship):
        self.adjacent[neighbor] = kinship

    def get_connections(self):
        return self.adjacent.keys()

    def get_name(self):
        return self.name

    def get_data(self):
        return self.name, self.gender, self.wiki, self.realm

    def get_kinship(self, neighbor):
        return self.adjacent[neighbor]

    def __str__(self):
        return f"{self.get_name()} -> {[x.get_name() for x in self.adjacent]}"

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vert = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, name, gender, wiki, realm):
        self.num_vert += 1
        new_vertex = Vertex(name,gender,wiki,realm)
        self.vert_dict[name] = new_vertex
        return new_vertex

    def get_vertex(self, name):
        if name in self.vert_dict:
            return self.vert_dict[name]
        else:
            return None

    def add_edge(self, frm, to, kinship):
        if frm not in self.vert_dict:
            return None
        if to not in self.vert_dict:
            return None
        self.vert_dict[frm].add_neighbor(self.vert_dict[to],kinship)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm],kinship)

    def get_vertices(self):
        return list(self.vert_dict.keys())

