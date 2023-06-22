

import itertools
from collections import Counter

# a function that takes a list of edges and the number of nodes as arguments and returns a list of all the possible graphs with those edges and nodes
def removeOneEdgeRecursively(edges, n):
    
    # base case    
    if len(edges) == n-1:
        return [edges]
    
    # recursive case
    results = []
    for edge in edges:
        # copy the list
        copy = edges.copy()
        copy.remove(edge)
        # check if the graph is fully connected
        for i in range(n):
            flag = False
            for e in copy:
                if i in e:
                    flag = True
            if not flag:
                break
        if not flag:
            continue
        results.append(copy)
        # recursive call
        result = removeOneEdgeRecursively(copy, n)
        # add the result to results
        for i in result:
            if i not in results:
                results.append(i)
    return results
        
        
# a function that takes a list of edges and the number of nodes as arguments and returns a list of all the possible names of the nodes        
def differentNames(edges, n):
    permutations = list(itertools.permutations(list(range(n))))
    permutations = permutations[1:]
    result = []
    for i in permutations:
        newEdges = []
        for j in edges:
            newEdges.append((i[j[0]], i[j[1]]))
        result.append(newEdges)
    return result


# a function that takes two lists as arguments and returns True if they are equal and False otherwise          
def compare_lists(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    return counter1 == counter2    
    
        


# a function that takes an integer as an argument (representing the number of nodes) and prints the edges of all the possible connected (directed) graphs with that number of nodes
def print_all_graphs(n):
    combinations = []
    # print all the edges of all fully connected graphs with n nodes
    combination = []
    for i in range(n):
        for j in range(n):
            if i != j:
                combination.append((i, j))
    combinations.append(combination)
    
    # remove one edge recursively, and add the result to combinations if it is a fully connected graph
    result = removeOneEdgeRecursively(combination, n)
    
    for i in result:
        combinations.append(i)
     
    # remove duplicates
    combinations = list(set(tuple(sorted(sub)) for sub in combinations))   
    for i in combinations:
        for j in differentNames(i, n):
            for comb in combinations:
                if compare_lists(comb, j):
                    if comb != i:
                        combinations.remove(comb)
                
               
    # reorder combinations by length of the list
    combinations.sort(key=len)
            
    # print the result
    print("count =", len(combinations)) 
    for i in combinations:
        print("#"+str(combinations.index(i)+1))
        for j in i:
            print(j[0]+1, j[1]+1)
            
    
    
    
    
    
    




if __name__ == "__main__":
    # go over the range of 1 to 4
    for n in range(1, 5):
        # print the number of nodes
        print("n =", n)
        # print all the graphs with n nodes
        print_all_graphs(n)
    