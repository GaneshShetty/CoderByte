# reference https://www.python.org/doc/essays/graphs/


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['E'],
         'E': ['F'],
         'F': ['C']}



def find_path(graph,start,end,path=[]):
    path=path+[start]

    if start==end:
        return path

    if not graph.has_key(start):
        return None

    for edge in graph[start]:
        if edge not in path:
            newpath=find_path(graph,edge,end,path)
            if newpath:
                return newpath

    return



a=[0]

print a + [1]
print a.append([1])



def find_All_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return [path]
    if not graph.has_key(start):
        return []
    paths=[]
    for edge in graph[start]:
        if edge not in path:
             newpath=find_All_path(graph,edge,end,path)
             paths=paths+ newpath
    return paths



def find_shortest_path(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path

    if not graph.has_key(start):
        return []

    shortest=None

    for node in graph[start]:
        if node not in path:
            newpath=find_shortest_path(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest=newpath

    return shortest








print find_path(graph,'A','E')
print find_All_path(graph,'A','D')
print find_shortest_path(graph,'A','D')