from classes import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

player_sprite = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
test_sprite = Object((200, 200))
all_sprites = pygame.sprite.Group()
all_sprites.add(test_sprite)
screen_fustrum = [[0, SCREEN_HEIGHT], [SCREEN_WIDTH, 0]]

while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w]:
        print("WAT")
        screen_fustrum[0][1] += 2
        screen_fustrum[1][1] += 2
    if pressed_keys[K_s]:
        screen_fustrum[0][1] -= 2
        screen_fustrum[1][1] -= 2
    if pressed_keys[K_a]:
        screen_fustrum[0][0] += 2
        screen_fustrum[1][0] += 2
    if pressed_keys[K_d]:
        screen_fustrum[0][0] -= 2
        screen_fustrum[1][0] -= 2
    print(screen_fustrum)
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
            screen.blit(
                sprite.surf,
                (
                    sprite.rect.x + screen_fustrum[0][0],
                    sprite.rect.y + screen_fustrum[0][1],
                ),
            )
    screen.blit(player_sprite.surf, player_sprite.rect)
    pygame.display.flip()
    clock.tick(FRAME_RATE)