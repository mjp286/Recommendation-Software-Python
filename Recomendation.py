from Data import root, genres, songs
from BFS import getting_songs


def introduction():
    print("Welcome to the song recomender!") 


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
    
    song = input(f"Would you like see songs\n Y'\'N: ")
    if song.lower() == 'y':
            format_list = []
            for item in songs[genre]:
                format_list.append(item.capitalize().replace("_", " "))
            print(format_list)
            choice = choice.lower().replace(" ", ("_"))
            if choice not in songs[genre]:
                print("Not on the list!")
            

    return genre, choice

def name_swap(string):
    string_split = string.split()
    if len(string_split) == 0:
        return ""
    surrname = string_split[0].strip().strip(',')
    name = "---"
    for i in string_split[1:]:
        name += i.strip() + ' '
    return name + surrname.strip()

def recomedations():
    (genre, sub_genre) = choices()
    list_of_nodes = getting_songs(root, genre, sub_genre)
    book_names = "\n"
    for node in list_of_nodes:
        if ',' in node.name and ('The' in node.name or 'A' in node.name):
            string_to_split = node.name.split()
            formated_string = ""
            prefix = ""
            suffix = ""
            for string in string_to_split:
                string = string.strip(',')
                if string.strip() == 'A' or string.strip() == 'The':
                    prefix += string.strip()
                    #print(prefix)
                else:
                    suffix += " " + string.strip()
                    #print(suffix)
            
            formated_string = prefix + suffix
            book_names += "Title: " + formated_string + ' | Author: ' + name_swap(node.author)
        else:
            book_names += "Title: " + node.name + ' | Author: ' + name_swap(node.author)
    
        if sub_genre is None or sub_genre == '':
            book_names += ' | Sub-Genre:' + node.sub_genre.capitalize().replace('_', ' ') + '\n'
        else:
            book_names += '\n'
    print(book_names)

def repeat():
    repeat_ans = input("\n Do you want to get recomendations for another genre ?  | Y'\'N: ")
    if repeat_ans.lower() == 'y':
        return True
    else:
        return False