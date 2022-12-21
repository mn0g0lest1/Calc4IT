import numCalculation


def u2_add_u2(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index !=0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)

    return n

def u2_minus_u2(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    return n

def u2_mnoshenya_u2(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x * y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(x)))
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x * y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x * y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index !=0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(numCalculation.numCalculation.u2_to_u1(y)))
        x = int(x)
        y = int(y)
        n = x * y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)

    return n

def u1_add_u1(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(x))
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(y))
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(x))
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index !=0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(y))
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)

    return n

def u1_minus_u1(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(x))
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(y))
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(x))
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(numCalculation.numCalculation.u1_to_zm(y))
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    return n

def zm_add_zm(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index !=0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x + y
        print(f"{n} результат додавання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)

    return n

def zm_minus_zm(num1, num2):
    x = str(num1)
    y = str(num2)
    x_index = x.index("1")
    y_index = y.index("1")
    if x_index == 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index == 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index != 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    elif x_index != 0 and y_index == 0:
        x = numCalculation.numCalculation.zm_to_dec(x)
        y = numCalculation.numCalculation.zm_to_dec(y)
        x = int(x)
        y = int(y)
        n = x - y
        print(f"{n} результат віднімання в (10)")
        n = numCalculation.numCalculation.zmu1u2(n)
    return n

