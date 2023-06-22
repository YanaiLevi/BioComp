
from itertools import combinations

# a function that takes a list of edges and the number of nodes as arguments and returns a list of all the possible names of the nodes
def find_connected_subgraphs(edges):
    def dfs(node, graph, visited, subgraph):
        visited[node] = True
        subgraph.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, subgraph)

    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

    visited = {node: False for node in graph}
    connected_subgraphs = []

    for node in graph:
        if not visited[node]:
            subgraph = []
            dfs(node, graph, visited, subgraph)
            connected_subgraphs.append(subgraph)

    subgraph_edges = []
    for subgraph in connected_subgraphs:
        subgraph_edge_set = set()
        for node in subgraph:
            for neighbor in graph[node]:
                if neighbor in subgraph:
                    subgraph_edge_set.add((node, neighbor))
        subgraph_edges.extend(list(subgraph_edge_set))

    return [subgraph_edges[i:] for i in range(len(subgraph_edges))]

# get all the subgraphs with n nodes of a graph
def getAllSubGraphs(n, graph):
    vertices = set()
    edges = []
    
    # Parse the graph input
    for edge in graph.split(','):
        if edge.strip() == '':
            continue
        u, v = map(int, edge.strip().split())
        vertices.add(u)
        vertices.add(v)
        edges.append((u, v))
    
    # Generate all combinations of n vertices
    combinations_vertices = combinations(vertices, n)
    
    # Generate all subgraphs using the combinations of vertices
    subgraphs = []
    for comb in combinations_vertices:
        possible_subgraph_edges = []
        for edge in edges:
            if edge[0] in comb and edge[1] in comb:
                possible_subgraph_edges.append(edge)
        for subgraph_edges in find_connected_subgraphs(possible_subgraph_edges):
            subgraphs.append(subgraph_edges)
    
    return subgraphs

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    graph_input = input("Enter the graph edges: ")
    graph_input = "1 2,2 3,1 4,2 1"

    subgraphs = getAllSubGraphs(n, graph_input)

    # Output the subgraphs
    print("Subgraphs of size", n, ":")
    for subgraph in subgraphs:
        print(subgraph)

