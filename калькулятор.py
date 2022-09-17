while True:
    s = input("Действие ")
    if s in ('+', '-', '*', '/','**'):
        a = float(input("Введите первый элемент "))
        b = float(input("Введите второй элемент "))
         
        if s == '+':
            print(a+b)
        elif s == '-':
            print(a-b)
        elif s == '*':
            print(a*b)
        elif s == '/':
            if b != 0:
                print(a/
                      b)
            else:
                print("Деление на ноль!")
        elif s=='**':
            print(a**b)
    elif s=='log':
        z=float(input("Введите число " ))
        x=float(input("Введите основание логарифма " ))
        import math
        print(math.log(z,x))
    else:
        print("Неверное действие")
        

