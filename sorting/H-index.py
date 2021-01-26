# H-index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    
    return max(map(min, enumerate(citations, start=1)))



# -----------------------------------------------
# [ enumerate() ]
# 위와 같이 index 시작점을 지정해 줄 수 있음
# return (idx, num) tuple

# [ zip() ]
# list, tuple 병렬처리
# 
# ex) [sum(x) for x in zip (1,2,3), (10,20,30), (100,200,300)]
# --> return [111,222,333]
# -----------------------------------------------