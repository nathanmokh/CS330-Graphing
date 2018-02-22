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
       graph[node] = [random.randint(0,50), random.randint(0,50)]
    return graph
        
def createConnDistance(graph):
    #For graph and plane
    nodeCounter = 0
    while (nodeCounter < len(graph)):
        j = nodeCounter + 1
        while j < len(graph):
            x_i = (graph[nodeCounter])[0]
            y_i = (graph[nodeCounter])[1]
            x_j = (graph[j])[0]
            y_j = (graph[j])[1]
            x_dis = abs(x_i - x_j)**2
            y_dis = abs(y_i - y_j)**2
            distance = (x_dis + y_dis)**(0.5)
            #graph[nodeCounter].append([j, x])
            graph[nodeCounter].insert(0,j)
            graph[nodeCounter].insert(1,distance)
            graph[j].insert(0,nodeCounter)
            graph[j].insert(1,distance)            
            
            #graph[j].append([nodeCounter, x])
            j += 1
        nodeCounter += 1
    return graph

