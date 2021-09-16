try:
    num = int(input('Введите число: '))

except ValueError:
    print('Введены некорректные значения. Попробуйте снова')

else:
    if 10000 > num > 0:
        a1 = num // 1000
        a2 = (num // 100) % 10
        a3 = (num // 10) % 10
        a4 = num % 10

        if a1 != 0:
            if a1 == 1:
                print('Одна тысяча ', end='')
            elif a1 == 2:
                print('Две тысячи ', end='')
            elif a1 == 3:
                print('Три тысячи ', end='')
            elif a1 == 4:
                print('Четыре тысячи ', end='')
            elif a1 == 5:
                print('Пять тысяч ', end='')
            elif a1 == 6:
                print('Шесть тысяч ', end='')
            elif a1 == 7:
                print('Семь тысяч ', end='')
            elif a1 == 8:
                print('Восемь тысяч ', end='')
            elif a1 == 9:
                print('Девять тысяч ', end='')
            if a2 == 1:
                print('сто ', end='')
            elif a2 == 2:
                print('двести ', end='')
            elif a2 == 3:
                print('триста ', end='')
            elif a2 == 4:
                print('четыреста ', end='')
            elif a2 == 5:
                print('пятьсот ', end='')
            elif a2 == 6:
                print('шестьсот ', end='')
            elif a2 == 7:
                print('семьсот ', end='')
            elif a2 == 8:
                print('восемьсот ', end='')
            elif a2 == 9:
                print('девятьсот ', end='')
            if a3 == 1:
                if a4 == 1:
                    print('одиннадцать ', end='')
                elif a4 == 2:
                    print('двенадцать ', end='')
                elif a4 == 3:
                    print('тринадцать ', end='')
                elif a4 == 4:
                    print('четырнадцать ', end='')
                elif a4 == 5:
                    print('пятнадцать ', end='')
                elif a4 == 6:
                    print('шестнадцать ', end='')
                elif a4 == 7:
                    print('семнадцать ', end='')
                elif a4 == 8:
                    print('восемнадцать ', end='')
                elif a4 == 9:
                    print('девятнадцать ', end='')
                elif a4 == 0:
                    print('десять ', end='')
                print('рублей')

            else:
                if a3 == 2:
                    print('двадцать ', end='')
                elif a3 == 3:
                    print('тридцать ', end='')
                elif a3 == 4:
                    print('сорок ', end='')
                elif a3 == 5:
                    print('пятьдесят ', end='')
                elif a3 == 6:
                    print('шестьдесят ', end='')
                elif a3 == 7:
                    print('семьдесят ', end='')
                elif a3 == 8:
                    print('восемьдесят ', end='')
                elif a3 == 9:
                    print('девяносто ', end='')

                if a4 == 1:
                    print('один ', end='')
                elif a4 == 2:
                    print('два ', end='')
                elif a4 == 3:
                    print('три ', end='')
                elif a4 == 4:
                    print('четыре ', end='')
                elif a4 == 5:
                    print('пять ', end='')
                elif a4 == 6:
                    print('шесть ', end='')
                elif a4 == 7:
                    print('семь ', end='')
                elif a4 == 8:
                    print('восемь ', end='')
                elif a4 == 9:
                    print('девять ', end='')

                if a4 == 0 or a4 == 5 or a4 == 6 or a4 == 7 or a4 == 8 or a4 == 9:
                    print('рублей')
                elif a4 == 1:
                    print('рубль')
                else:
                    print('рубля')

        elif a1 == 0 and a2 != 0:
            if a2 == 1:
                print('Cто ', end='')
            elif a2 == 2:
                print('Двести ', end='')
            elif a2 == 3:
                print('Триста ', end='')
            elif a2 == 4:
                print('Четыреста ', end='')
            elif a2 == 5:
                print('Пятьсот ', end='')
            elif a2 == 6:
                print('Шестьсот ', end='')
            elif a2 == 7:
                print('Семьсот ', end='')
            elif a2 == 8:
                print('Восемьсот ', end='')
            elif a2 == 9:
                print('Девятьсот ', end='')
            if a3 == 1:
                if a4 == 1:
                    print('одиннадцать ', end='')
                elif a4 == 2:
                    print('двенадцать ', end='')
                elif a4 == 3:
                    print('тринадцать ', end='')
                elif a4 == 4:
                    print('четырнадцать ', end='')
                elif a4 == 5:
                    print('пятнадцать ', end='')
                elif a4 == 6:
                    print('шестнадцать ', end='')
                elif a4 == 7:
                    print('семнадцать ', end='')
                elif a4 == 8:
                    print('восемнадцать ', end='')
                elif a4 == 9:
                    print('девятнадцать ', end='')
                elif a4 == 0:
                    print('десять ', end='')
                print('рублей')

            else:
                if a3 == 2:
                    print('двадцать ', end='')
                elif a3 == 3:
                    print('тридцать ', end='')
                elif a3 == 4:
                    print('сорок ', end='')
                elif a3 == 5:
                    print('пятьдесят ', end='')
                elif a3 == 6:
                    print('шестьдесят ', end='')
                elif a3 == 7:
                    print('семьдесят ', end='')
                elif a3 == 8:
                    print('восемьдесят ', end='')
                elif a3 == 9:
                    print('девяносто ', end='')

                if a4 == 1:
                    print('один ', end='')
                elif a4 == 2:
                    print('два ', end='')
                elif a4 == 3:
                    print('три ', end='')
                elif a4 == 4:
                    print('четыре ', end='')
                elif a4 == 5:
                    print('пять ', end='')
                elif a4 == 6:
                    print('шесть ', end='')
                elif a4 == 7:
                    print('семь ', end='')
                elif a4 == 8:
                    print('восемь ', end='')
                elif a4 == 9:
                    print('девять ', end='')

                if a4 == 0 or a4 == 5 or a4 == 6 or a4 == 7 or a4 == 8 or a4 == 9:
                    print('рублей')
                elif a4 == 1:
                    print('рубль')
                else:
                    print('рубля')

        elif a1 == 0 and a2 == 0 and a3 != 0:
            if a3 == 1:
                if a4 == 1:
                    print('Одиннадцать ', end='')
                elif a4 == 2:
                    print('Двенадцать ', end='')
                elif a4 == 3:
                    print('Тринадцать ', end='')
                elif a4 == 4:
                    print('Четырнадцать ', end='')
                elif a4 == 5:
                    print('Пятнадцать ', end='')
                elif a4 == 6:
                    print('Шестнадцать ', end='')
                elif a4 == 7:
                    print('Семнадцать ', end='')
                elif a4 == 8:
                    print('Восемнадцать ', end='')
                elif a4 == 9:
                    print('Девятнадцать ', end='')
                elif a4 == 0:
                    print('Десять ', end='')
                print('рублей')

            else:
                if a3 == 2:
                    print('Двадцать ', end='')
                elif a3 == 3:
                    print('Тридцать ', end='')
                elif a3 == 4:
                    print('Сорок ', end='')
                elif a3 == 5:
                    print('Пятьдесят ', end='')
                elif a3 == 6:
                    print('Шестьдесят ', end='')
                elif a3 == 7:
                    print('Семьдесят ', end='')
                elif a3 == 8:
                    print('Восемьдесят ', end='')
                elif a3 == 9:
                    print('Девяносто ', end='')

                if a4 == 1:
                    print('один ', end='')
                elif a4 == 2:
                    print('два ', end='')
                elif a4 == 3:
                    print('три ', end='')
                elif a4 == 4:
                    print('четыре ', end='')
                elif a4 == 5:
                    print('пять ', end='')
                elif a4 == 6:
                    print('шесть ', end='')
                elif a4 == 7:
                    print('семь ', end='')
                elif a4 == 8:
                    print('восемь ', end='')
                elif a4 == 9:
                    print('девять ', end='')

                if a4 == 0 or a4 == 5 or a4 == 6 or a4 == 7 or a4 == 8 or a4 == 9:
                    print('рублей')
                elif a4 == 1:
                    print('рубль')
                else:
                    print('рубля')
        else:
            if a4 == 1:
                print('Один ', end='')
            elif a4 == 2:
                print('Два ', end='')
            elif a4 == 3:
                print('Три ', end='')
            elif a4 == 4:
                print('Четыре ', end='')
            elif a4 == 5:
                print('Пять ', end='')
            elif a4 == 6:
                print('Шесть ', end='')
            elif a4 == 7:
                print('Семь ', end='')
            elif a4 == 8:
                print('Восемь ', end='')
            elif a4 == 9:
                print('Девять ', end='')

            if a4 == 0 or a4 == 5 or a4 == 6 or a4 == 7 or a4 == 8 or a4 == 9:
                print('рублей')
            elif a4 == 1:
                print('рубль')
            else:
                print('рубля')

    else:
        print('Число не попадает в диапазон [1;9999]')
