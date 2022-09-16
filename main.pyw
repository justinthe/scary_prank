import pygame
from time import sleep
import random


def main():
	while True:	
		n = random.randint(30, 120)
		# print(n)
		sleep(n)
		surprise()

def surprise():
	pygame.init()
	window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.mixer.init()
	pygame.mixer.music.load('res/scary.mp3')
	pygame.mixer.music.play()
	image = pygame.image.load('res/scr.jpg')
	window.blit(image, (0, 0))
	pygame.display.update()
	sleep(2)
	pygame.quit()	
	


if __name__ == "__main__":
	main()





