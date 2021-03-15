input = 20


def find_prime_list_under_number(number):
    result = []
    for i in range(2, number):
        semi_result = []
        for j in range(1, i):
            if i % j == 0:
                semi_result.append(j)
        if len(semi_result) == 1:
            result.append(i)

    return result


result = find_prime_list_under_number(input)
print(result)