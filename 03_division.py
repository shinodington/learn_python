# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

# insert variable c to output initial dimensions. variable celoe count how much
# times we can summ b, before we owerpass a
a, b = 37, 179

c = b

celoe = 0
while a >= c:
    c += b
    celoe += 1
print('целочисленное деление', a, 'на', b, 'дает', celoe)