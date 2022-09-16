import pygame
from time import sleep
import random

def main():

    while True:
        n = random.randint(30, 120)
        # print(n)
        sleep(n)
        pygame.mixer.init()
        pygame.mixer.music.load('res/scary.mp3')
        pygame.mixer.music.play()
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        image = pygame.image.load('res/scr.jpg')
        window.blit(image, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
