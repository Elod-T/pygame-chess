from re import I
from .piece import Piece
from .empty import Empty
from .rook import Rook
from typing import List, Tuple


class King(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.value = 0 # okay it's worth the whole game but we don't count it in the points

    def get_moves(self) -> List[Tuple[int, int]]:
        moves = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                x = self.x + j
                y = self.y + i

                if x < 0 or x > 7 or y < 0 or y > 7 or (i == 0 and j == 0):
                    continue
                
                piece = self.board[y][x]
                if isinstance(piece, Empty) or piece.color != self.color:
                    moves.append((x, y))

        # * castling
        if self.has_moved == False:
            if self.color == "white":
                leftRook = self.board[7][0]
                rightRook = self.board[7][7]

                isLeftEmpty = True
                isRightEmpty = True
                for i in range(1, 4):
                    if not isinstance(self.board[7][i], Empty):
                        isLeftEmpty = False
                        break
                for i in range(5, 7):
                    if not isinstance(self.board[7][i], Empty):
                        isRightEmpty = False
                        break

                if isinstance(leftRook, Rook) and leftRook.color == "white" and leftRook.has_moved == False and isLeftEmpty:
                    moves.append((2, 7))
                if isinstance(rightRook, Rook) and rightRook.color == "white" and rightRook.has_moved == False and isRightEmpty:
                    moves.append((6, 7))
            else:
                leftRook = self.board[0][0]
                rightRook = self.board[0][7]

                isLeftEmpty = True
                isRightEmpty = True
                for i in range(1, 4):
                    if not isinstance(self.board[0][i], Empty):
                        isLeftEmpty = False
                        break
                for i in range(5, 7):
                    if not isinstance(self.board[0][i], Empty):
                        isRightEmpty = False
                        break

                if isinstance(leftRook, Rook) and leftRook.color == "black" and leftRook.has_moved == False and isLeftEmpty:
                    moves.append((2, 0))
                if isinstance(rightRook, Rook) and rightRook.color == "black" and rightRook.has_moved == False and isRightEmpty:
                    moves.append((6, 0))

        return moves
        