top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    results = [0]
    for i in range(1, len(heights)):

        stack = heights[0:i]
        print(stack, heights[i])
        for j in range(1, i + 1):
            print(i, j)
            if stack[i - j] > heights[i]:
                result = i - j + 1
                break
            else:
                result = 0
                continue
        results.append(result)

    return results


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
