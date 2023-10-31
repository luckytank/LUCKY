import pygame
import random

# 初始化Pygame
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 颜色定义
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("射击游戏")

# 玩家相关设置
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 5

# 敌人相关设置
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = 0
enemy_speed = 3

# 初始化分数
score = 0

# 游戏循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 移动玩家
    if player_x < 0:
        player_x = 0
    if player_x > window_width - player_width:
        player_x = window_width - player_width

    # 移动敌人
    enemy_y += enemy_speed
    if enemy_y > window_height:
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = 0
        score += 1

    # 检测碰撞
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        running = False

    # 渲染背景
    screen.fill(white)

    # 渲染玩家
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    # 渲染敌人
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

    # 渲染分数
    font = pygame.font.Font(None, 36)
    text = font.render("分数: " + str(score), True, blue)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
