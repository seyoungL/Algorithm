## 아이템 줍기
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# idea : 점과 점을 '잇는 공간'도 한 영역으로 간주하여 배열에 표시하자 (2배 사유)
# 즉, (1,1) (2,2) 사각형 = 원래는 1칸만 색칠되지만
# (1,1), (1-->2,1), (2,1)
# (1, 1-->2), (1-->2, 1-->2), (2, 1-->2)
# (1,2), (1-->2, 2), (2,2)
# 이런식으로 '가는 길' 까지 한 영역으로 간주하는 것임. 즉 원래는 1칸이 9칸이 색칠되도록 작업
# idea 참고 : https://katfun.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%84%EC%9D%B4%ED%85%9C-%EC%A4%8D%EA%B8%B0

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX_NUM = 1000
    board = [[0 for j in range(MAX_NUM)] for i in range(MAX_NUM)] # 이차원 배열 초기화
    
    # 테두리,내부 1로 채우기 
    for c1, r1, c2, r2 in rectangle :
        for i in range(2*r1, 2*r2+1):
            for j in range(2*c1, 2*c2+1):
                board[i][j] = 1
                
    # 내부 0으로 채우기 
    for c1, r1, c2, r2 in rectangle :
        for i in range(2*r1+1, 2*r2):
            for j in range(2*c1+1, 2*c2):
                board[i][j] = 0
                
    cR, cC, iR, iC = 2*characterY, 2*characterX, 2*itemY, 2*itemX
    stack = [(0, cR, cC)]
    
    # bfs
    while stack :
        cnt, curR, curC = stack.pop(0)
        board[curR][curC] = -1  # passed
        
        if board[iR][iC] < 0:
            return cnt/2   # 좌표 2배해주었으니 마지막 결과에서 /2
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if board[curR+dr][curC+dc] > 0 :
                stack.append((cnt+1, curR+dr, curC+dc))
        