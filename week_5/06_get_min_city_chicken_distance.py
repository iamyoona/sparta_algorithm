import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):

    chicken = []
    home = []
    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == 2:
                chicken.append([i, j])
            elif city_map[i][j] == 1:
                home.append([i, j])

    max_chicken = list(itertools.combinations(chicken, m))

    min_distance = []
    for house in home:
        distance = []
        for chick in max_chicken:
            for ch in chicken:
                dis = abs(ch[0] - house[0]) + abs(ch[1] - house[1])
                distance.append(dis)
        min_distance.append(min(distance))

    return(sum(min_distance))

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!