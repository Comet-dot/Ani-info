import os
from AnilistPython import Anilist
anilist = Anilist()
title = input("Enter anime title: ")

#Anilist part 
ani_list = anilist.get_anime(title, manual_select=True)
os.system('cls')
print("Name:",ani_list["name_english"])
print("Score:",ani_list["average_score"])
print("Release date:", ani_list["starting_time"])
print("Episodes:",ani_list["airing_episodes"])
print("Genres:",ani_list["genres"])
print("Description:",ani_list["desc"])
