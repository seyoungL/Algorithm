# 이중 우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

# sol1 ) 배열
def solution(operations):
    tmpList = []
    
    for o in operations:
        try:
            delim, num = o.split()

            if delim == "I":
               tmpList.append(int(num)) 
            else:
                if num == "1":
                    tmpList.pop()
                else:
                    tmpList.pop(0)

            tmpList.sort()
        except IndexError:
            pass

    if len(tmpList) > 0:
        return [tmpList.pop(), tmpList.pop(0)]
    else:
        return [0,0]


# Sol2) heapq (heapq로 구현하기 때문에 따로 sort 필요 없음. default 오름차순)
# min/max heap 배열 2개
# 최대값 : max_heap = heappop / min_heap은 remove
def solution(operations):
    import heapq
    
    min_heap = []
    max_heap = []
    
    for o in operations:
        try:
            delim, num = o.split()

            if delim == "I":
               heapq.heappush(min_heap, int(num)) 
               heapq.heappush(max_heap, (int(num)*-1, int(num)))   # (우선순위, value)
            else:
                if num == "1":
                    max_val = heapq.heappop(max_heap)[1]
                    min_heap.remove(max_val)
                else:
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove((min_val*-1, min_val))

        except IndexError:
            pass

    if len(min_heap) > 0:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0,0]


# Sol3) 다른사람 풀이
import heapq

def solution(arguments):
    dp_queue = []

    for arg in arguments:
        op, val = arg.split(' ')
        if op == 'I':
            heapq.heappush(dp_queue, int(val))
        else:
            try:
                if val == '1':
                    remove_value = heapq.nlargest(1, dp_queue)[0]   # heapq.nlargest(n, list)[0:]  : 가장 큰 top n개 뽑아냄
                else:
                    remove_value = heapq.nsmallest(1, dp_queue)[0]  # heapq.nsmallest(n, list)[0:] : 가장 작은 top n개 뽑아냄
            except IndexError:
                pass
            else:
                dp_queue.remove(remove_value)
                heapq.heapify(dp_queue)

    if len(dp_queue) == 0:
        max_value = 0
        min_value = 0
    elif len(dp_queue) == 1:
        max_value = dp_queue[0]
        min_value = dp_queue[0]
    else:
        max_value = heapq.nlargest(1, dp_queue)[0]
        min_value = heapq.nsmallest(1, dp_queue)[0]

    return [max_value, min_value]