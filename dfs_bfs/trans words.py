# 단어 변환 
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# 1) DFS
global answer

def DFS(node, target, words, visited, cnt):
    if(node == target):
        global answer
        answer = min(cnt, answer)
        return

    for idx, word in enumerate(words):
        if visited[idx] == 0 and len([i for i, w in enumerate(word) if w != node[i]]) == 1:
            visited[idx] = 1
            DFS(word, target, words, visited, cnt+1)
            visited[idx] = 0      # [주의] 잊지말자. 이 부분 빼먹으면 1) log - dog - cog / 2) log - cog --> 1번 경우에서 cog visited = 1이 되어 2번 경우를 고려하지 않게 됨! 
            
def solution(begin, target, words):
    if(begin == target or target not in words):
        return 0
    
    global answer
    answer = 999999999
    
    l = len(words)
    visited = [0] * l
    DFS(begin, target, words, visited, 0)
    
    return answer


# 2) BFS
# M) 모든 경우를 탐색해서 가장 짧은 값(경로)을 얻어야 한다면 BFS! 사용하는 게 G
# 단, queue에 넣을 때 level 같이 넣어줘야 함! (tuple로 구현) = (값, level)

def BFS(node, words, visited, target):
    search = []
    search.append((node,0))
    answer = 0
    
    while search:
        current =   .pop()
        if current[0] == target:
            return current[1]


        for idx, word in enumerate(words):
            if visited[idx] == 0 and len([i for i, w in enumerate(word) if w != current[0][i]]) == 1:
                visited[idx] = 1
                search.append((word, answer+1))
        answer += 1
    
def solution(begin, target, words):
    if(begin == target or target not in words):
        return 0

    l = len(words)
    visited = [0] * l

    return BFS(begin, words, visited, target)


#-------------------------------------------------#
# 7/18 done