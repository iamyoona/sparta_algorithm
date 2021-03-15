genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    song_dict = {}
    song_index_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in song_dict:
            song_dict[genre] = play
            song_index_dict[genre] = [[i, play]]
        else:
            song_dict[genre] += play
            song_index_dict[genre].append([i, play])

    sorted_song = sorted(song_dict.items(), reverse = True, key = lambda item: item[1])

    result = []

    for genre, _value in sorted_song:
        index_play_array = song_index_dict[genre]
        sorted_index_dict = sorted(index_play_array, key = lambda item: item[1], reverse = True)

        for i in range(len(sorted_index_dict)):
            if i > 1:
                break
            result.append(sorted_index_dict[i][0])

    return result




print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!