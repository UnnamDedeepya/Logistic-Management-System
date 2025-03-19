import pandas as pd
import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    # Example graph representation
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)
    print(f"Distances from {start_vertex}: {distances}")
