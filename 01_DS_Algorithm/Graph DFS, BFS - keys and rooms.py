from collections import deque

def bfs(rooms, key):
    q = deque()
    q.append(key)
    visited = {key:True}
    while q:
        cur_room = q.popleft()
        for key in rooms[cur_room]:
            if key not in visited:
                q.append(key)
                visited[key] = True
    return len(visited) == len(rooms)


visited = {}
def dfs(graph, start_v):
    visited[start_v] = True
    print(start_v, end=' - ')

    for v in graph[start_v]:
        if v not in visited:
            dfs(graph, v)


rooms = [[1],[2],[3],[]]

result = bfs(rooms, 0)
# print(dfs(rooms, 0))

print(result)