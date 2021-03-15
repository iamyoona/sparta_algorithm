input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alpha_array = [0] * 26

    for char in string:
        if char.isalpha():
            array_index = ord(char) - ord("a")
            alpha_array[array_index] =+ 1
        else:
            continue

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alpha_array)):
        alphabet_occurrence = alpha_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    val = chr(max_alphabet_index + ord("a"))

    #val = alpha_array.index(max(alpha_array))
    #val = chr(val + ord("a"))

    return val


result = find_max_occurred_alphabet(input)
print(result)
