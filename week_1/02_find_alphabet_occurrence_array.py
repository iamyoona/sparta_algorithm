def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for alpha in string:
        if alpha.isalpha():
            array_index = ord(alpha) - ord("a")
            alphabet_occurrence_array[array_index] =+ 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
alphabet_occurrence_array = find_alphabet_occurrence_array("hello my name is sparta")
print("most_frequent_alphabet:", chr((alphabet_occurrence_array.index(max(alphabet_occurrence_array))) + ord("a")))
