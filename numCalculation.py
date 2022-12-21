class numCalculation:
    #x = int(input())
    #binarna to desyatkova
    def bin_dec(data):
        number = 0
        len_dat = len(data)
        for i in range(0, len_dat):
            number += int(data[i]) * (2 ** (len_dat - i - 1))

        return number

    def myrevers(num):
        n1 = num
        n2 = 0

        while n1 > 0:
            # находим остаток - последнюю цифру
            digit = n1 % 10
            # делим нацело - удаляем последнюю цифру
            n1 = n1 // 10
            # увеличиваем разрядность второго числа
            n2 = n2 * 10
            # добавляем очередную цифру
            n2 = n2 + digit

        return n2

    #Десяткова в бінарну ввести число
    bin(10)
    #16кова в двійкову число, система
    bin(int('10', 16))
    #преобразование целого числа в шестнадцатеричную строку.
    hex(10)
    #преобразование целого числа в восьмеричную строку.
    oct(10)
    # ZM приклад на 5 перевести в двійкову буде 101, якщо число займає 3з4х бітів додаємо ще один біт де 0 = + а 1 = - топто 0101 = 5 1101 = -5
    #також приклад на 15 це 1111 занято 4 з 4 бітів, перетворюєм в 8біт додавши 3 0: 0001111 і тепер додаємо 0 або 1 00001111(ZM) = 15 \ 10001111(ZM)= -15
    def zmu1u2(num):
        def myrevers(num):
            n1 = num
            n2 = 0

            while n1 > 0:
                # находим остаток - последнюю цифру
                digit = n1 % 10
                # делим нацело - удаляем последнюю цифру
                n1 = n1 // 10
                # увеличиваем разрядность второго числа
                n2 = n2 * 10
                # добавляем очередную цифру
                n2 = n2 + digit

            return n2

        x = num
        x_bin = bin(int(x))
        x_bin = x_bin.replace("0b", "", 1)
        x_first_symbol = x_bin[0]
        x_len = len(x_bin)
        print(f"{x_bin} (2)")
        if x_first_symbol == "-":
            if x_len <= 4:
                x_bin_without_minus = x_bin.replace("-", "", 1)
                x_len_without_minus = len(x_bin_without_minus)
                n = 4 - x_len_without_minus
                zm_minus = "0" * n + x_bin_without_minus
                zm_minus = zm_minus.replace("0", "1", 1)
                print(f"{zm_minus}  ZM")
            elif x_len >= 4 and x_len < 9:
                x_bin_without_minus = x_bin.replace("-", "", 1)
                x_len_without_minus = len(x_bin_without_minus)
                n = 8 - x_len_without_minus
                zm_minus = "0" * n + x_bin_without_minus
                zm_minus = zm_minus.replace("0", "1", 1)
                print(f"{zm_minus}  ZM")
        elif x_first_symbol == "1" or x_first_symbol == "0":
            if x_len < 4:
                n = 4 - x_len
                zm = "0" * n + x_bin
                print(f"{zm}  ZM U1 U2")
                return zm
            elif x_len >= 4 and x_len < 8:
                n = 8 - x_len
                zm = "0" * n + x_bin
                print(f"{zm}  ZM U1 U2")
                return zm

        #U1 приклад на 55 в 2й це 110111 в число дадатнє доповнюєм 0 пусті місця 4чкратного бітами 00110111 -55 інвертуєм получене 11001000
        #-115 115 в 2й 1110011 в ю1 це 01110011 щоб отримати - інвертуємо 10001100
        try:
            u1_minus = zm_minus.replace("1", "-", 1)
            u1_minus = u1_minus.replace("0", "2")
            u1_minus = u1_minus.replace("1", "0")
            u1_minus = u1_minus.replace("2", "1")
            u1_minus = u1_minus.replace("-", "1", 1)
            print((f"{u1_minus}  U1"))
        except NameError:
            pass

        #U2 маємо код Ю1 допустимо 11111110 де 1 це - і саме число 1111110 додаємо 0000001 щоб отримати Ю2 1111111 і на початку 1 як - топто 1111111
        #щоб отримати в 10вій потрібно Ю2 код відняти 00000001 отримати Ю1 і інветрувати його щоб отримати в ЗМ топто в 2вому з приставкою 0 чи 1 його вже переводим у 10ву
        #додаткове число таке саме як в зм і ю1 топто бінарне з 0 на очатку в 8біт
        active = True
        # try:
        #     u1_indexn = str(u1_minus)
        #     u1_plus_1 = int(u1_minus) + 1
        #     u1_index = u1_indexn.index("0", 3)
        #     # if u1_index != 3:
        #         # u1_index2 = u1_indexn.index("0", 7)
        #     if u1_index == 3:# or u1_index2 == 7:
        #         active = False
        #         print(f"{int(u1_minus) + 1}  U2")
        # except NameError:
        #     pass

        try:
            u1_indexn = str(u1_minus)
            u1_plus_1 = int(u1_minus) + 1
            u1_index = u1_indexn.find("0", -1)
            # if u1_index != 3:
                # u1_index2 = u1_indexn.index("0", 7)
            if u1_index == 3 or u1_index == 7:
                active = False
                print(f"{int(u1_minus) + 1}  U2")
                return int(u1_minus) + 1
        except NameError:
            pass


        # active = True
        try:
            u1_plus_1 = int(u1_minus) + 1
            while active:
                u1_plus_1 = str(u1_plus_1)
                u1_minus = int(u1_plus_1)
                u2_reverse = myrevers(u1_minus)
                u2_reverse = str(u2_reverse)
                u2_reverse = u2_reverse.replace("3", "9", 1)
                u2_reverse = u2_reverse.replace("2", "3", 1)
                g = u2_reverse.index("1")
                if u2_reverse.find("3") != -1:
                    g1 = u2_reverse.index("3") + 1
                else:
                    g1 = u2_reverse.index("0")
                g2 = u2_reverse.index("0")
                if g == g1:
                    u2_reverse = u2_reverse.replace("1", "2", 1)
                    u2_reverse = int(u2_reverse)
                    u1_plus_1 = myrevers(u2_reverse)
                elif g2 == g1:
                    u2_reverse = u2_reverse.replace("0", "1", 1)
                    u2_reverse = int(u2_reverse)
                    u1_plus_1 = myrevers(u2_reverse)
                    u2_reverse = myrevers(u2_reverse)
                    u2_reverse = str(u2_reverse)
                    u2_reverse = u2_reverse.replace("3", "0")
                    u2_reverse = u2_reverse.replace("9", "0")
                    print((f"{u2_reverse}  U2"))
                    active = False
        except NameError or ValueError:
            pass

    #zmu1u2(-11)

    def zm_to_dec(num):

        def bin_dec(data):
            number = 0
            len_dat = len(data)
            for i in range(0, len_dat):
                number += int(data[i]) * (2 ** (len_dat - i - 1))

            return number

        x = num
        x = str(x)
        if len(x) == 4 or len(x) == 8:
            symbol_of_number = x.index("1")
            if symbol_of_number == 0:
                x = x.replace("1", "", 1)
                x = f"-{bin_dec(x)}"
                return x
            elif symbol_of_number >= 1:
                print(bin_dec(x))
                return bin_dec(x)

    # zm_to_dec("10101000")

    def u1_to_zm(num):
        try:
            u1_minus = num.replace("1", "-", 1)
            u1_minus = u1_minus.replace("0", "2")
            u1_minus = u1_minus.replace("1", "0")
            u1_minus = u1_minus.replace("2", "1")
            u1_minus = u1_minus.replace("-", "1", 1)
            return u1_minus
        except NameError:
            pass

    # zm_to_dec(u1_to_zm("11010111"))

    def u2_to_u1(num):
        x = num
        x = int(x)
        x = x - 1
        # print(x)
        x = str(x)
        x = x.replace("9", "1")
        # print(x)
        return x

    # u2_to_u1("1010")

    # zm_to_dec(u1_to_zm(u2_to_u1("11110001")))
    # zm_to_dec("01111111")
