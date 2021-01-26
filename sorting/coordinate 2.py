# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

from functools import cmp_to_key

# 오름차순 정렬
def cmp(n1, n2){
    if (n1[1] > n2[1]):
        return 1    # >0 : return 뒤 (즉, 작은 값이 return)
    elif (n1[1] == n2[1]):
        if (n1[0] > n2[0]):    
            return 1
        elif (n1[0] < n2[0]):
            return -1    # <0 : return 앞 (M) (즉, 작은 값이 return) 
        else:
            return 0
}

return sorted(input_list, key = cmp_to_key(cmp))