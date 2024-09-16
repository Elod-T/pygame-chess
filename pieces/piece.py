import pygame
from uuid import uuid4
from typing import List, Tuple


class Piece:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.board = []
        self.moves = []
        self.log = [(self.x, self.y)]
        self.ID = uuid4()
        self.shortName = self.color[0] + self.__class__.__name__[0]
        self.letter = self.__class__.__name__[0] if self.color == "white" else self.__class__.__name__[0].lower()
        self.value = 0
        self.has_moved = False
        self.image_size = 50
        self.x_correction = 400
        self.y_correction = 100

    def __str__(self) -> str:
        return f"{self.__class__.__name__} at x = {self.x}, y = {self.y}"

    def get_moves(self) -> List[Tuple[int, int]]:
        return [] 

    def draw(self, screen: pygame.Surface) -> None:
        if self.__class__.__name__ in ["Empty", "Piece"]:
            return

        path = f"/home/elod/programok/python/pygame/chess/pictures/{self.shortName}.png"

        img = pygame.image.load(path)

        img = pygame.transform.scale(img, (self.image_size, self.image_size))

        screen.blit(img, (self.x * 64 + self.x_correction, self.y * 64 + self.y_correction))

    def is_clicked(self, x: int, y: int) -> bool:
        if x > self.x * 64 + self.x_correction and x < self.x * 64 + self.x_correction + self.image_size:
            if y > self.y * 64 + self.y_correction and y < self.y * 64 + self.y_correction + self.image_size:
                return True
        return False

    def is_move_clicked(self, x: int, y: int) -> bool:
        for move in self.moves:
            if x > move[0] * 64 + self.x_correction and x < move[0] * 64 + self.x_correction + self.image_size:
                if y > move[1] * 64 + self.y_correction and y < move[1] * 64 + self.y_correction + self.image_size:
                    return True
        return False

    def show_moves(self, screen: pygame.Surface) -> None:
        for move in self.moves:
            pygame.draw.circle(screen, (0, 0, 255), (move[0] * 64 + self.x_correction + self.image_size // 2, move[1] * 64 + self.y_correction + self.image_size // 2), 5)

    def coordinate_to_index(self, x: int, y: int) -> Tuple[int, int]:
        return (x - self.x_correction) // 64, (y - self.y_correction) // 64