# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

def solution(scoville, K):
    import heapq
    
    heapq.heapify(scoville)
    ans = 0
    
    while 1:
        if scoville[0] < K and len(scoville) <=1:
            ans = -1
            break
            
        if scoville[0] >=K:
            break
        
        cur = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,cur)
        ans += 1

    return ans
        

# [ Lesson learned ]
# heapq : heap 정렬 queue. sort()보다 빠름
# min heap : 오름차순 정렬 (default)
# max heap(내림차순)을 원하면 heapq에 tulple (우선순위, 값)으로 insert하고, (우선순위 = 큰 값) 
# heapq.heappop()[1] 로 꺼내면 됨.

# 1. 하나씩 insert
# import heapq
# arr = []
# heapq.heappush(arr, 2)

# 2. 기존재하는 배열 heapq로
# heapq.heapify(arr)


# [ 주의할 점 ]
# heapq는 heappop할 때 최소 값을 다시 배열내에서 구해서 정렬시킴
# 따라서 scoville[0] 은 min으로 보장하지만, scoville[1]이 그 다음 최소값임은 보장 X
# 2번째 최소값을 얻으려면 heappop()하고, scoville[0] 해야함