def topsortorder(node,neighbour,visited,stack):
    visited[node] = True

    for i in neighbour[node]:
        if not visited[i]:
            topsort(i,neighbour,visited,stack)
        
        #pushing the leaf node into the stack
        stack.append(node)

def topsort(neighbour, node):
    stack = []

    visited = [False] * node
    for i in range(node):
        if not visited[i]:
            topsortorder(i,node,neighbour,visited,stack)

    print("topological sorting of the graph:", end = "")

    while stack:
        print(stack.pop(),end="")
    
    if __name__ == "__main__":
        #number of nodes
        node = 7

        #edges
        edges = [[A,B],[A,E],[B,D],[B,C],[C,G],[C,F],[D,A]]

        neighbour = [[] for _ in range(node)]

        for i in edges:
            neighbour[i[0]].append(i[1])
        
        topsort(neighbour,node)
