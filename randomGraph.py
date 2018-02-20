import random

def createGraph(n):
    for node in range(n):
        graph = {}
        graph[node] = [[]]
        for elem in graph:
