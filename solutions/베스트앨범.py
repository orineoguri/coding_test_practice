def solution(genres, plays):
    
    number_of_songs = len(genres)
    
    genre_played = {}
    genre_best_song_1 = {}
    genre_best_song_2 = {}
    
    for i in range(number_of_songs): # setup
        genre_played[genres[i]] = 0
        genre_best_song_1[genres[i]] = -1
        genre_best_song_2[genres[i]] = -1
        
    for i in range(number_of_songs): # actual loop
        genre_played[genres[i]] += plays[i]
        if genre_best_song_1[genres[i]] == -1:
            genre_best_song_1[genres[i]] = i
        elif plays[genre_best_song_1[genres[i]]] < plays[i]:
            genre_best_song_2[genres[i]] = genre_best_song_1[genres[i]]
            genre_best_song_1[genres[i]] = i
        elif genre_best_song_2[genres[i]] == -1:
            genre_best_song_2[genres[i]] = i
        elif plays[genre_best_song_2[genres[i]]] < plays[i]:
            genre_best_song_2[genres[i]] = i 
    
    sorted_genre = sorted(genre_played.items(), key=lambda x: x[1], reverse=True) # value 기준으로 정렬
    answer = []
    
    for genre in sorted_genre:
        answer.append(genre_best_song_1[genre[0]])
        if genre_best_song_2[genre[0]] > -1:
            answer.append(genre_best_song_2[genre[0]])

    return answer