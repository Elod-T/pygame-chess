from .piece import Piece

class Empty(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.shortName = "--"
          
        