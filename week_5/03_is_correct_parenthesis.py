from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()

    return len(stack) == 0

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1

        if left == right:
            break

    v = ''.join(list(queue))
    return u, v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('

    return reversed_string

#1. 입력된 문자열이 빈 문자열인 경우, 빈 문자열을 반환
#2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리
#   단, u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 하며
#   v는 빈 문자열이 될 수 있습니다.
#   ( 와 ) 개수가 같아야 한다
#3. 문자열 u가 올바른 괄호 문자열 이라면, 문자열 v에 대해 1단계부터 다시 수행
#   -> change_to_correct_parenthesis를 다시 호

def change_to_correct_parenthesis(string):
    if string == "":
        return ""
    u, v = separate_to_u_v(string)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return '(' + change_to_correct_parenthesis(v) + ')' + reverse_parenthesis(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)

    print(get_correct_parentheses(balanced_parentheses_string))




print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!