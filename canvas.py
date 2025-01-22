# Example file showing a basic pygame "game loop"
import pygame
from character_wasd import Character as Character_wasd
from character_arrow import Character as Character_arrow

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

character1 = Character_wasd(screen, 200, 200, 20)
character2 = Character_arrow(screen, 400, 400, 20)

def update():
    character1.update()
    character2.update()

    if abs(character1.x - character2.x) < 10 and abs(character1.y - character2.y) < 10:
        character1.color = "green"
        character2.color = "black"

    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked_pos = pygame.mouse.get_pos()
            character1.x = mouse_clicked_pos[0]
            character1.y = mouse_clicked_pos[1]

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("seashell4")

    update()   

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()