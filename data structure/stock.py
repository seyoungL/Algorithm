# 주식 가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    from collections import deque
    
    answers = []
    dq = deque(prices)
    
    while(dq):
        price = dq.popleft()
        time = 0
        
        for p in dq:
            time +=1
            if(p < price):
                break
            
        answers.append(time)
                
    return answers
    

# ---------------------
# [ deque ]
from collections import deque
dq = deque('love')  # [l,o,v,e]

## 1. 추가/삭제
# append(), pop() : 오른쪽 추가/삭제
# appendleft(), popleft() : 왼쪽 추가/삭제

# extend(), extendleft() : 한꺼번에 추가하기
dq.extend('you')       # l,o,v,e,y,o,u
dq.extendleft('you')   # u,o,y,l,o,v,e

# insert(), remove() : index로 추가, 삭제
dq.insert(0,'K')      # K,l,o,v,e
dq.insert(100,'K')    # K,l,o,v,e,K

dq.remove('K')        # l,o,v,e,K     # 같은 항목이 있을 때 '왼쪽' 부터 삭제됨
dq.remove('K')        # l,o,v,e

## 2. 치환
dq[2] = 'n'           # l,o,n,e

## 3. 좌우 반전
# reverse()
dq.reverse()

## 4. 밀어내기
# rotate(n) : n>0 왼쪽에서 밀기 / n<0 오른쪽에서 밀기(push) 
dq.rotate(1)    # e,l,o,v
dq.rotate(2)    # v,e,l,o

dq.rotate(-1)   # o,v,e,l
dq.rotate(-2)   # v,e,l,o