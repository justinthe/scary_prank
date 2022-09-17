import pygame
from time import sleep
import random
import sys
import os


def main():
    while True:	
        n = random.randint(30, 120)
        # print(n)
        sleep(n)
        surprise()
    
def surprise():

    sound_file = "res/scary.mp3"
    image_file = "res/scr.jpg"
    
    sound_path = resource_path(sound_file)
    image_path = resource_path(image_file)
    # print("Sound path: {}; Image path: {}".format(sound_path, image_path))
            
    pygame.init()
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    image = pygame.image.load(image_path)
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





