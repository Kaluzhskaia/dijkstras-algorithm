graph = [
    {1: 7, 2: 9, 5: 14},
    {0: 7, 2: 10, 3: 15},
    {0: 9, 1: 10, 5: 2, 3: 11},
    {1: 15, 2: 11, 4: 6},
    {3: 6, 5: 9},
    {0: 14, 2: 2, 4: 9}
]


def dijkstra(graph, start_node):
    #some unreachable value
    inf = 999
    distances = [inf] * len(graph)
    distances[start_node] = 0
    #to track where we've been already
    visited = [False] * len(graph)
    cur_node = start_node
    #while there are unvisited nodes
    while False in visited:
        visited[cur_node] = True
        #sort our adjoining nodes by minimal value
        adj = sorted(graph[cur_node].items(), key=lambda x: x[1])
        for key, value in adj:
            if distances[cur_node] + value < distances[key]:
                distances[key] = distances[cur_node] + value
        min_ind = inf
        #finding the next node with minimal travel distance from start node
        for i in range(0, len(distances)):
            if not visited[i] and distances[i] < min_ind:
                min_ind = distances[i]
                cur_node = i
    return distances

print("Please input node:")
node = input()
print("Minimal distances from node ", node, " are: ", dijkstra(graph, int(node)))