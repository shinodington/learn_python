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
# TODO здесь ваш код
def puz_param(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius=radius)

point = sd.get_point(x = 100, y = 100)
puz_param(point = point, step = 5)
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


