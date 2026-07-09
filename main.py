import pygame
from game import ChessGame


game = ChessGame()

pygame.init()
screen = pygame.display.set_mode((1200,900))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)