from collections import defaultdict


def favorite_genre(user_songs, song_genres):
    genre_map = {}
    for genre, songs in song_genres.items():
        for song in songs:
            genre_map[song] = genre

    # Initialize result dictionary
    result = {}

    # STEP 2: Process each user
    for user, songs in user_songs.items():
        # Initialize frequency counter for genres
        freq_map = defaultdict(int)
        max_freq = 0

        # STEP 3: Count genre frequencies for user's songs
        for song in songs:
            if song in genre_map:
                genre = genre_map[song]
                freq_map[genre] += 1
                max_freq = max(max_freq, freq_map[genre])

        # STEP 4: Find all genres with maximum frequency
        # Instead of list comprehension, using explicit loop for clarity
        fav_genre = []
        for genre, frequency in freq_map.items():
            # If this genre's frequency matches the maximum frequency
            if frequency == max_freq:
                # Add it to favorite genres list
                fav_genre.append(genre)

        # Store result for this user
        result[user] = fav_genre

    return result


# Input: userSongs and songGenres
user_songs = {
    "David": ["song1", "song2", "song3", "song4", "song5"],
    "Emma": ["song5", "song6", "song7"],
}

song_genres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"],
}

# Call the function and print the result
result = favorite_genre(user_songs, song_genres)
print(result)
