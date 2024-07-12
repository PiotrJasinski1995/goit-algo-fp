import heapq


def dijkstra(graph, start):
    # Initialize distances and the set of unvisited vertices
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # priority queue to store vertices that are being preprocessed
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        _, u = heapq.heappop(pq)
        # vertex
        for v, weight in graph[u].items():
            # If there is shorted path to v through u.
            if distances[v] > distances[u] + weight:
                # Updating distance of v
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))

    return distances


# An example of a graph in the form of a dictionary
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Calling the function for vertex A
print(dijkstra(graph, 'A'))
