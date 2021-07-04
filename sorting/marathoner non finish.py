# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]

def solution2(participant, completion):
    from itertools import zip_longest
    
    participant.sort()
    completion.sort()

    for p,c in zip_longest(participant,completion):
        if p != c:
            return p

# ------------------------------------------------
# [ zip_logest() ]
# zip()의 인자 리스트 길이가 다른 경우, 짧은 리스트에 맞춰짐
# 이런경우 zip_logest()를 사용하면 데이터 손실 X
from itertools import zip_longest
 
x = [1, 2, 3]
y = [4, 5, 6,7]
 
list(zip_longest(x, y))
# 결과 : [(1, 4), (2, 5), (3, 6), (None, 7)]

list(zip_longest(x, y, fillvalue=0))
# 결과 : [(1, 4), (2, 5), (3, 6), (0, 7)]



# ------------------ 다른 사람 풀이 ------------------
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# [ collections.Counter ]
# collections.Counter() : dict 로 반환
# return {원소 : 갯수, 원소 : 갯수}
#
# .keys() : 원소 반환 (distinct)
# .elements() : 갯수 만큼 원소 반환
# .items() : key, value 반환
#
# collections.Counter() 는 산술연산이 가능!
collections.Counter({'a':3})-collections.Counter({'a':2})
# 결과 : {'a' : 1}
# cf) 단순 dict 끼리 뺄셈은 안 됨. 즉, {'a' :3} - {'a':2} 는 안 됨.


# [ Counter method 종류 ]
# 1. update() : counter 값 갱신
a = collections.Counter()
# 1) STRING
a.update("aabc")
# 결과 : {'a':2, 'b':1, 'c':1}
# 2) DICT
a.update({'a':2, 'b':1})

# 2. most_common(n) : top n개 리턴 (list안에 tuple로 리턴)
a = collections.Counter({'a':2, 'b':2, 'c':1})
a.most_common(2)
# 결과 : [(a,2), (b,2)]