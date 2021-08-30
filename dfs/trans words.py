# 단어 변환 
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

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
            visited[idx] = 0
            
def solution(begin, target, words):
    if(begin == target or target not in words):
        return 0
    
    global answer
    answer = 999999999
    
    l = len(words)
    visited = [0] * l
    DFS(begin, target, words, visited, 0)
    
    return answer