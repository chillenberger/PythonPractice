# Graphs consist of vertecies and edges.  Edges connect verticies.  Graphs are
# similar to trees, but graphs can have loops and verticies that are not connected,
# trees can not.  Verticies that are connected are said to be adjacent.  A graph
# where every vertex is connected somehow are called connected graphs.


# DFS (depth first search) and BFS (breadth first search) are searching techniques.
# O(V+E) speed V=vertecies E=edges


import random

class vertex:
    user_id = 0

    def __init__(self, meta):
        # sequential ids
        self.id = vertex.user_id
        # incriment id tracker
        vertex.user_id += 1
        # container for connected edges
        self.adjacent = []
        # container for any data associated with this vertex
        self.meta=meta

    # add an connection between two vertecies.
    def add_adjacent(self, vertex_to_add=None):
        # ensure correct type being added.
        if type(vertex_to_add) is not vertex:
            return
        # ensure not already added.
        if vertex_to_add not in self.adjacent:
            self.adjacent.append(vertex_to_add)

    # add connection to and from two verecies.
    def add_adjacent_mutual(self, vertex_to_add=None):
        self.add_adjacent(vertex_to_add)
        vertex_to_add.add_adjacent(self)

class weighted_vertex:
    id = 0
    def __init__(self, meta):
        self.id = weighted_vertex.id
        weighted_vertex.id += 1
        self.adjacent = {}

    def add_adjacent(self, vertex_to_add=None, weight=0):
        if type(vertex_to_add) is not weighted_vertex:
            return
        if vertex_to_add not in self.adjacent:
            self.adjacent[vertex_to_add] = weight


# depth first search because if follows every verticies contact chain to the end
# before moving on to the next verticies contacts
def depth_first_search(vertex, visited=None):
    visited = {} if visited is None else visited
    visited[vertex.id] = True
    print(vertex.id)
    # if weighted graph adjacent in dicts
    if type(vertex.adjacent) is dict:
        for edge, weight in vertex.adjacent.items():
            if not visited.get(edge.id):
                depth_first_search(edge, visited)
    # if not weighted graph adjacent in list
    elif type(vertex.adjacent) is list:
        for edge in vertex.adjacent:
            if not visited.get(edge.id):
                depth_first_search(edge, visited)

# bredth first search because it will add all adjacent verticies to a queue
# before moving deeper into the graph.
def breadth_first_search(vertex, visited=None, queue=None):
    visited = {} if visited is None else visited
    queue = [] if queue is None else queue
    visited[vertex.id] = True
    queue.append(vertex)
    while queue:
        vertex = queue[0]
        del queue[0]
        print(vertex.id)
        if type(vertex.adjacent) is dict:
            for adj, weight in vertex.adjacent.items():
                if not visited.get(adj.id):
                    visited[adj.id] = True
                    queue.append(adj)
        elif type(vertex.adjacent) is list:
            for adj in vertex.adjacent:
                if not visited.get(adj.id):
                    visited[adj.id] = True
                    queue.append(adj)

# one solution to minimum length problem.
def dijkstra_alogorithm(start, end):
    if type(start) is not weighted_vertex:
        return
    if type(end) is not weighted_vertex:
        return
    # make our current vertex the start vertex
    current = start
    # track min weight from start vertex to all other vertecies
    cheapest = {}
    # track min previous vertex weight
    previous_city = {}
    # track visited verticies
    visited = {}
    # track discovered vertiecies we have not visited.
    unvisited = {}
    # set weight to current at zero
    cheapest[current] = 0
    while current:
        # add current vertex to visited
        visited[current] = True
        # if current in unvisited, we must remove it
        if unvisited.get(current):
            del unvisited[current]
        # iterate through all adjacent vertices
        for vertex, weight in current.adjacent.items():
            # if newly discovered vertex we havent been to, add to unvisited
            if not unvisited.get(vertex) and not visited.get(vertex):
                unvisited[vertex] = True
            # calculate total weigh to get to adjacent vertex from start vertex
            total_weight = cheapest[current] + weight
            # if lower weight than other path in cheapest,
            if not cheapest.get(vertex) or total_weight < cheapest[vertex]:
                # replace cheapest value
                cheapest[vertex] = total_weight
                # track previous verticie
                previous_city[vertex] = current
        # find min weight of unvisited vertices and make that next vertice
        min = None
        next = None
        for key in unvisited.keys():
            if min is None or cheapest.get(key) < min:
                min = cheapest[key]
                next = key
        current = next

    # iterate through previous to get path
    path = []
    current = end
    while current is not start:
        path.append(current.id)
        current = previous_city[current]

    path.append(start.id)
    # reverse path to get correct order from start to finish 
    path.reverse()
    return path, cheapest[end]

# make graph for testing
def make_graph(size, weighted=False):
    # build graph nodes
    max_verticies = size
    verticies = {}
    for i in range(max_verticies):
        verticies[i] = weighted_vertex(i) if weighted else vertex(i)

    # randomly make graph edges.
    for i in random.sample(range(1,max_verticies), max_verticies-1):
        number_of_edges = random.randint(1, max_verticies-1)
        for j in range(number_of_edges):
            adj = random.randint(1, max_verticies-1)
            if weighted:
                verticies[i].add_adjacent(verticies[adj], random.randint(1, 100))
            else:
                verticies[i].add_adjacent(verticies[adj])
    return verticies


if __name__ == "__main__":

    verticies = make_graph(size=100, weighted=True)
    print(f"vertex: {verticies[4].id}, adj: {verticies[4].adjacent}")
    # depth_first_search(verticies[1])
    # print("*****")
    # breadth_first_search(verticies[1])

    path, price = dijkstra_alogorithm(verticies[3], verticies[54])
    print(f"path: {path}, price: {price}")

    # a = weighted_vertex(1)
    # b = weighted_vertex(2)
    # c = weighted_vertex(3)
    # d = weighted_vertex(4)
    #
    # a.add_adjacent(b, 2)
    # b.add_adjacent(c, 3)
    # a.add_adjacent(c, 2)
    # b.add_adjacent(d, 1)
    # c.add_adjacent(d, 2)
    #
    # path, price = dijkstra_alogorithm(a, d)
    # print(f"path: {path}, price: {price}")
