import random

def createGraph(n):
    #For randomly generated edge weights
    graph = {}
    for node in range(n):
       graph[node] = []
    return graph

def createConn2(graph):
    #For randomly generated edge weights
    nodeCounter = 0
    while (nodeCounter < len(graph)):
        j = nodeCounter + 1
        while j < len(graph):
            x = random.random()
            graph[nodeCounter].append([j, x])
            graph[j].append([nodeCounter, x])
            j += 1
        nodeCounter += 1
    return graph

def createGraphDistance(n):
    #For graph and plane
    graph = {}
    for node in range(n):
       graph[node] = []
    return graph
        
def createConnDistance(graph):
    #For graph and plane
    nodeCounter = 0
    while (nodeCounter < len(graph)):
        j = nodeCounter + 1
        while j < len(graph):
            x = random.random()
            y = random.random()
            distance = 
            graph[nodeCounter].append([j, x])
            graph[j].append([nodeCounter, x])
            j += 1
        nodeCounter += 1
    return graph

