from collections import deque

def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    queue = deque(phone_book)
    now_num = queue.popleft()

    print(now_num, queue)

    while queue:
        print(queue)
        while queue:
            if now_num == num[0:len(now_num)]:
                print(num[0:len(now_num)])
                answer = False
                break
            else:
                now_num = queue.popleft()

                print(now_num)
                continue

    return answer


print(solution(["12", "123", "1235", "567", "88"]))