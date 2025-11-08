def main():
    print("Enter a number")
    try:
        n = int(input().strip())
    except ValueError:
        print("Invalid input")
        return

    for i in range(10):
        print(f"{i} x {n} = {i * n}")

if __name__ == "__main__":
    main()
