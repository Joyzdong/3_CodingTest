from collections import deque

def isvalid(r, c):
    return 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and not visited[r][c]

def bfs(r, c):
    if not isvalid(r, c):
        return

    q = deque([(r, c)])
    while q:
        cur_r, cur_c = q.popleft()
        visited[cur_r][cur_c] = True
        for dr, dc in directions:
            if isvalid(cur_r + dr, cur_c + dc):
                q.append((cur_r + dr, cur_c + dc))

def dfs(r, c):
    if not isvalid(r, c):
        return

    visited[r][c] = True
    for dr, dc in directions:
        dfs(r + dr, c + dc)

grid = [             # implicit graph (암시적 그래프)
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
m, n = len(grid), len(grid[0])
visited = [[False] * n for _ in range(m)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dfs(0, 0)
for row in visited:
    print(row)


