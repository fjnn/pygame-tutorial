import pygame

class Character:
    def __init__(self, screen, x, y, size) -> None:
        self.screen = screen
        self.color = (255, 0, 0)
        self.x = x
        self.y = y
        self.size = size

    def update(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
