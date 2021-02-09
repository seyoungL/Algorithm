# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    from collections import deque

    bridge = deque()

    for i in range(bridge_length):   # ***
        bridge.append(0)

    ans, b_weight = 0, 0

    while(truck_weights):
        ans += 1

        if(len(bridge) == bridge_length):   # *** 여기 if문 없애고 위에 for문 초기화 추가해줘도 됨 (아래 class solution과 동일해짐)
            out_trk = bridge.popleft()
            b_weight -= out_trk

        if(b_weight +truck_weights[0] <= weight):
            in_trk = truck_weights.pop(0)
            bridge.append(in_trk)
            b_weight += in_trk
        else:
            bridge.append(0)

    return ans + bridge_length


# [ Lesson learned ]
# list.pop(0) : 왼쪽 요소 pop
# list.pop() : 오른쪽 요소 pop

# ----- 다른 사람 풀이 ------
# my sol을 class로 구현
from collections import deque

DUMMY_TRUCK = 0

class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        out_trk = self._queue.popleft()
        self._current_weight -= out_trk        
        return

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    return count + bridge_length


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()