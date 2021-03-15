from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    going = [queue.popleft()]

    while queue:
        while weight >= sum(going):
            going.append(queue.popleft())
            if answer
            answer += bridge_length

        return answer



solution(2, 10, [7, 4, 5, 6])