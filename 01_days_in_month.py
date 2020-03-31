# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

year = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'augist',
'september', 'october', 'november', 'december']
# check correct month number inputed
# then print  month name from list -1 because list from 0 to 11
# feb is second month so check it first to print 28 days
# count of days in other month we can deside by division month number by 2
# but in october, november and december this division will be !=to print correct dayc number
if 0 < month <= 12:
    print(year[month - 1])
    key = month % 2
    if month == 2:
        print('28 days')
    elif month >= 10:
        if key == 1:
            print('30 days')
        else:
            print('31 days')
    elif month < 10:
        if key == 1:
            print('31 days')
        else:
            print('30 days')
else:
    print('incorrect month number')
