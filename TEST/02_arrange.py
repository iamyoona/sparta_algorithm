items = [['item1', '10', '15'], ['item2', '3', '4'], ['item3', '17', '8']]
orderBy = 1
orderDirection = 0
pageSize = 2
pageNumber = 0

def solution(items, orderBy, orderDirection, pageSize, pageNumber):
    answer = []

    if orderDirection == 0:
        rev_val = False
    else:
        rev_val = True

    if orderBy == 0:
        items.sort(key = lambda x:x[orderBy], reverse = rev_val)
    else:
        items.sort(key = lambda x:int(x[orderBy]), reverse = rev_val)

    item_no = pageSize * pageNumber
    start = pageSize

    while len(answer) < pageSize and item_no <= len(items) - 1:
        print(item_no)
        answer.append(items[item_no][0])
        item_no += 1

    return answer


print(solution(items, orderBy, orderDirection, pageSize, pageNumber))

