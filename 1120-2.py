import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for i in range(N)]

queue = [[0,0]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    y, x = queue.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
            continue
            
        if maze[ny][nx] != 1:
            continue

        maze[ny][nx] = maze[y][x] + 1
        queue.append([ny, nx])

print(maze[-1][-1])