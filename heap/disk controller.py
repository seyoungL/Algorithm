# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

import heapq

def solution(jobs):
    ans, now, i = 0,0,0
    bfJobStartTime = -1
    jobList = []

    while i < len(jobs):
        # 현 시각 기준 요청들어온 job들을 heapq에 insert
        for job in jobs:
            if bfJobStartTime < job[0] <= now:    # bfJobStartTime < 조건 넣는 이유 : 이미 처리한 job이 중복 처리될 수 있으므로
                heapq.heappush(jobList, [job[1], job[0]])

        if len(jobList) > 0:
            i += 1
            bfJobStartTime = now
            
            cur = heapq.heappop(jobList)
            now += cur[0]
            
            ans += (now - cur[1])

        else:
            now += 1

    return int(ans/len(jobs))


## Wrong : 작업 시간 오름차순으로 생각하면, 작업을 안하는 빈 시간이 생기게 됨
# (0,1) (3,3) (2,4) (1,9) --> 1~3초 사이 공백이 생김 (2초에 요청한 job 처리할 수 있으나)
def solution(jobs):
    import heapq
    
    jobList = []
    ans, cum = 0, 0
    
    for job in jobs:
        jobList.append([job[1], job[0]])    # 작업 시간 오름차순으로 정렬되도록. 작업 시간이 앞으로 오도록 변형
                        
    heapq.heapify(jobList)
    
    while 1:
        if len(jobList) < 1 :
            break
        
        cur = heapq.heappop(jobList)
        ans += (cum + cur[0] - cur[1])
        cum += cur[0]
        
    return int(ans/len(jobs))