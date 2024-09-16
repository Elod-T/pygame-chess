import pygame
from chessboard import Chessboard
from pieces import King


class Game:
    def __init__(self, width = 1280, height = 720) -> None:
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.chessboard = Chessboard(self.screen)
        self.clock = pygame.time.Clock()
        self.running = True
        self.white_turn = True
        self.log = []
        self.active = None
        self.white_pieces = self.chessboard.white_pieces
        self.black_pieces = self.chessboard.black_pieces
        self.white_points = self.chessboard.white_points
        self.black_points = self.chessboard.black_points
        self.fullmove_turn = 1

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        #self.font = pygame.font.SysFont("Arial", 20)

    def move_rook_after_castling(self) -> None:
        lastPos = self.active.log[-1]
        beforeLastPos = self.active.log[-2]
        print(lastPos, beforeLastPos)
        if lastPos[0] == beforeLastPos[0] + 2:
            rook = self.chessboard.board[self.active.y][self.active.x + 1]
            print(rook)
            self.chessboard.move(rook.x, rook.y, rook.x - 2, rook.y)

        elif lastPos[0] == beforeLastPos[0] - 2:
            rook = self.chessboard.board[self.active.y][self.active.x - 1]
            self.chessboard.move(rook.x, rook.y, rook.x + 3, rook.y)

    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.white_turn:
                    for piece in self.white_pieces:
                        if piece.is_clicked(*event.pos):
                            piece.get_moves()
                            self.active = piece
                            break

                    if self.active != None:
                        if self.active.is_move_clicked(*event.pos):
                            # move piece
                            x, y = self.active.coordinate_to_index(*event.pos)
                            self.chessboard.move(self.active.x, self.active.y, x, y)


                            # checks if its castling and moves the rook
                            if isinstance(self.active, King):
                                self.move_rook_after_castling()

                            # cleanup
                            self.active = None
                            self.white_turn = False
                            break

                else:
                    for piece in self.black_pieces:
                        if piece.is_clicked(*event.pos):
                            piece.get_moves()
                            self.active = piece
                            break

                    if self.active != None:
                        if self.active.is_move_clicked(*event.pos):
                            # move piece
                            x, y = self.active.coordinate_to_index(*event.pos)
                            self.chessboard.move(self.active.x, self.active.y, x, y)

                            # checks if its castling and moves the rook
                            if isinstance(self.active, King):
                                self.move_rook_after_castling()

                            # cleanup
                            self.active = None
                            self.white_turn = True
                            self.fullmove_turn += 1
                            break

    def get_fen(self) -> str:
        fen = self.chessboard.to_fen()
        active = "w" if self.white_turn else "b"
        castling = "KQkq" # TODO: implement castling
        en_passant = "-" # TODO: implement en passant
        halfmove_clock = str(self.chessboard.halfmove_clock)
        fullmove_number = str(self.fullmove_turn)
        return " ".join([fen, active, castling, en_passant, halfmove_clock, fullmove_number])




chess = Game()
while chess.running:
    chess.event_loop()
    chess.chessboard.draw()
    if chess.active != None:
        chess.active.show_moves(chess.screen)

    chess.clock.tick(60)
    pygame.display.flip()

    print(chess.get_fen())