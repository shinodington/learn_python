# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
x_resol = 400
y_resol = 400
sd.resolution = (x_resol, y_resol)
sd.background_color = (sd.COLOR_WHITE)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x_dimension = 40
y_dimension = 20
for y in range(0, y_resol, y_dimension):
    for x in range (0, x_resol, x_dimension):
        left_bottom = sd.get_point(x = x, y = y)
        top_right = sd.get_point(x = x + x_resol, y = y + y_resol)
        sd.rectangle(left_bottom=left_bottom, right_top=top_right, color=sd.random_color(), width=0)

sd.pause()
