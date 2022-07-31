# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

# Sol 1) BFS, 이중 for 문 미사용
# https://url.kr/a9pzsw (G)

def solution(n, computers):
    ans = 0
    visited = [0] * n
    bfs = []  # 탐색할 노드

    while 0 in visited:
        node = visited.index(0)    # 탐색할 노드    ** Sol 2) line 46~47
        bfs.append(node)           # Sol 2) BFS()
        visited[node] = 1

        while bfs:
            node = bfs.pop()

            for i in range(n):
                if(visited[i] == 0 and computers[i][node] == 1):
                    visited[i] = 1
                    bfs.append(i)

        ans+=1

    return ans

# Sol 2) BFS
# https://url.kr/4nv6z9
def BFS(idx, computers, n, visited):
    bfs = []
    bfs.append(idx)

    while bfs:
        node = bfs.pop(0)
        visited[node] = 1

        for j in range(n):
            if visited[j] == 0 and computers[node][j] == 1:
                bfs.append(j)

def solution(n, computers):
    ans = 0
    visited = [0]*n

    for i in range(n):
        if visited[i] == 0:     # Sol 1, line 12 ~ 13
            BFS(i, computers, n, visited)
            ans += 1
    
    return ans


# Sol 3) DFS
# https://url.kr/4nv6z9
def DFS(idx, computers, n, visited):
    visited[idx] = 1

    for j in range(n):
        if visited[j] == 0 and computers[idx][j] == 1:
            DFS(j, computers, n, visited)

def solution(n, computers):
    ans = 0
    visited = [0]*n

    for i in range(n):
        if visited[i] == 0:
            DFS(i, computers, n, visited)
            ans += 1

    return ans 

#-------------------------------------------------#
# 7/18 done