input = [3, 5, 6, 1, 2, 4]


"""def is_number_exist(number, array):
    result = 'False'

    if number in array:
        result = 'True'
    else:
        pass

    return result"""


input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array: # array의 길이 만큼 아래 연산 실행
        if number == element:
            return True # N * 1 = N 만큼의 시간복잡
    return False

# 알고리즘은 성능이 항상 동일한게 아니라 입력값의 분포에 따라 시간복잡도가 달라짐



result = is_number_exist(3, input)
print(result)