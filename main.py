import numberSystemDictionary
import numCalculation
import dss

active = True
while active:
    action_choice_dic = {
        'key1': "Перевести з однієї системи числення в іншу",
        'key2': "Додати",
        'key3': "Відняти"
    }

    print(f"Шо надо здєлац?")
    n = 0
    for values_in_dic in action_choice_dic.values():
        n += 1
        print(f"{n} {values_in_dic}")

    user_choice = 0
    while user_choice < 1 or user_choice > 3:
        try:
            user_choice = int(input('Введи число '))
            if user_choice < 1 or user_choice > 3:
                print("Введи число від 1 до 3 гусь")
        except ValueError:
            print("Введи число від 1 до 3 гусь")

    if user_choice == 1:
        print("В якій системі числення число?")
        n = 0
        for values_in_dic in numberSystemDictionary.numberSystemDictionary.numSysDic.values():
            n += 1
            print(f"{n} {values_in_dic}")
        num_system_choice = int(input('Вибери систему '))
        # (2)
        if num_system_choice == 1:
            x = input('Введи число ')
            x = numCalculation.numCalculation.bin_dec(x)
            print(f"{x} (10)")
            x = numCalculation.numCalculation.zmu1u2(x)
            print(x)
        # (3)
        elif num_system_choice == 2:
            x = input('Введи число ')
        # (8)
        elif num_system_choice == 3:
            x = input('Введи число ')
        # (16)
        elif num_system_choice == 4:
            x = input('Введи число ')
        # (10)
        elif num_system_choice == 5:
            x = input('Введи число ')
            x = numCalculation.numCalculation.zmu1u2(x)
            print(x)
        # (ZM)
        elif num_system_choice == 6:
            x = input('Введи число ')
            x = numCalculation.numCalculation.zm_to_dec(x)
            print(f"{x} (10)")
            x = numCalculation.numCalculation.zmu1u2(x)
        # (U1)
        elif num_system_choice == 7:
            x = input('Введи число ')
            x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(x))
            print(f"{x} (10)")
            x = numCalculation.numCalculation.zmu1u2(x)
        # (U2)
        elif num_system_choice == 8:
            x = input('Введи число ')
            x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
            print(f"{x} (10)")
            x = numCalculation.numCalculation.zmu1u2(x)
        # (BIAS=7)
        elif num_system_choice == 9:
            x = input('Введи число ')

    # Додавання
    elif user_choice == 2:
        print("В якій системі обчислення?")
        n = 0
        for values_in_dic in numberSystemDictionary.numberSystemDictionary.numForAdd.values():
            n += 1
            print(f"{n} {values_in_dic}")
        num_system_choice = int(input('Вибери систему '))
        # (2)
        if num_system_choice == 1:
            x = input('Введи перше число ')
        # ZM
        elif num_system_choice == 2:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.zm_add_zm(x, y)
            print(n)
        # U1
        elif num_system_choice == 3:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.u1_add_u1(x, y)
            print(n)
        # U2
        elif num_system_choice == 4:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.u2_add_u2(x, y)
            print(n)
        # BIAS = 7
        elif num_system_choice == 5:
            x = input('Введи перше число ')

    # Віднімання
    elif user_choice == 3:
        print("В якій системі обчислення?")
        n = 0
        for values_in_dic in numberSystemDictionary.numberSystemDictionary.numForAdd.values():
            n += 1
            print(f"{n} {values_in_dic}")
        num_system_choice = int(input('Вибери систему '))
        # (2)
        if num_system_choice == 1:
            x = input('Введи перше число ')
        # ZM
        elif num_system_choice == 2:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.zm_minus_zm(x, y)
            print(n)
        # U1
        elif num_system_choice == 3:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.u1_minus_u1(x, y)
            print(n)
        # U2
        elif num_system_choice == 4:
            x = input('Введи перше число ')
            y = input('Введи друге число ')
            n = dss.u2_minus_u2(x, y)
            print(n)
        # BIAS = 7
        elif num_system_choice == 5:
            x = input('Введи перше число ')


    user_choice = 0
    print("Ще є завдання?\n 1 - Так\n 2 - Ні")
    while user_choice == 0:
        try:
            user_choice = int(input('Введи число '))
            if user_choice == 1:
                continue
            elif user_choice == 2:
                active = False
            else:
                print("Введи число від 1 до 2 гусь")
                user_choice = 0
        except ValueError:
            print("Введи число від 1 до 2 гусь")


