from SongRecommendations import introduction, choices, repeat

introduction()
recommend = True

while recommend:
    choices()
    recommend = repeat()

print("\n Thank you for using the song recomender. Good Bye! ")