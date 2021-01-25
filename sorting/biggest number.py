# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*4, reverse = True) 
    
    return str(int(''.join(numbers)))




# -----------------------------------------------
# [ sort() vs sorted() ]
# sort() : 반환값 없음. 원본 리스트 변경
# sorted() : 원본 리스트 변함 없음. 정렬된 리스트 반환
# -----------------------------------------------