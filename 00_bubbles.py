# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

#point = sd.get_point(x = 100, y = 100)
#radius = 50
#for _ in range(3):
#    step = 5
#    radius += step
#    sd.circle(point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

#def puz_param(point, step):
#    radius = 50
#    for _ in range(3):
#        radius += step
#        sd.circle(point, radius=radius)
#
#point = sd.get_point(x = 100, y = 100)
#puz_param(point = point, step = 5)

# Нарисовать 10 пузырьков в ряд

#def puz_param(point):
#    radius = 50
#    for _ in range(3):
#        sd.circle(point, radius=radius)
#for x in range (100, 1001, 100):
#    point = sd.get_point(x = x, y = 100)
#    puz_param(point = point)

# Нарисовать три ряда по 10 пузырьков

#def puz_param(point):
#    radius = 50
#    for _ in range(3):
#        sd.circle(point, radius=radius)
#
#for x in range (100, 1001, 100):
#    for y in range (100, 301, 100):
#        point = sd.get_point(x = x, y = y)
#        puz_param(point = point)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

def puz_param(point, color):
    radius = 50
    sd.circle(point, radius = radius, color = color)


for _ in range (101):
    color = sd.random_color()
    point = sd.random_point()
    print(point)
    puz_param(point = point, color = color)
sd.pause()


