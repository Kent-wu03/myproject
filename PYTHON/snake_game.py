import pygame,random

pygame.init()

set_fs = pygame.display.Info()
lebar = set_fs.current_w;panjang = set_fs.current_h
b_color = (127,0,255);hijau = (0, 255, 0);merah = (255, 0, 0);putih = (255, 255, 255);hitam = (0, 0, 0)
set_grid = min(lebar, panjang) // 25
lebar_game, panjang_game = lebar, panjang - (panjang // 4)
lebar_grid,panjang_grid = lebar_game // set_grid, panjang_game // set_grid
snake = [(5, 5)];direction = (1, 0)
score, win_score = 0, 8
apel = (random.randint(1, lebar_grid - 2), random.randint(1, panjang_grid - 2))
layar = pygame.display.set_mode((lebar, panjang));frame = pygame.time.Clock()
b_size = panjang // 14;distance = b_size // 2;center_x = lebar // 2;center_y = panjang_game + (panjang - panjang_game) // 2
w_button = pygame.Rect(center_x, center_y - distance - b_size, b_size, b_size)
a_button = pygame.Rect(center_x - distance - b_size, center_y, b_size, b_size)
s_button= pygame.Rect(center_x, center_y, b_size, b_size)
d_button = pygame.Rect(center_x + distance + b_size, center_y, b_size, b_size)
batas = pygame.Rect(0, panjang_game, lebar, panjang - panjang_game)

def draw_button():
    pygame.draw.rect(layar, b_color, w_button, border_radius=15)
    pygame.draw.rect(layar, b_color, a_button, border_radius=15)
    pygame.draw.rect(layar, b_color, s_button, border_radius=15)
    pygame.draw.rect(layar, b_color, d_button, border_radius=15)

    font = pygame.font.Font(None, b_size // 2)
    layar.blit(font.render("W", True, putih), (w_button.x + b_size // 3, w_button.y + b_size // 4))
    layar.blit(font.render("A", True, putih), (a_button.x + b_size // 3, a_button.y + b_size // 4))
    layar.blit(font.render("S", True, putih), (s_button.x + b_size // 3, s_button.y + b_size // 4))
    layar.blit(font.render("D", True, putih), (d_button.x + b_size // 3, d_button.y + b_size // 4))

start = True
while start:
    layar.fill(hitam)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if w_button.collidepoint(event.pos) and direction != (0, 1):
                direction = (0, -1)
            elif a_button.collidepoint(event.pos) and direction != (1, 0):
                direction = (-1, 0)
            elif s_button.collidepoint(event.pos) and direction != (0, -1):
                direction = (0, 1)
            elif d_button.collidepoint(event.pos) and direction != (-1, 0):
                direction = (1, 0)

    head_body = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head_body)

    if (snake[0][0] < 0 or snake[0][0] >= lebar_grid or
            snake[0][1] < 0 or snake[0][1] >= panjang_grid or
            snake[0] in snake[1:] or
            batas.collidepoint(snake[0][0] * set_grid, snake[0][1] * set_grid)):
        layar.fill(merah)
        lose_text = font.render("KAMU KALAH", True, putih)
        layar.blit(lose_text, (lebar // 2 - 50, panjang // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        start = False

    if snake[0] == apel:
        score += 1
        apel = (random.randint(1, lebar_grid - 2), random.randint(1, panjang_grid - 2))
    else:
        snake.pop()

    for bagian in snake:
        pygame.draw.rect(layar, hijau, (bagian[0] * set_grid, bagian[1] * set_grid, set_grid, set_grid))

    pygame.draw.rect(layar, merah, (apel[0] * set_grid, apel[1] * set_grid, set_grid, set_grid))
    pygame.draw.line(layar, putih, (0, panjang_game), (lebar, panjang_game), 5)
    draw_button()
    font = pygame.font.Font(None, 50)
    score_text = font.render(f"SCORE: {score}/{win_score}", True, putih)
    layar.blit(score_text, (10, 10))

    if score == win_score:
        layar.fill(hijau)
        win_text = font.render("KAMU MENANG", True, putih)
        layar.blit(win_text, (lebar // 2 - 50, panjang // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        start = False
    pygame.display.flip()
    frame.tick(9)
pygame.quit()
