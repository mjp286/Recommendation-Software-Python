from Tree import TreeNode
from BFS import adding_songs
import csv
genres = []
songs = {}

with open('songs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["genre"] not in genres:
            genres.append(row["genre"])
        list_of_songs = songs.get(row["genre"])
        if list_of_songs == None:
            key = row["genre"]
            if songs.get(key) is None:
                songs[key] = []
                songs[key].append(row["songs"])
            else:
                songs[key].append(row["songs"])
        elif row["songs"] not in list_of_songs:
            key = row["genre"]
            if songs.get(key) is None:
                songs[key] = []
                songs[key].append(row["songs"])
            else:
                songs[key].append(row["songs"])

# Making a tree #

root = TreeNode("Root")
for genre in genres:
    current_child = TreeNode(genre, genre, None)
    root.add_child(current_child)
    for song in songs[genre]:
        grand_child = TreeNode(song, genre, song)
        current_child.add_child(grand_child)

# Adding songs to the tree #
with open('songs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        parent_node = adding_songs(root ,row["songs"], row["genre"])
        current_child = TreeNode(row["songs"], row["album"], row["artist"], row["genre"])
        parent_node.add_child(current_child)



# print(genres)
# print(songs.values())

