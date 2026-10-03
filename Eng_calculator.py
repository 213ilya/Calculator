while True:
    print("Choose an option:")
    print("1 — Two numbers, one operation")
    print("2 — Three numbers, two operations")
    print("3 — Exit")
    option = input("Your choice: ").strip()

    if option == "1":
    
        while True:
        
            try:
                num1 = float(input("First number: ").strip())
            except ValueError:
                print("Enter a number!")
                continue
                
            op = input("Operation: ").strip()
            
            try:
                num2 = float(input("Second number: ").strip())
            except ValueError:
                print("Enter a number!")
                continue
            
            if op == "/" and num2 == 0:
                print("Error: division by zero!")
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
                print("Invalid operation. Use /, *, +, -.")
                continue
                
            print("Result:", result)
                
            if input("Continue? (yes/no): ").lower().strip() == "no":
                break

    elif option == "2":
    
        while True:
        
            try:
                num1 = float(input("First number: ").strip())
            except ValueError:
                print("Enter a number!")
                continue
                
            op1 = input("First operation: ").strip()
            
            try:
                num2 = float(input("Second number: ").strip())
            except ValueError:
                print("Enter a number!")
                continue
                
            op2 = input("Second operation: ").strip()
            
            try:
                num3 = float(input("Third number: ").strip())
            except ValueError:
                print("Enter a number!")
                continue
            
            if op1 == "/" and num2 == 0 or op2 == "/" and num3 == 0:
                print("Error: division by zero!")
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
                print("Invalid operation. Use /, *, +, -.")
                continue
                
            print("Result:", result)

            if input("Continue? (yes/no): ").lower().strip() == "no":
                break

    elif option == "3":
        break
    else:
        print("No, enter 1, 2 or 3.")
