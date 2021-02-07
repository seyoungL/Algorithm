# 기능 개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    from collections import deque
    import math

    ans = []
    dq = deque()

    for (p,s) in zip(progresses, speeds):
        dq.append(math.ceil((100 - p)/s))


    while(dq):
        try:
            cnt = 1
            cur= dq.popleft()

            # if(len(dq)==0):
            #     ans.append(cnt)
            #     break

            nx = dq[0]

            while(cur >= nx):
                cnt += 1
                cur = max(cur, dq.popleft())
                # if(len(dq)==0): 
                #     break
                nx = dq[0]

            ans.append(cnt)
            
        except IndexError:
            ans.append(cnt)

    return ans