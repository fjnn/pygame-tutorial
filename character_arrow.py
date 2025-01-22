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

        # grab keyboard input for left and right through a and d
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.x += 5
        elif keys[pygame.K_UP]:
            self.y -= 5
        elif keys[pygame.K_DOWN]:
            self.y += 5
        else:
            pass

        