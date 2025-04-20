operation = input("Введите операцию (+,-,*,/): ")
if operation != "+,-,*,/":
        print("Я не знаю такой операции")
        exit()
cifr1 = float(input("Введите первое число: "))
cifr2 = float(input("Введите второе число: "))

if operation == "+":
    result = cifr1 + cifr2
    print(f"Результат сложения: {result}")
elif operation == "-":
    result = cifr1 - cifr2
    print(f"Результат вычитания: {result}")
elif operation == "*":
    result = cifr1 * cifr2
    print(f"Результат умножения: {result}")
elif operation == "/":
    if cifr2 != 0:
        result = cifr1 / cifr2
        print(f"Результат деления: {result}")
    else:
        print("Делить на 0 нельзя!")