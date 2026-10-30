
# Day 3: Menu-Driven Number Analyzer
# Class 11 Computer Science

while True:

    print("\n===== NUMBER ANALYZER =====")
    print("1. Check Even or Odd")
    print("2. Find Factorial")
    print("3. Check Prime Number")
    print("4. Display Multiplication Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program ended.")
        break

    elif choice == 1:
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")

    elif choice == 2:
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            fact = 1

            for i in range(1, num + 1):
                fact = fact * i

            print("Factorial =", fact)

    elif choice == 3:
        num = int(input("Enter a number: "))

        if num < 2:
            print(num, "is not a Prime Number")
        else:
            prime = True

            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                print(num, "is a Prime Number")
            else:
                print(num, "is not a Prime Number")

    elif choice == 4:
        num = int(input("Enter a number: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    else:
        print("Invalid choice! Please try again.")
