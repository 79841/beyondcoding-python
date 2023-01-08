N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append([_ for _ in input()])

wScore = 0
bScore = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for x in range(M):
    for y in range(N):

        if graph[x][y] != 'x':
            queue = [[x, y]]
            letter = graph[x][y]
            graph[x][y] = 'x'

            c = 1
            while queue:
                i, j = queue.pop(0)

                for a in range(4):
                    ni = i + di[a]
                    nj = j + dj[a]

                    if ni < 0 or nj < 0 or ni > M-1 or nj > N-1:
                        continue
                    
                    if letter != graph[ni][nj]:
                        continue

                    queue.append([ni, nj])
                    graph[ni][nj] = 'x'

                    c += 1

            if letter == "W":
                wScore += c**2
            else:
                bScore += c**2

print(wScore, bScore)