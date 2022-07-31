## 게임 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    from collections import deque
    
    n,m = len(maps), len(maps[0])
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    dq = deque([(0,0)])
    
    while dq:
        cx,cy = dq.popleft()

        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if(0<=nx<n and 0<=ny<m and maps[nx][ny]==1):
                    maps[nx][ny] = maps[cx][cy]+1
                    dq.append((nx,ny))

    return maps[-1][-1] if maps[-1][-1] > 1 else -1