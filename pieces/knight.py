from .piece import Piece
from .empty import Empty
from typing import List, Tuple


class Knight(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.shortName = self.color[0] + "N"
        self.value = 3 

    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if x < 0 or x > 7 or y < 0 or y > 7:
                continue
            if isinstance(self.board[y][x], Empty) or self.board[y][x].color != self.board[self.y][self.x].color:
                moves.append((x, y))
        return moves
