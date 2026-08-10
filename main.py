from ai_engine import improve_headline, improve_about

while True:

    print("\n==============================")
    print(" LinkedIn AI Assistant ")
    print("==============================")

    print("1. Improve Headline")
    print("2. Improve About")
    print("3. Exit")

    choice = input("\nChoose: ")

    if choice == "1":

        headline = input("\nEnter Current Headline:\n")

        print("\nGenerating...\n")

        print(improve_headline(headline))

    elif choice == "2":

        about = input("\nPaste About Section:\n")

        print("\nGenerating...\n")

        print(improve_about(about))

    elif choice == "3":

        break

    else:

        print("Invalid Choice")