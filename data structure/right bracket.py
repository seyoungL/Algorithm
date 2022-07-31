## 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if (s[0] == ")"):
        return False
    
    tmp = list()
    for i in s:
        if i == "(":
            tmp.append(i)
        if i == ")":
            try :
                tmp.pop()
            except IndexError:
                return False
            
    return len(tmp) == 0
            