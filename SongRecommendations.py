from Data import genres, songs


def introduction():
    print("Welcome to the song recommender!") 


def choices():
    genre = ""
    choice = ""
    print("What genre would you like to see? \n")
    while True:

        format_genres = []
        for i in genres:
            format_genres.append(i.capitalize())
        genre = input(f"Here is list of possible genre: {format_genres} \n")
        genre = genre.lower()
        if genre not in genres:
            print("Not on the list!")
        else: 
            break
    
    song = input(f"Would you like see songs? Y'\'N: ")
    if song.lower() == 'y':
            format_list = []
            for item in songs[genre]:
                format_list.append(item.capitalize().replace("_", " "))


            if not format_list:
                print("No songs available for this genre.")
            else:
                for song in format_list:
                 print(song)
            

    return genre, choice



def repeat():
    repeat_ans = input("\n Do you want to get recommmendations for another genre ?  | Y'\'N: ")
    if repeat_ans.lower() == 'y':
        return True
    else:
        return False