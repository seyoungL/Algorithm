# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n = len(numbers)
    ans = 0

    def dfs(idx, result):
        if idx == n :
            if result == target:
                nonlocal ans
                ans += 1
            return

        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])

    dfs(0,0)

    return ans

# Sol2)
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))

    return s.count(target)


# [ Lesson learned ]
# 1. nonlocal
# nonlocal이 사용된 함수 바로 한 단계 바깥쪽에 위치한 변수에 바인딩 cf) global

# 2. from itertools import product (곱집합)
# ex)
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)

# using product
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))


#-------------------------------------------------#
# 7/18 done