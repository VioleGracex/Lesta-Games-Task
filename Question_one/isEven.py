def isEven_division_check(value: int) -> bool:
    return (value / 2) == (value // 2)

def main():
    while True:
        user_input = input("\nEnter a number: ").strip().lower()

        try:
            number = int(user_input)
            print(isEven_division_check(number))

        except ValueError:
            print(f"error")

if __name__ == "__main__":
    main()