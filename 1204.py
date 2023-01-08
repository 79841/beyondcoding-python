import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
graph = list([0]*(b+1) for i in range(a+1))
t = []
for i in range(c):
    x,y = map(int,input().split())
    graph[x][y] = 1
    t.append([x,y])

print(graph)
k = []
k_1 = 0
s = [0]
visited = []
queue = []
xd = [1,-1,0,0]
yd = [0,0,1,-1]
print(t)
for j in t:

    queue.append(j)
    if queue[0] in visited:
        continue
    while queue:
        x,y = queue.pop(0)
        visited.append([x,y])
        for i in range(4):
            nx = x+xd[i]
            ny = y+yd[i]

            if nx < 1 or ny < 1 or nx > a-1 or ny > b-1:
                continue

            if graph[nx][ny] != 1:
                continue


            k_1 += 1
            graph[nx][ny] = 0
            visited.append([nx,ny])
            queue.append([nx,ny])

            # if sum(k) == c:
            #     break
            # s.append(graph[nx][ny])

        k.append(k_1)
        k_1 = 0
        # s.clear()
        # s.append(0)


print(graph)
print(k)
print(k_1)