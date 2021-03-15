input = "abadabac"


def find_not_repeating_first_character(string):
    temp = list(set(string))
    result = '_'
    for elem in temp:
        if string.count(elem) == 1:
            result = elem


    return result


result = find_not_repeating_first_character(input)
print(result)