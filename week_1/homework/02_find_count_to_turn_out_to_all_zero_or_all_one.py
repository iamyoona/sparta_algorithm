input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    temp_array = [string[0]]
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            temp_array.append(string[i])

    result = min(temp_array.count('0'), temp_array.count('1'))

    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)