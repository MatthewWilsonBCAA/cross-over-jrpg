from classes import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

test_sprite = Object((200, 200))
all_sprites = pygame.sprite.Group()
all_sprites.add(test_sprite)
screen_fustrum = [[0, SCREEN_HEIGHT], [SCREEN_WIDTH, 0]]

while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w]:
        screen_fustrum[0][1] += 1
        screen_fustrum[1][1] += 1
    if pressed_keys[K_s]:
        screen_fustrum[0][1] -= 1
        screen_fustrum[1][1] -= 1
    if pressed_keys[K_a]:
        screen_fustrum[0][0] -= 1
        screen_fustrum[1][0] -= 1
    if pressed_keys[K_d]:
        screen_fustrum[0][0] += 1
        screen_fustrum[1][0] += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    for sprite in all_sprites:
        isk = False
        le = sprite.rect.left
        ye = sprite.rect.top
        re = sprite.rect.right
        be = sprite.rect.bottom
        if re >= screen_fustrum[0][0]:
            isk = True
        elif be <= screen_fustrum[0][1]:
            isk = True
        elif le <= screen_fustrum[1][0]:
            isk = True
        elif ye >= screen_fustrum[1][1]:
            isk = True
        if isk:
            screen.blit(sprite.surf, sprite.rect)
    pygame.display.flip()
    clock.tick(FRAME_RATE)