import random

def createGraph(n):
    graph = {}
    for node in range(n):
       graph[node] = []
    return graph

def createConnections(graph):
    for node in graph:
        i = node
        while i < len(graph):
            graph[i].append([i + 1, random.random()])
            i += 1
    return graph

def createConn2(graph):
    nodeCounter = 0
    while (nodeCounter < len(graph)):
        j = nodeCounter + 1
        while j < len(graph):
            x = round(random.random(), 1)
            graph[nodeCounter].append([j, x])
            graph[j].append([nodeCounter, x])
            j += 1
        nodeCounter += 1
    return graph
        
