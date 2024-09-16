from numpy import isin
import pygame
from pieces import Pawn, Rook, Knight, Bishop, Queen, King, Empty, Piece
from typing import List


class Chessboard:
    def __init__(self, screen = None, width = 1280, height = 720, position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") -> None:
        self.position = position
        self.board = self.initialize_board(self.position)
        self.send_board_to_pieces()
        self.white_pieces = self.board[-1] + self.board[-2]
        self.black_pieces = self.board[0] + self.board[1]
        self.white_points = 0
        self.black_points = 0
        self.calculate_points()
        self.halfmove_clock = 0
        self.log = []
        self.width = width
        self.height = height
        if screen == None:
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = screen
        
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.backgroundColor = self.white


    def __str__(self) -> str:
        # returns pretty board like this:
        # ———————————
        # | bR | bN |
        # ———————————
        # | -- | -- |
        # ———————————

        return "—"*41 + "\n" + "".join(["| " + " | ".join([piece.shortName for piece in row]) + " |\n" + "—"*41 + "\n" for row in self.board])

    def initialize_board(self, fen: str) -> List[Piece]:
        fen = fen.split()[0] + "/"
        board = []
        row = []
        for char in fen:
            if char == "/":
                board.append(row)
                row = []
                continue
            if char.isdigit():
                for _ in range(int(char)):
                    row.append(Empty(len(row), len(board), "empty"))

            if char.isalpha():
                if char == "r":
                    row.append(Rook(len(row), len(board), "black"))
                elif char == "n":
                    row.append(Knight(len(row), len(board), "black"))
                elif char == "b":
                    row.append(Bishop(len(row), len(board), "black"))
                elif char == "q":
                    row.append(Queen(len(row), len(board), "black"))
                elif char == "k":
                    row.append(King(len(row), len(board), "black"))
                elif char == "p":
                    row.append(Pawn(len(row), len(board), "black"))
                elif char == "R":
                    row.append(Rook(len(row), len(board), "white"))
                elif char == "N":
                    row.append(Knight(len(row), len(board), "white"))
                elif char == "B":
                    row.append(Bishop(len(row), len(board), "white"))
                elif char == "Q":
                    row.append(Queen(len(row), len(board), "white"))
                elif char == "K":
                    row.append(King(len(row), len(board), "white"))
                elif char == "P":
                    row.append(Pawn(len(row), len(board), "white"))

        return board

    def to_fen(self) -> str:
        fen = ""
        for row in self.board:
            empty_count = 0
            for piece in row:
                if isinstance(piece, Empty):
                    empty_count += 1
                else:
                    if empty_count != 0:
                        fen += str(empty_count)
                        empty_count = 0
                    fen += piece.letter
            if empty_count != 0:
                fen += str(empty_count)
            fen += "/"
        return fen[:-1]

    def send_board_to_pieces(self) -> None:
        for row in self.board:
            for piece in row:
                if not isinstance(piece, Empty):
                    piece.board = self.board
                    piece.moves = piece.get_moves()


    def calculate_points(self) -> None:
        self.white_points = 0
        self.black_points = 0
        for piece in self.white_pieces:
            self.white_points += piece.value
        for piece in self.black_pieces:
            self.black_points += piece.value


    def move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        piece = self.board[y1][x1]
        if piece.shortName == "--":
            return False

        attack = not isinstance(self.board[y2][x2], Empty)
        if (x2, y2) in piece.moves:
            if isinstance(piece, Pawn):
                self.halfmove_clock = -1
            if attack:
                if piece.color == "white":
                    self.black_pieces.remove(self.board[y2][x2])
                    self.halfmove_clock = -1
                else:
                    self.white_pieces.remove(self.board[y2][x2])
                    self.halfmove_clock = -1
                self.calculate_points()

            piece.x, piece.y = x2, y2
            self.board[y2][x2] = piece
            self.board[y1][x1] = Empty(x1, y1, "empty")
            self.send_board_to_pieces()
            self.log.append((x1, y1, x2, y2))
            piece.log.append((x2, y2))
            self.halfmove_clock += 1
            return True
        else:
            return False


    def draw(self) -> None:
        self.screen.fill(self.backgroundColor)
        for row in self.board:
            for piece in row:
                piece.draw(self.screen)
        pygame.display.flip()
