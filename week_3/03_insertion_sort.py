input = [4, 6, 2, 9, 1]


def insertion_sort(array): # break 때문에 시간복잡도 줄어들음( 오메가(N))
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i- j], array[i- j -1]
            else:
                break


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!