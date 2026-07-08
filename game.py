import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self,move):

        if isinstance(move,str):
            try:
                move = chess.Move.from_uci(move)
            except ValueError:
                return False
    
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False
    
    def is_over(self):
        return self.board.is_game_over()
    
    def result(self):
        return self.board.result()
    
    def legal_moves(self):
        return list(self.board.legal_moves)
    
    def turn(self):
        return self.board.turn == chess.WHITE

    def piece_at(self, square):
        sq = chess.parse_square(square)
        return self.board.piece_at(sq)
    
    def __str__(self):
        return str(self.board)