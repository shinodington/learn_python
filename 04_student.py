# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
month = 1
total_expenses = 0
while month <= 10:
    total_expenses += expenses
    expenses = round(expenses * 1.03, 2)
    month += 1
total_educational_grant = educational_grant * 10
parent_help = total_expenses - total_educational_grant
print('Студенту надо поросить', round(parent_help, 2), 'рублей')