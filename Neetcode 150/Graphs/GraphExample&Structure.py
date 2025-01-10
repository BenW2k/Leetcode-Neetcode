# Array of Edges (Directed)

n = 8
A = [[0, 1], [1, 2] ,[0, 3], [3, 4], [3, 6], [3, 7], [4, 2] [4, 5], [5, 2]]

# Convert Array of Edges to adjacency Matrix

M = []
for i in range(n):
    M.append([0]*n)

for u, v in A:
    M[u][v] = 1
    # If the graph is undirected uncomment the line below
    # M[v][u] = 1


# Convert Array of Edges -> Adjacency List

from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    # uncomment for undirected
    # D[v].append(u)

# DFS with Recursion O(v + e) where v is num of nodes and e is num of edges

def dfs_recursive(node):
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursive(neighbour_node)
source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

# Iterative DFS with stack - O(v+e)

source = 0
seen = set()
seen.add(source)
stack = [source]
while stack:
    node = stack.pop()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            stack.append(neighbour_node)

# BFS with Queue O(v+e)

from collections import deque

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            q.append(neighbour_node)

# class based approach
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __str__(self):
        return f'Node({self.value})'
    def display(self):
        connections = [node.value for node in self.neighbours]
        return f'{self.value} is connected to: {connections}'



