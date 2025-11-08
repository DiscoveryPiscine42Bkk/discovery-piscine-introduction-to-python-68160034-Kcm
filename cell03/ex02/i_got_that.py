def main():
    while True:
        user_input = input("What you gotta say? : " if 'msg' not in locals() else "I got that! Anything else? : ")
        if user_input == "STOP":
            break

if __name__ == "__main__":
    main()