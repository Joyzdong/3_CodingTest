from collections import deque

def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visited = {start_v:True}
    while q:
        cur_v = q.popleft()
        print(cur_v, end=' - ')
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True


visited = {}
def dfs(graph, start_v):
    visited[start_v] = True
    print(start_v, end=' - ')

    for v in graph[start_v]:
        if v not in visited:
            dfs(graph, v)


graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

print('BFS: ', end='')
bfs(graph, start_v=0)
print()

print('DFS: ', end='')
dfs(graph, start_v=0)