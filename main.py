import pygame
import math


def draw():
    screen.fill('black')
    draw_text()

    pygame.draw.circle(screen, get_circle_color(0), get_circle_center(0), radius)
    pygame.draw.circle(screen, get_circle_color(120), get_circle_center(120), radius)
    pygame.draw.circle(screen, get_circle_color(240), get_circle_center(240), radius)

    pygame.draw.circle(screen, get_circle_color2(-30), get_circle_center(-30), radius * 0.75)
    pygame.draw.circle(screen, get_circle_color2(-150), get_circle_center(-150), radius * 0.75)
    pygame.draw.circle(screen, get_circle_color2(-270), get_circle_center(-270), radius * 0.75)

    pygame.draw.circle(screen, get_circle_color3(-60), get_circle_center(-60), radius // 2)
    pygame.draw.circle(screen, get_circle_color3(-180), get_circle_center(-180), radius // 2)
    pygame.draw.circle(screen, get_circle_color3(-300), get_circle_center(-300), radius // 2)


def update(delta):
    global angle
    angle = (angle + 180 * delta) % 360


def draw_text():
    font = pygame.font.Font(None, 35)

    text = font.render('Загрузка игры' + '.' * int(angle // 90), True, get_circle_color(0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 10 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    text2 = font.render('Рисуем главное меню' + '.' * int(angle // 90), True, get_circle_color(120))
    text2_x = width // 2 - text2.get_width() // 2
    text2_y = height // 10 * 9 - text.get_height() // 2
    screen.blit(text2, (text2_x, text2_y))


def get_circle_center(n):
    circle_angle = (angle + n) % 360
    x = math.cos(math.radians(circle_angle)) * distance + width / 2
    y = math.sin(math.radians(circle_angle)) * distance + height / 2

    return x, y


def get_circle_color(n):
    color = pygame.color.Color('red')
    circle_angle = (angle + n) % 360
    color.hsla = circle_angle, *color.hsla[1:]

    return color


def get_circle_color2(n):
    color = pygame.color.Color('red')
    circle_angle = (angle + n) % 360
    color.hsva = circle_angle, color.hsva[1], 50, color.hsva[3]

    return color


def get_circle_color3(n):
    color = pygame.color.Color('red')
    circle_angle = (angle + n) % 360
    color.hsva = circle_angle, color.hsva[1], 25, color.hsva[3]

    return color


if __name__ == "__main__":
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)

    running = True
    clock = pygame.time.Clock()

    angle = 0
    distance = 100
    radius = 20

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        delta = clock.tick() / 1500
        update(delta)

        draw()
        pygame.display.flip()
    pygame.quit()
