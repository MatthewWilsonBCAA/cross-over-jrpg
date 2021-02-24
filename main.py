from classes import *
from worlds import *
import moves
import copy
import time

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Cross-over JRPG")
# icon = pygame.image.load()
# pygame.display.set_icon(icon)
damage = 0
running = True

is_battle = False
attack_timer = 0

player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
for obj in test_arena:
    test_sprite = Object(obj[0], obj[1])
    all_sprites.add(test_sprite)
    if obj[2]:
        walls.add(test_sprite)

screen_fustrum = [[0, SCREEN_HEIGHT], [SCREEN_WIDTH, 0]]

base_entity = [
    500,
    500,
    40,
    60,
    20,
    [moves.FireBall, moves.Rage, moves.CloseCombat, moves.IceBeam],
    ["dragon_front.png", "dragon_back.png"]
]
e_player = None
enemy = None
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    if not is_battle and pressed_keys[K_b]:
        is_battle = True
        # initializes entities
        e_player = Fighter(
            (200, SCREEN_HEIGHT - 200),
            base_entity[0],
            base_entity[1],
            base_entity[2],
            base_entity[3],
            base_entity[4],
            base_entity[5],
            base_entity[6][1]
        )
        enemy = Fighter(
            (SCREEN_WIDTH - 200, 200),
            base_entity[0],
            base_entity[1],
            base_entity[2],
            base_entity[3],
            base_entity[4],
            base_entity[5],
            base_entity[6][0]
        )
    if not is_battle and pressed_keys[K_w]:
        screen_fustrum[0][1] += MOVEMENT_SPEED
        screen_fustrum[1][1] += MOVEMENT_SPEED
        for wall in walls:
            temp = copy.copy(wall)
            temp.rect = wall.rect.copy()
            temp.rect = temp.surf.get_rect(
                center=(
                    temp.rect.center[0] + screen_fustrum[0][0],
                    temp.rect.center[1] + screen_fustrum[0][1],
                )
            )
            HITS = pygame.sprite.collide_rect(player, temp)
            if HITS:
                screen_fustrum[0][1] -= MOVEMENT_SPEED
                screen_fustrum[1][1] -= MOVEMENT_SPEED
    if not is_battle and pressed_keys[K_s]:
        screen_fustrum[0][1] -= MOVEMENT_SPEED
        screen_fustrum[1][1] -= MOVEMENT_SPEED
        for wall in walls:
            temp = copy.copy(wall)
            temp.rect = wall.rect.copy()
            temp.rect = temp.surf.get_rect(
                center=(
                    temp.rect.center[0] + screen_fustrum[0][0],
                    temp.rect.center[1] + screen_fustrum[0][1],
                )
            )
            HITS = pygame.sprite.collide_rect(player, temp)
            if HITS:
                screen_fustrum[0][1] += MOVEMENT_SPEED
                screen_fustrum[1][1] += MOVEMENT_SPEED
    if not is_battle and pressed_keys[K_a]:
        screen_fustrum[0][0] += MOVEMENT_SPEED
        screen_fustrum[1][0] += MOVEMENT_SPEED
        for wall in walls:
            temp = copy.copy(wall)
            temp.rect = wall.rect.copy()
            temp.rect = temp.surf.get_rect(
                center=(
                    temp.rect.center[0] + screen_fustrum[0][0],
                    temp.rect.center[1] + screen_fustrum[0][1],
                )
            )
            HITS = pygame.sprite.collide_rect(player, temp)
            if HITS:
                screen_fustrum[0][0] -= MOVEMENT_SPEED
                screen_fustrum[1][0] -= MOVEMENT_SPEED
    if not is_battle and pressed_keys[K_d]:
        screen_fustrum[0][0] -= MOVEMENT_SPEED
        screen_fustrum[1][0] -= MOVEMENT_SPEED
        for wall in walls:
            temp = copy.copy(wall)
            temp.rect = wall.rect.copy()
            temp.rect = temp.surf.get_rect(
                center=(
                    temp.rect.center[0] + screen_fustrum[0][0],
                    temp.rect.center[1] + screen_fustrum[0][1],
                )
            )
            HITS = pygame.sprite.collide_rect(player, temp)
            if HITS:
                screen_fustrum[0][0] += MOVEMENT_SPEED
                screen_fustrum[1][0] += MOVEMENT_SPEED
    # print(screen_fustrum)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    for sprite in all_sprites:
        if is_battle:
            break
        isk = False
        le = sprite.rect.left
        ye = sprite.rect.bottom
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
    if not is_battle:
        screen.blit(player.surf, player.rect)
    else:  # this is the actual main battle code
        screen.blit(e_player.surf, e_player.rect)
        screen.blit(enemy.surf, enemy.rect)
        player_texts = [
            f"4. {e_player.move_list[3][3]}",
            f"3. {e_player.move_list[2][3]}",
            f"2. {e_player.move_list[1][3]}",
            f"1. {e_player.move_list[0][3]}",
            f"{e_player.hp} / {e_player.max_hp}",
            "Player",
        ]
        enemy_texts = [f"{enemy.hp} / {enemy.max_hp}", "Enemy"]
        ty = 100
        for text in player_texts:
            screen.blit(
                font.render(text, True, (255, 255, 0)),
                (SCREEN_WIDTH - 300, SCREEN_HEIGHT - ty),
            )
            ty += 25
        ty = 25
        for text in enemy_texts:
            screen.blit(font.render(text, True, (255, 255, 0)), (100, ty))
            ty += 25
        if attack_timer > 0:
            if damage == 0:
                screen.blit(
                    font.render("Missed!", True, (255, 255, 0)),
                    (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                )
            attack_timer -= 1
        if attack_timer == 250:
            choice = random.randint(1,4)
            e_damage = enemy.use_move(choice, e_player.defense)
            e_player.hp -= int(e_damage)
        attack_input = None
        if pressed_keys[K_1]:
            attack_input = 1
        if pressed_keys[K_2]:
            attack_input = 2
        if pressed_keys[K_3]:
            attack_input = 3
        if pressed_keys[K_4]:
            attack_input = 4
        if attack_input and attack_timer == 0:
            damage = e_player.use_move(attack_input, enemy.defense)
            # print(damage)
            enemy.hp -= int(damage)
            if enemy.hp <= 0:
                is_battle = False
            attack_timer = 500
            # time.sleep(2)

    pygame.display.flip()
    clock.tick(FRAME_RATE)