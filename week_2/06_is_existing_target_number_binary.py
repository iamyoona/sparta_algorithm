finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0 # 인덱스 값
    current_max = len(array) - 1 # 인덱스 값
    current_guess = (current_min + current_max)//2

    count = 0

    while current_min <= current_max:
        count += 1
        if array[current_guess] == target:
            print(count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1

        current_guess = (current_max + current_min) // 2


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)