import sys

V = 6  # Number of vertices

def dijkstra(graph, start_vertex):
    # Initialize distance and visited arrays
    distance = [sys.maxsize] * V
    visited = [False] * V

    # Distance to the source vertex is 0
    distance[start_vertex] = 0

    # Initialize the priority queue with all vertices
    priority_queue = list(range(V))  # Queue contains [0, 1, 2, ..., V-1]
    queue_size = V

    while queue_size > 0:
        # Find the vertex with the smallest distance in the priority queue
        min_distance = sys.maxsize
        min_index = -1

        for i in range(queue_size):
            vertex = priority_queue[i]
            if not visited[vertex] and distance[vertex] < min_distance:
                min_distance = distance[vertex]
                min_index = i

        # If no vertex found, break
        if min_index == -1:
            break

        # Extract the vertex with the smallest distance
        u = priority_queue[min_index]
        priority_queue[min_index] = priority_queue[queue_size - 1]  # Remove u from queue
        queue_size -= 1

        # Mark the vertex as visited
        visited[u] = True

        # Update distances of the adjacent vertices of u
        for v in range(V):
            if not visited[v] and graph[u][v] != 0 and distance[u] != sys.maxsize:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    # Print the result
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i+1}\t{distance[i]}")

# Test the code with the given graph
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 4, 3, 0],
        [0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 1, 0, 0, 3],
        [0, 0, 0, 0, 0, 0]
    ]
    
    start_vertex = 0
    dijkstra(graph, start_vertex)
