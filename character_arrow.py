import pygame


class Character:
    def __init__(self, screen, x, y, size) -> None:
        self.screen = screen
        # self.color = (255, 0, 0)
        self.images = []
        self.images.append(pygame.image.load("assets/hotdog.png").convert_alpha())
        self.images.append(pygame.image.load("assets/hotdog2.png").convert_alpha())
        self.images = [pygame.transform.scale(img, (100, 100)) for img in self.images]
        self.x = x
        self.y = y
        self.size = size

    def update(self):
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
        self.screen.blit(self.images[pygame.time.get_ticks()%2], (self.x, self.y))

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

        