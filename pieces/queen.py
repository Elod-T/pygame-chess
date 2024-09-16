from .piece import Piece
from .bishop import Bishop
from .rook import Rook
from typing import List, Tuple


class Queen(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)

    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []

        asBishop = Bishop(self.x, self.y, self.color)
        asBishop.board = self.board
        moves += asBishop.get_moves()
        del asBishop

        asRook = Rook(self.x, self.y, self.color)
        asRook.board = self.board
        moves += asRook.get_moves()
        del asRook
        
        return moves