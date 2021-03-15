top_heights = [6, 9, 5, 7, 4]


# 맨 뒤에께 없어지니까 stack 사용
def get_receiver_top_orders(heights):# O(N^2)의 시간복잡도를 가짐
    answer = [0] * len(heights)  # [0, 0, 0, 0, 0] 초기화된 결과 배열
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))
