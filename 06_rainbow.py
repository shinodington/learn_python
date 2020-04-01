# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (400, 500)
sd.background_color = (sd.COLOR_WHITE)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
x = 50
y = 50
width = 4
for color in rainbow_colors:
    start = sd.get_point(x=x, y=y)
    finish = sd.get_point(x=x+300, y=y+400)
    sd.line(start, finish, color=color, width=width)
    x += width
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
