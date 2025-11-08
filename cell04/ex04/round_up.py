import math

def main():
    try:
        num = float(input("Give me a number: "))
        print(math.ceil(num))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()