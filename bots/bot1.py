import chess
import random



def get_best_guess(game):
    
    game.board = chess.Board()
    
    list(game.board.legal_moves)

    return "e2e4"

def get_random_move(game):
    game.board = chess.Board()
    
    chosen_at_random = list(game.board.legal_moves)

    return str(random.choice(chosen_at_random))

