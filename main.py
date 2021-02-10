from classes import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

test_sprite = Object((200, 200))

while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(test_sprite.surf, test_sprite.rect)
    pygame.display.flip()
    clock.tick(FRAME_RATE)