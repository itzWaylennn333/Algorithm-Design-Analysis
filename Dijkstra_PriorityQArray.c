#include <stdio.h>
#include <limits.h>

#define V 6

void insertInOrder(int queue[], int d[], int *queueSize, int v) {
    int i;
    for (i = *queueSize - 1; (i >= 0 && d[queue[i]] > d[v]); i--) {
        queue[i + 1] = queue[i]; 
    }
    queue[i + 1] = v;
    (*queueSize)++;
}


int extractMin(int queue[], int *queueSize) {
    if (*queueSize == 0) {
        return -1;
    }
    
    int minVertex = queue[0];
    for (int i = 0; i < (*queueSize) - 1; i++) {
        queue[i] = queue[i + 1];
    }
    (*queueSize)--;
    return minVertex;
}

void Dijkstra_ShortestPath(int graph[V][V], int source) {
    int d[V];
    int pi[V];
    int S[V];
    int queue[V];
    int queueSize = 0;

    for (int v = 0; v < V; v++) {
        d[v] = INT_MAX;
        pi[v] = -1;
        S[v] = 0;
    }
    d[source] = 0;

    for (int v = 0; v < V; v++) {
        insertInOrder(queue, d, &queueSize, v);
    }

    while (queueSize > 0) {
        int u = extractMin(queue, &queueSize);
        
        if (u == -1) break;

        S[u] = 1;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] != 0 && !S[v]) {
                if (d[v] > d[u] + graph[u][v]) {
                    d[v] = d[u] + graph[u][v];
                    pi[v] = u;

                    for (int i = 0; i < queueSize; i++) {
                        if (queue[i] == v) {
                            for (int j = i; j < queueSize - 1; j++) {
                                queue[j] = queue[j + 1];
                            }
                            queueSize--;
                            break;
                        }
                    }
                    insertInOrder(queue, d, &queueSize, v);
                }
            }
        }
    }

    printf("Vertex\tDistance from Source\n");
    for (int i = 0; i < V; i++) {
        printf("%d\t\t%d\n", i + 1, d[i]);
    }
}

int main() {
    int graph[V][V] = {
        {0, 2, 0, 4, 3, 0}, 
        {0, 0, 5, 0, 0, 0},
        {0, 0, 0, 0, 0, 4}, 
        {0, 0, 0, 0, 2, 0},
        {0, 0, 1, 0, 0, 3}, 
        {0, 0, 0, 0, 0, 0}
    };

    int startVertex = 0;
    
    Dijkstra_ShortestPath(graph, startVertex);

    return 0;
}
