import pygame

from game import ChessGame
from ui import UI, load_pieces

pygame.init()

WIDTH = 640
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

pieces = load_pieces()
ui = UI(screen, pieces)

game = ChessGame()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = ui.get_square_clicked(event.pos)
            print(f"Clicked: row={row}, col={col}")

    ui.draw_board(game)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()