def count_ice_squares(N, M, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[0]*M for _ in range(N)]
    counted = [[0]*M for _ in range(N)]
 
    def dfs(i, j):
        count = 0
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if not counted[i][j]:
                count += 1
                counted[i][j] = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                while 0 <= x < N and 0 <= y < M and grid[x][y] != '#':
                    if not counted[x][y]:
                        count += 1
                        counted[x][y] = 1
                    x, y = x + dx, y + dy
                x, y = x - dx, y - dy
                if not visited[x][y]:
                    stack.append((x, y))
        return count
 
    start_i, start_j = None, None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                start_i, start_j = i, j
                break
        if start_i is not None:
            break
 
    return dfs(start_i, start_j)
 
N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = input()
    grid.append(row)
print(count_ice_squares(N, M, grid))
def count_ice_squares(N, M, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[0]*M for _ in range(N)]
    counted = [[0]*M for _ in range(N)]

    def dfs(i, j):
        count = 0
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if not counted[i][j]:
                count += 1
                counted[i][j] = 1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                while 0 <= x < N and 0 <= y < M and grid[x][y] != '#':
                    if not counted[x][y]:
                        count += 1
                        counted[x][y] = 1
                    x, y = x + dx, y + dy
                x, y = x - dx, y - dy
                if not visited[x][y]:
                    stack.append((x, y))
        return count

    start_i, start_j = None, None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                start_i, start_j = i, j
                break
        if start_i is not None:
            break

    return dfs(start_i, start_j)

N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = input()
    grid.append(row)
print(count_ice_squares(N, M, grid))
