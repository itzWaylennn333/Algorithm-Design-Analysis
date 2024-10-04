import heapq

def dijkstra(graph, source):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize distances to all vertices as infinity
    dist = {}
    for i in range(V):
        dist[i] = float('inf')  # Infinite distance initially
    
    dist[source] = 0  # Distance to the source is 0
    
    # Previous node array (to store shortest path tree)
    prev = {}
    for i in range(V):
        prev[i] = None  # No predecessors initially
    
    # Set of vertices for which the shortest distance is already found
    S = {}
    for i in range(V):
        S[i] = 0  # All vertices are initially unvisited
    
    # Priority queue (min-heap) initialized with the source node
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))  # (distance, vertex)
    
    while priority_queue:
        # Extract the vertex with the minimum distance
        current_dist, u = heapq.heappop(priority_queue)
        
        # If this vertex has already been visited, skip it
        if S[u] == 1:
            continue
        
        # Mark u as visited (add to S)
        S[u] = 1
        
        # For each neighbor v of u
        for neighbor in graph[u]:
            v = neighbor[0]  # The neighboring vertex
            weight = neighbor[1]  # The edge weight
            
            # Relaxation: check if a shorter path is found
            if S[v] == 0 and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight  # Update distance
                prev[v] = u  # Update predecessor
                
                # Insert v into the priority queue
                heapq.heappush(priority_queue, (dist[v], v))
    
    return dist, prev

# Example graph represented as an adjacency list
graph = {
    0: [(1, 2), (3, 4), (4, 3)],   # edges from vertex 0 to others
    1: [(2, 5)],                   # edges from vertex 1 to others
    2: [(5, 4)],                   # edges from vertex 2 to others
    3: [(4, 2)],                   # edges from vertex 3 to others
    4: [(2, 1), (5, 3)],           # edges from vertex 4 to others
    5: []                          # vertex 5 has no outgoing edges
}

# Define the source vertex
source = 0
distances, predecessors = dijkstra(graph, source)

# Print the shortest distances from the source
print("Vertex\tDistance from Source")
for vertex in range(len(graph)):
    print(f"{vertex}\t{distances[vertex]}")
