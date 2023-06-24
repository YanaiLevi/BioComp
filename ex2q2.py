import itertools
from tqdm import tqdm
import networkx as nx


# count all the motifs in a graph of size n
def countMotifs(graph, size):
    allMotifs = []
    motifCount = 0
    for i in tqdm(range(size-1, size*(size-1)+1)):
        curMotifs = []  # tuple that contains graphs and their motifs count
        combinations = [list(x) for x in itertools.combinations(graph.edges(), i)]  # all edges combinations
        for combination in combinations:
            curGraph = nx.DiGraph()
            curGraph.add_edges_from(combination)
            if len(curGraph.nodes) != size:
                continue
            if not nx.is_connected(curGraph.to_undirected()):
                continue
            is_isomorphic = any(nx.is_isomorphic(contender[0], curGraph) for contender in curMotifs)
            if is_isomorphic:
                for j, contender in enumerate(curMotifs):
                    if nx.is_isomorphic(contender[0], curGraph):
                        temp = list(curMotifs[j])
                        temp[1] += 1
                        curMotifs[j] = tuple(temp)
                        break
            else:
                curMotifs.append((curGraph, 1))
                motifCount += 1
        allMotifs.append(curMotifs)

    return allMotifs, motifCount

# print graph edges
def printMotifs(edges):
    strToPrint = ""
    for edge in edges:
        strToPrint += f"{edge[0]} {edge[1]}\n"
    return strToPrint


def printToTerminal(motifs, count):
    strToPrint = ""
    i = 1
    strToPrint += f"count={count}\n"
    strToPrint += f"total motifs={count}\n"
    for lst in motifs:
        for motif in lst:
            strToPrint += f"#{i}\n"
            strToPrint += f"count={motif[1]}\n"
            i += 1
            strToPrint += printMotifs(motif[0].edges)
    print(strToPrint)


# parse the graph and start the program
def parseAndStart(graph_str, n):
    edges_str_arr = graph_str.split("\n")
    new_edges = [(int(edge.split(" ")[0]), int(edge.split(" ")[1])) for edge in edges_str_arr if edge]
    # create a graph
    g = nx.DiGraph()
    g.add_edges_from(new_edges)
    # count motifs
    motifs, count = countMotifs(g, n)
    # print to terminal
    printToTerminal(motifs, count)



if __name__ == "__main__":
    # get n from user
    n = int(input("Enter the value of n: "))
    # get graph from file
    with open("input.txt", "r") as file:
        graph_str = file.read()
    # parse and start
    parseAndStart(graph_str, n)


