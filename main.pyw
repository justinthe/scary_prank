# run pyinstaller on windows machine with this command:
# pyinstaller --onefile --add-data="scary.mp3;." --add-data="scr.jpg;." --icon="firefox_icon.ico" main.pyw


import pygame
from time import sleep
import random
import sys
import os
import webbrowser
import datetime
import platform


# flag to determine if os == windows
is_windows = True

if "Linux" in platform.system():
    is_windows = False

# specifically for windows. need this to always show on top
if is_windows:   
    from ctypes import windll


def main():

    # run webbrowser to disguise the app
    webbrowser.open("http://www.google.com")

    while True:	
        # n = random.randint(30, 120)
        # randomize the surprise between 1 min to 1 hour
        n_lst = random.sample(range(60, 60*60, 60), 1)
        # n_lst = random.sample(range(10, 10*6, 60), 1)
        n = n_lst[0]
        # print(n)

        # only run on even date - to make it more unpredictable
        cur = datetime.datetime.now()
        dt = cur.day
        if dt % 2 == 0:
            # print(n)
            sleep(n)
            surprise()
    
def surprise():

    if is_windows:
        SetWindowPos = windll.user32.SetWindowPos

    sound_file = "scary.mp3"
    image_file = "scr.jpg"
    
    sound_path = resource_path(sound_file)
    image_path = resource_path(image_file)
    # print("Sound path: {}; Image path: {}".format(sound_path, image_path))
            
    pygame.init()
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mixer.init()
    
    # check to see if user is engaged 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            # pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops = -1)
            image = pygame.image.load(image_path)
            # make sure it always sits on top of other windows    
            if is_windows:
                SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)
                window.blit(image, (0, 0))
                pygame.display.update()
    sleep(2)
    pygame.quit()	
    

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
    
if __name__ == "__main__":
    main()





