# Graphs consist of vertecies and edges.  Edges connect verticies.  Graphs are
# similar to trees, but graphs can have loops and verticies that are not connected,
# trees can not.  Verticies that are connected are said to be adjacent.  A graph
# where every vertex is connected somehow are called connected graphs.


# DFS (depth first search) and BFS (breadth first search) are searching techniques.
# O(V+E) speed V=vertecies E=edges


import random

class vertex:
    user_id = 0

    def __init__(self, value):
        # sequential ids
        self.id = vertex.user_id
        # incriment id tracker
        vertex.user_id += 1
        self.adjacent = {}
        self.meta={}

    # add an connection between two vertecies.
    def add_adjacent(self, vertex_to_add=None):
        # ensure correct type being added.
        if type(vertex_to_add) is not vertex:
            return
        # ensure not already added.
        if not self.adjacent.get(vertex_to_add.id):
            self.adjacent[vertex_to_add.id] = vertex_to_add

    # add connection to and from two verecies.
    def add_adjacent_mutual(self, vertex_to_add=None):
        self.add_adjacent(vertex_to_add)
        vertex_to_add.add_adjacent(self)

# depth first search because if follows every verticies contact chain to the end
# before moving on to the next verticies contacts
def depth_first_search(vertex, visited=None):
    visited = {} if visited is None else visited
    visited[vertex.id] = True
    print(vertex.id)
    for key, edge in vertex.adjacent.items():
        if not visited.get(key):
            depth_first_search(edge, visited)

# bredth first search because it will add all adjacent verticies to a queue
# before moving deeper into the graph.
def breadth_first_search(vertex, visited=None, queue=None):
    visited = {} if visited is None else visited
    queue = [] if Queue is None else queue
    visited[vertex.id] = True
    queue.append(vertex)
    while queue:
        vertex = queue[0]
        del queue[0]
        print(vertex.id)
        for key, adj in vertex.adjacent:
            if not visited.get(key):
                visited[key] = True
                queue.append(adj)





if __name__ == "__main__":

    # build graph nodes
    max_verticies = 100
    verticies = {}
    for i in range(max_verticies):
        verticies[i] = vertex(i)

    # randomly make graph edges.
    for i in random.sample(range(1,max_verticies), max_verticies-1):
        number_of_edges = random.randint(1, max_verticies-1)
        for j in range(number_of_edges):
            adj = random.randint(1, max_verticies-1)
            verticies[i].add_adjacent(verticies[adj])

    print(f"vertex: {verticies[4].id}, adj: {verticies[4].adjacent}")

    depth_first_search(verticies[1])
