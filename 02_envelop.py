# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

#envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9
# проверить для
#paper_x, paper_y = 9, 8
#paper_x, paper_y = 6, 8
#paper_x, paper_y = 8, 6
#paper_x, paper_y = 3, 4
#paper_x, paper_y = 11, 9
#paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

# compare 2 dimensions. both must be less than envelop variable
# dosent matter what side x or y to paper, we can spin it in 2 dimensions
#if paper_x <= envelop_x:
#    if paper_y <= envelop_y:
#        print('Da')
#    elif paper_x <= envelop_y:
#        if paper_y <= envelop_x:
#            print('Da')
#    else:
#        print('Net')
#else:
#    print('net')
# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
#brick_x, brick_y, brick_z = 11, 10, 2
#brick_x, brick_y, brick_z = 11, 2, 10
#brick_x, brick_y, brick_z = 10, 11, 2
#brick_x, brick_y, brick_z = 10, 2, 11
#brick_x, brick_y, brick_z = 2, 10, 11
#brick_x, brick_y, brick_z = 2, 11, 10
#brick_x, brick_y, brick_z = 3, 5, 6
#brick_x, brick_y, brick_z = 3, 6, 5
#brick_x, brick_y, brick_z = 6, 3, 5
#brick_x, brick_y, brick_z = 6, 5, 3
#brick_x, brick_y, brick_z = 5, 6, 3
#brick_x, brick_y, brick_z = 5, 3, 6
#brick_x, brick_y, brick_z = 11, 3, 6
#brick_x, brick_y, brick_z = 11, 6, 3
#brick_x, brick_y, brick_z = 6, 11, 3
#brick_x, brick_y, brick_z = 6, 3, 11
#brick_x, brick_y, brick_z = 3, 6, 11
brick_x, brick_y, brick_z = 3, 11, 6
#(просто раскоментировать нужную строку и проверить свой код)
# compare two dimensions. (x and x) & ((y and y) or (z and y)). analog
# for other setup. brick can be spin in 3 dimensions? so we make 3 compare
if brick_x <= hole_x:
    if brick_y <= hole_y:
        print('da')
    elif brick_z <= hole_y:
        print('da')
    else:
        print('net')
elif brick_y <= hole_x:
    if brick_x <= hole_y:
        print('da')
    elif brick_z <= hole_y:
        print('da')
    else:
        print('net')
elif brick_z <= hole_x:
    if brick_x <= hole_y:
        print('da')
    elif brick_y <= hole_y:
        print('da')
    else:
        print('net')
else:
    print('net')
