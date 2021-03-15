from collections import deque

c = 11
b = 2

# 경우의 수가 너무 많을 것 같다 -> 다 나열해야됨 -> BFS
# 규칙적으로 변화하는 건 배열, 자유자재로 변화하는 건 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 동시에 담음 (둘 다 일치해야 하기 때문에)
    visited = [{} for _ in range(200001)]
    # visited[0] = {2:True}
    # visited[1] = {1:True, 3:True, 4:True}...

    while cony_loc + time <= 200000:
        # print(cony_loc)
        cony_loc += time
        print(visited[cony_loc])
        if time in visited[cony_loc]:
            return time

        for i in range(len(queue)):
            cur_position, cur_time = queue.popleft()

            new_time = cur_time + 1

            new_position = cur_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!
