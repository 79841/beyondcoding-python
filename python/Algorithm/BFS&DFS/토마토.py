from collections import deque

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
            continue

        if matrix[ny][nx] != 0:
            continue

        matrix[ny][nx] = matrix[y][x] + 1
        queue.append([ny, nx])

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)