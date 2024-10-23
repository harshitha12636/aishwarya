# Simple Music Organizer

def music_organizer():
    songs = []

    while True:
        print("\nMusic Organizer")
        print("1. Add Song")
        print("2. View Songs")
        print("3. Remove Song")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            song = input("Enter the song title: ")
            artist = input("Enter the artist name: ")
            songs.append({"title": song, "artist": artist})
            print(f"Song '{song}' by {artist} added.")
        elif choice == '2':
            if not songs:
                print("No songs in the organizer.")
            else:
                print("Songs in the organizer:")
                for idx, song in enumerate(songs, start=1):
                    print(f"{idx}. {song['title']} by {song['artist']}")
        elif choice == '3':
            if not songs:
                print("No songs to remove.")
            else:
                song_number = int(input("Enter the song number to remove: "))
                if 1 <= song_number <= len(songs):
                    removed_song = songs.pop(song_number - 1)
                    print(f"Removed '{removed_song['title']}' by {removed_song['artist']}.")
                else:
                    print("Invalid song number.")
        elif choice == '4':
            print("Exiting the music organizer.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    music_organizer()