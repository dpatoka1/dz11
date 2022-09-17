def fib(n):
    a, b = 0, 1
    for __ in range(n):
        a, b = b, a + b
        if n == b:
          return 'Является числом последовательности фибоначчи'
    return 'Не является числом последовательности фибоначчи'
x=int(input("Введите число "))
print(fib(x))
