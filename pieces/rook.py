from .piece import Piece
from .empty import Empty
from typing import List, Tuple


class Rook(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.value = 5
        
    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []
        # up
        for i in range(self.y-1, -1, -1):
            if isinstance(self.board[i][self.x], Empty):
                moves.append((self.x, i))
            elif self.board[i][self.x].color != self.board[self.y][self.x].color:
                moves.append((self.x, i))
                break
            else:
                break
        # down
        for i in range(self.y+1, 8):
            if isinstance(self.board[i][self.x], Empty):
                moves.append((self.x, i))
            elif self.board[i][self.x].color != self.board[self.y][self.x].color:
                moves.append((self.x, i))
                break
            else:
                break
        # left
        for i in range(self.x-1, -1, -1):
            if isinstance(self.board[self.y][i], Empty):
                moves.append((i, self.y))
            elif self.board[self.y][i].color != self.board[self.y][self.x].color:
                moves.append((i, self.y))
                break
            else:
                break
        # right
        for i in range(self.x+1, 8):
            if isinstance(self.board[self.y][i], Empty):
                moves.append((i, self.y))
            elif self.board[self.y][i].color != self.board[self.y][self.x].color:
                moves.append((i, self.y))
                break
            else:
                break
        return moves
