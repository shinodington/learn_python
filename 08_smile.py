# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
x_resol = 400
y_resol = 400
sd.resolution = (x_resol, y_resol)
sd.background_color = (sd.COLOR_WHITE)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# def smile draw smile with variable x,y_dim - dimensions of face, 
# eye point simmetric from central y-line
# mouth start-stop simmetric from y line
def smile(x, y, color):
    x_dim = 50
    y_dim = 40
    width = 3
    start_head = sd.get_point(x = x - x_dim//2, y = y - y_dim//2)
    finish_head = sd.get_point(x = x + x_dim//2, y = y + y_dim//2)
    left_eye = sd.get_point(x = x - x_dim//4, y = y + y_dim//4)
    right_eye = sd.get_point(x = x + x_dim//4, y = y + y_dim//4)
    mouth_start = sd.get_point(x = x - x_dim//4, y = y - y_dim//4)
    mouth_finish = sd.get_point(x = x + x_dim//4, y = y - y_dim//4)
    sd.circle(center_position=left_eye, radius=10, color=color,  width=0)
    sd.circle(center_position=right_eye, radius=10, color=color, width=0)
    sd.ellipse(left_bottom=start_head, right_top=finish_head, color=color, width = width)
    sd.line(start_point=mouth_start, end_point=mouth_finish, color=color, width=width)

for _ in range (10):
    x = sd.random_number(a=0, b=x_resol)
    y = sd.random_number(a=0, b=y_resol)
    print(x , y)
    smile(x = x, y = y, color = sd.random_color())
sd.pause()
