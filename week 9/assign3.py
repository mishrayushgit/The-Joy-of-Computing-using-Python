def no_of_edges(nodes):
    return (nodes*(nodes-1))//2
nodes = int(input())
print(no_of_edges(nodes))