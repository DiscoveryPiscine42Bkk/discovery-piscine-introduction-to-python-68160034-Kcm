def main():
    user_input = input("Give me a number: ").strip()
    try:
        num = float(user_input)
        # ตรวจสอบว่าเป็นจำนวนเต็มหรือทศนิยม
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("That's not a valid number.")

if __name__ == "__main__":
    main()