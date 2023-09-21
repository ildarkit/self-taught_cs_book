import heapq


def dijkstra(graph, start):
    path = {}
    dist = {v: float('infinity') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while len(pq) > 0:
        current_dist, current = heapq.heappop(pq)
        if current_dist > dist[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                path[neighbor] = current
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return path


def short_path(graph, start, end):
    short_path = []
    path = dijkstra(graph, start)
    current = end
    
    while current != start:
        short_path.append(current)
        current = path[current]
    short_path.append(current)

    short_path.reverse()
    return short_path


if __name__ == '__main__':
    graph = {
        'A': {'B': 2, 'C': 6},
        'B': {'A': 2, 'D': 5},
        'D': {'B': 5, 'C': 8},
        'C': {'A': 6, 'D': 8}}
    start = 'A'
    end = 'D'
    path = short_path(graph, start, end)
    assert path == ['A', 'B', 'D']


