class graphs:
    
    def __init__(self):
        self.graph = {}
        #since the graph is undirected graph
        self.directed = False
    #ADJACENCY LIST
    #adding verteces
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    #adding edges
    def addEdges(self,source,dest):
        self.addVertex(source)
        self.addVertex(dest)

        #if graph is directed
        self.graph[source].append(dest)

        #if undirected
        if not self.directed:
            self.graph[dest].append(source)
    
    #displaying the graph
    def displayGraph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    #BFS
    def bfs(self,startvertex):
        queue = [startvertex]
        visited = {startvertex: True}
        while queue:
            currentvertex = queue.pop()
            print(currentvertex, end=" ")

            for vertex in self.graph[currentvertex]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited[vertex] = True
    
    #DFS
    def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end= " ")
            visited.append(vertex)
            for v in self.graph[vertex]:
                self.dfs(v,visited)




#creating a graph

G = graphs()
G.addEdges('A','B')
G.addEdges('C','B')
G.addEdges('A','D')
G.addEdges('C','E')
G.addEdges('D','E')
G.addEdges('A','E')

#display graph
G.displayGraph()

#Breadth first search
G.bfs('A')

#Depth first search
G.dfs('A',[])


