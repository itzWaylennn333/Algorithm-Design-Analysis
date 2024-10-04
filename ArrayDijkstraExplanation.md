### Explanation

- Priority Queue:
The priority queue is stored as a simple array (priority_queue), and at each step, the vertex with the minimum distance is extracted by scanning the entire queue linearly.

- Main loop:
The algorithm loops until the priority queue is empty (queue_size > 0).
In each iteration, it scans the entire priority queue to find the vertex 
𝑢 with the smallest known distance that hasn’t been visited yet. This is done with a linear search (which takes O(V)).

Once vertex 𝑢 is found, it is removed from the priority queue by swapping it with the last element and reducing the queue size by 1.

The distances of all adjacent vertices v of u are then updated. This step checks if the current known path to v can be shortened by traveling through u. If so, the distance[v] is updated.

### Theoretical Time Complexity

- Time to extract the minimum vertex:
In each iteration of the main loop, the algorithm performs a linear search over the priority queue to find the vertex with the smallest distance, which takes O(V) time.

- Time to relax adjacent vertices:
For each vertex u, the algorithm checks all V vertices to see if they are adjacent and updates their distances if needed. This takes O(V) time per vertex.

### Empirical Time Complexity

The growth is relatively smooth and follows an expected pattern based on Dijkstra's time complexity, which is O(V^2) for the basic implementation. As the number of vertices increases, the number of edges grows proportionally due to the fixed edge density

![alt text](https://github.com/zImmortal333/Algorithm-Design-Analysis/blob/main/Images/TimeComplexityofArrayDijkstra_wrt_V_E.png)

# Comparison between Heap and Basic

### (a) Basic Array-Based Implementation

Approach: This version of Dijkstra’s algorithm uses an array to represent a priority queue. It finds the vertex with the smallest distance by scanning through the entire list of vertices at each step.

Time Complexity: O(V^2), where 𝑉 is the number of vertices. This is because finding the minimum distance vertex takes O(V) time and the algorithm performs this search for each of the 𝑉 vertices.

Space Complexity: O(V), as it maintains arrays for distance and visited vertices.

Pros:
- Simple and easy to implement.
- Works well for small graphs where the number of vertices is relatively low.

Cons:
- Inefficient for large graphs due to the 
O(V^2) time complexity, as scanning through all vertices repeatedly is computationally expensive.


### (b) Heap-Based Implementation Using Min-Heap (Priority Queue)

Approach: This version uses a min-heap (priority queue) to efficiently find the vertex with the smallest distance. It uses the heapq module in Python for this purpose and represents the graph as an adjacency list.

Time Complexity: O((V+E)logV), where V is the number of vertices and E is the number of edges. Extracting the minimum distance vertex and updating distances using the heap takes O(logV), which is more efficient than scanning an array.

Space Complexity: O(V+E), as it stores the adjacency list and uses the heap for priority queue management.

Pros:
- Much faster for large graphs, especially sparse graphs where the number of edges is much smaller than O(V^2)
- More scalable due to the heap-based optimization.

Cons:
- Slightly more complex to implement compared to the basic array version.

## Comparison and Recommendation (Conclusion)
For *small graphs* (few vertices): The array-based implementation (a) is sufficient and may even be preferable due to its simplicity.
For *large graphs* (many vertices and edges): The heap-based implementation (b) is superior. It handles both large and sparse graphs efficiently, reducing the time complexity to O((V+E)logV), which is significantly better than O(V^2) for dense or large graphs.

### Theoretical
![alt text](https://github.com/zImmortal333/Algorithm-Design-Analysis/blob/main/Images/TheoreticalDijkstraTimeComplexity.gif)

### Empirical
![alt text](https://github.com/zImmortal333/Algorithm-Design-Analysis/blob/main/Images/TimeComplexityofComparison_Basic_Heap.png)

### *Notice how Basic Dijkstra in BLUE is slightly above Heap Dijkstra in RED*
