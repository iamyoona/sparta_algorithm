n = 5
start_time = [17, 978, 409, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426,
              670, 116, 95, 630]
running_time = [17, 502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753,
                567, 717, 338, 439, 145]


def solution(start_time, running_time):
    end_time = [x + y for x, y in zip(start_time, running_time)]
    meeting = list(zip(start_time, end_time))
    print(meeting)
    meeting.sort(key = lambda x:(x[1], x[0]))

    start_time, end_time = map(list,zip(*meeting))
    print(start_time, end_time)

    answer = 0
    start = 0
    for i in range(len(start_time)):
        #print(i, start, start_time[i], start < start_time[i])
        if start_time[i] >= start:

            start = end_time[i]
            answer += 1


    #print(i, start, start_time[i])
    return answer

print(solution(start_time, running_time))