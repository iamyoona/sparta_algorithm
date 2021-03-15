s = "(())()"

# 바로 직전의 열린 괄호를 저장해야되니까 Stack이 적절
def is_correct_parenthesis(string):
    parenthesis = []
    for elem in string:
        if elem == '(':
            parenthesis.append(elem)
        else:
            try:
                parenthesis.pop()
            except:
                return False

    if len(parenthesis) == 0:
        return True
    else:
        return False



print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!