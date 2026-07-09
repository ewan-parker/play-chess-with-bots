import pygame
import chess

SQUARE_SIZE = 80

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
HIGHLIGHT = (246, 246, 105)


def load_pieces():
    pieces = {}

    piece_names = [
        "black_bishop",
        "black_king",
        "black_knight",
        "black_pawn",
        "black_queen",
        "black_rook",
        "white_bishop",
        "white_king",
        "white_knight",
        "white_pawn",
        "white_queen",
        "white_rook",
    ]

    for name in piece_names:
        image = pygame.image.load(f"assets/pieces/{name}.png").convert_alpha()
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[name] = image

    return pieces


class UI:
    def __init__(self, screen, piece_images):
        self.screen = screen
        self.piece_images = piece_images

    def draw_board(self, game):
        piece_lookup = {
            chess.PAWN: "pawn",
            chess.ROOK: "rook",
            chess.KNIGHT: "knight",
            chess.BISHOP: "bishop",
            chess.QUEEN: "queen",
            chess.KING: "king",
        }

        for row in range(8):
            for col in range(8):

                color = LIGHT if (row + col) % 2 == 0 else DARK

                rect = pygame.Rect(
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                )

                pygame.draw.rect(self.screen, color, rect)

                square = chess.square(col, 7 - row)
                piece = game.board.piece_at(square)

                if piece:
                    colour = "white" if piece.color == chess.WHITE else "black"
                    image_name = f"{colour}_{piece_lookup[piece.piece_type]}"

                    self.screen.blit(
                        self.piece_images[image_name],
                        (col * SQUARE_SIZE, row * SQUARE_SIZE),
                    )

    def get_square_clicked(self, pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        return row, col