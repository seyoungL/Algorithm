# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for i in range(0,len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return True


# ----- 다른 사람 풀이 -------- #
def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if(p2.startswith(p1)):
            return False

    return True