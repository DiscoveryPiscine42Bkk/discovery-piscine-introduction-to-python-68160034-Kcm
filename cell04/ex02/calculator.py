def main():
    try:
        a = float(input("Give me the first number: "))
        b = float(input("Give me the second number: "))
        print("Thank you!")
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print(f"{a} / {b} = Cannot divide by zero")
        print(f"{a} * {b} = {a * b}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
    