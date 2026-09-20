while True:
    print("Выбери опцию:")
    print("1 — Два числа, одна операция")
    print("2 — Три числа, две операции")
    print("3 — Выход из программы")
    option = input("Твой выбор: ").strip()

    if option == "1":
    
        while True:
            try:
                num1 = float(input("1-ое число: ").strip())
            except ValueError:
                print("Введите число!")
                continue
            op = input("Операция: ").strip()
            try:
                num2 = float(input("2-ое число: ").strip())
            except ValueError:
                print("Введите число!")
                continue
            
            if op == "/" and num2 == 0:
                print("Ошибка: деление на ноль!")
                continue

            if op == "/":
                result = num1 / num2
            elif op == "*":
                result = num1 * num2
            elif op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            else:
                print("Неправильно, допустимые операции: /, *, +, -. Попробуй снова.")
                continue
                
            print("Результат:", result)
                
            if input("Продолжить? (да/нет): ").lower().strip() == "нет":
                break

    elif option == "2":
    
        while True:
            try:
                num1 = float(input("1-ое число: ").strip())
            except ValueError:
                print("Введите число!")
                continue
            op1 = input("1-ая операция: ").strip()
            try:
                num2 = float(input("2-ое число: ").strip())
            except ValueError:
                print("Введите число!")
                continue
            op2 = input("2-ая операция: ").strip()
            try:
                num3 = float(input("3-е число: ").strip())
            except ValueError:
                print("Введите число!")
                continue
            
            if op1 == "/" and num2 == 0 or op2 == "/" and num3 == 0:
                print("Ошибка: деление на ноль!")
                continue

            if op1 == "/" and op2 == "/":
                result = num1 / num2 / num3
            elif op1 == "/" and op2 == "*":
                result = num1 / num2 * num3
            elif op1 == "/" and op2 == "+":
                result = num1 / num2 + num3
            elif op1 == "/" and op2 == "-":
                result = num1 / num2 - num3
            elif op1 == "*" and op2 == "/":
                result = num1 * num2 / num3
            elif op1 == "*" and op2 == "*":
                result = num1 * num2 * num3
            elif op1 == "*" and op2 == "+":
                result = num1 * num2 + num3
            elif op1 == "*" and op2 == "-":
                result = num1 * num2 - num3
            elif op1 == "+" and op2 == "/":
                result = num1 + num2 / num3
            elif op1 == "+" and op2 == "*":
                result = num1 + num2 * num3
            elif op1 == "+" and op2 == "+":
                result = num1 + num2 + num3
            elif op1 == "+" and op2 == "-":
                result = num1 + num2 - num3
            elif op1 == "-" and op2 == "/":
                result = num1 - num2 / num3
            elif op1 == "-" and op2 == "*":
                result = num1 - num2 * num3
            elif op1 == "-" and op2 == "+":
                result = num1 - num2 + num3
            elif op1 == "-" and op2 == "-":
                result = num1 - num2 - num3
            else:
                print("Неправильно, допустимые операции: /, *, +, -. Попробуй снова.")
                continue
                
            print("Результат:", result)

            if input("Продолжить? (да/нет): ").lower().strip() == "нет":
                break

    elif option == "3":
        print("Выход из программы.")
        break
    else:
        print("Неправильный выбор, попробуй снова.")