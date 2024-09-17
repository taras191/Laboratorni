from number_to_words.converter import number_to_words

def greet_user():
    print("Welcome to Number to Words Converter!")
    while True:
        number = input("Enter a number (or 'q' to quit): ")
        if number == 'q':
            break
        try:
            number = int(number)
            words = number_to_words(number)
            print(f"Word representation: {words}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
