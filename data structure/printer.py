# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    
    from collections import deque
    
    dq = deque([(v,i) for (i,v) in enumerate(priorities)])
    ans = 0
    
    while len(dq):
        cur = dq.popleft()
        
        #if any(cur[0] < q[0] for q in dq)     # sol 2)
        if dq and cur[0] < max(dq)[0]:
            dq.append(cur)
        else:
            ans += 1
            if location == cur[1]:
                break
                
    return ans