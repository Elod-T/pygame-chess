from .piece import Piece
from .empty import Empty
from typing import List, Tuple


class Bishop(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.value = 3

    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        for direction in directions:
            x, y = self.x, self.y
            while True:
                x += direction[0]
                y += direction[1]
                if x < 0 or x > 7 or y < 0 or y > 7:
                    break
                if isinstance(self.board[y][x], Empty):
                    moves.append((x, y))
                elif self.board[y][x].color != self.color:
                    moves.append((x, y))
                    break
                else:
                    break

        return moves
