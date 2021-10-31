
import random
import os
import time

while True:
    c = random.randint(1, 2)
    if c == 1:
        music_folder = "D:\\d data\\NCS music"
        songs = os.listdir(music_folder)
        a = random.randint(1, len(songs) - 1)
        os.startfile(os.path.join(music_folder, songs[a]))
        time.sleep(60*4)
    elif c == 2:
        music_folder = "D:\\d data\\New songs"
        songs = os.listdir(music_folder)
        a = random.randint(1, len(songs) - 1)
        os.startfile(os.path.join(music_folder, songs[a]))
        time.sleep(60*4)
    else:
        pass

