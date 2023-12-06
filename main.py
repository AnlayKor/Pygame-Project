import pygame
import math


def draw():
    screen.fill('black')
    draw_text()

    pygame.draw.circle(screen, get_circle_color(0), get_circle_center(0), radius)
    pygame.draw.circle(screen, get_circle_color(120), get_circle_center(120), radius)
    pygame.draw.circle(screen, get_circle_color(240), get_circle_center(240), radius)


def update(delta):
    global angle
    angle = (angle + 180 * delta) % 360


def draw_text():
    font = pygame.font.Font(None, 40)
    text = font.render('Загрузка' + '.' * int(angle // 90), True, get_circle_color(0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 10 * 9 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


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

        delta = clock.tick() / 1000
        update(delta)

        draw()
        pygame.display.flip()
    pygame.quit()
