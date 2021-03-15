input = "abcba"

"""
def is_palindrome(string):
    current_min = 0
    current_max = len(string) - 1
    guess_num = (current_min + current_max) // 2

    for i in range(guess_num):
        if string[current_min + i] == string[current_max - i]:
            return True

        return False"""


"""def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]:
            return False
        return True"""

def is_palindrome(string):
    cur_min = 0
    cur_max = len(string) - 1

    string[n] != string[-n]



print(is_palindrome(input))