from .piece import Piece
from typing import List, Tuple

class Pawn(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.value = 1

    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []

        if self.color == "black":
            y = self.y + 1
        else:
            y = self.y - 1

        if (0 <= y <= 7) and self.board[y][self.x].color == "empty":
            moves.append((self.x, y))

        if self.color == "black":
            y = self.y + 2
        else:
            y = self.y - 2

        if (0 <= y <= 7) and self.board[y][self.x].color == "empty" and self.board[y-1][self.x].color == "empty":
            moves.append((self.x, y))

        if self.color == "black":
            y = self.y + 1
            x = self.x + 1
        else:
            y = self.y - 1
            x = self.x - 1

        if (0 <= y <= 7 and 0 <= x <= 7) and self.board[y][x].color != "empty":
            moves.append((x, y))

        if self.color == "black":
            y = self.y + 1
            x = self.x - 1
        else:
            y = self.y - 1
            x = self.x + 1

        if (0 <= y <= 7 and 0 <= x <= 7) and self.board[y][x].color != "empty":
            moves.append((x, y))

        return moves
        