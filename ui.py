import pygame

SQUARE_SIZE = 80
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
HIGHLIGHT = (246, 246, 105)

class c_UI:
    def __init__(self, screen, piece_images):
        self.screen = screen
        self.piece_images = piece_images

    def draw_board(self, game):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = LIGHT
                else:
                    color = DARK

                if game.selected_square == (row,col):
                    color = HIGHLIGHT

                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, 
                                    SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.Rect(self.screen, color, rect)

    def get_square_clicked(self,pos):
        x,y = pos
        col = x
        row = y
        return row, col




