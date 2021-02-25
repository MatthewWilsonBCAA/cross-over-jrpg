from classes import *
from worlds import *
import basecharacters
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
e_damage = 0
damage = 0
is_player_turn = True
battle_state_text = "Your turn!"

player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
for obj in test_arena:
    test_sprite = Object(obj[0], obj[1])
    all_sprites.add(test_sprite)
    if obj[2]:
        walls.add(test_sprite)

screen_fustrum = [[0, SCREEN_HEIGHT], [SCREEN_WIDTH, 0]]

e_player = None
enemy = None
while running:
    screen.fill((0, 0, 0))
    pressed_keys = pygame.key.get_pressed()
    if not is_battle and pressed_keys[K_b]:
        is_battle = True
        # initializes entities
        ep = list(basecharacters.dragon)
        ee = list(basecharacters.ladybug)
        e_player = Fighter(
            (200, SCREEN_HEIGHT - 200),
            ep[0],
            ep[1],
            ep[2],
            ep[3],
            ep[4],
            ep[5],
            ep[6][1],
            ep[6][2]
        )
        enemy = Fighter(
            (SCREEN_WIDTH - 200, 200),
            ee[0],
            ee[1],
            ee[2],
            ee[3],
            ee[4],
            ee[5],
            ee[6][0],
            ee[6][2]
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
            f"{e_player.name}",
        ]
        enemy_texts = [f"{enemy.name}",f"{enemy.hp} / {enemy.max_hp}"]
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
        screen.blit(
            font.render(battle_state_text, True, (255, 255, 0)),
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        )
        attack_input = None
        if pressed_keys[K_1]:
            attack_input = 1
        if pressed_keys[K_2]:
            attack_input = 2
        if pressed_keys[K_3]:
            attack_input = 3
        if pressed_keys[K_4]:
            attack_input = 4
        if attack_timer == 0:
            battle_state_text = "Your turn!"
        if attack_input and attack_timer == 0:
            battle_state_text = "Your turn!"
            attack_timer = 500
            damage = 0
            damage = e_player.use_move(attack_input, enemy.defense)
            if damage > 0:
                anim = AttackAnimation("splatter.png", 0, (enemy.rect.x + 100, enemy.rect.y + 100))
            else:
                damage = 0
                anim = None
                is_player_turn = False
        if attack_timer > 0:
            if anim:
                finish = anim.play_animation()
                screen.blit(anim.surf, anim.rect)
                if finish == 1:
                    enemy.hp -= int(damage)
                    damage = 0
                    finish = 0
                    is_player_turn = False
            if not is_player_turn:
                battle_state_text = "Their turn..."
                choice = random.randint(1,4)
                e_damage = enemy.use_move(choice, e_player.defense)
                if e_damage > 0:
                    anim = AttackAnimation("splatter.png", 0, (e_player.rect.x + 100, e_player.rect.y + 100))
                else:
                    e_damage = 0
                    anim = None
                is_player_turn = True
            if e_damage > 0 and attack_timer == 1:
                e_player.hp -= int(e_damage)
                if e_player.hp <= 0:
                    running = False
            attack_timer -= 1
        if attack_timer == 1:
            battle_state_text = "Your turn!"
            e_player.hp -= int(e_damage)

    pygame.display.flip()
    clock.tick(FRAME_RATE)