array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

array_c = []


def merge(array1, array2):
    global array_c
    for i in range(len(array1)):

        for j in range(len(array2)):
            if array1[i] > array2[j]:
                array_c.append(array2[j])
                return merge(array1, array2[j + 1:])
            else:
                array_c.append(array1[i])
                return merge(array1[i + 1:], array2)

    if len(array1) == 0:
        for k in array2:
            array_c.append(k)
    elif len(array2) == 0:
        for l in array2:
            array_c.append(l)

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
