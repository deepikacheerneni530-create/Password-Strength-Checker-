from password_checker import check_password


def main():

    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    while True:

        password = input(
            "\nEnter a test password (or type exit): "
        )

        if password.lower() == "exit":
            print("Thank you for using Password Checker!")
            break

        if not password:
            print("Password cannot be empty.")
            continue

        result = check_password(password)

        print("\n--------- PASSWORD REPORT ---------")

        print("Password Strength:",
              result["strength"])

        print("Security Score:",
              str(result["score"]) + "/6")

        print("Estimated Entropy:",
              str(result["entropy"]) + " bits")

        print("\nSuggestions:")

        if result["feedback"]:
            for suggestion in result["feedback"]:
                print("-", suggestion)
        else:
            print("Good! No basic policy improvements needed.")

        print("-----------------------------------")


if __name__ == "__main__":
    main()