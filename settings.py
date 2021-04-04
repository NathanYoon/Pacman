import pygame
from maze import gameBoard

BoardPath = "Assets/BoardImages/"
ElementPath = "Assets/ElementImages/"
TextPath = "Assets/TextImages/"
DataPath = "Assets/Data/"
MusicPath = "Assets/Music/"

pygame.mixer.init()
pygame.init()
print(pygame.mixer.music.get_busy())

spriteRatio = 3/2
square = 28 # Size of each unit square
spriteOffset = square * (1 - spriteRatio) * (1/2)
(width, height) = (len(gameBoard[0]) * square, len(gameBoard) * square) # Game screen
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
musicPlaying = 0 # 0: Chomp, 1: Important, 2: Siren
# pelletColor = (165, 93, 53)
pelletColor = (222, 161, 133)
