import sys
import passgen


def main():
    try:
        password_style = ''
        while password_style != '1' and password_style != '2' and password_style != 'n':
            password_style = input('1. Dl4_053_U719\n2. TEVA8-tocmoyen5-HASPMU6\nWhich password style would you like'
                                   'to generate?\n-> ')

        if password_style == '1':
            password_length = 0
            while True:
                try:
                    password_length = int(input('What should be the length of the password? (0 for random)\n-> '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    break

            password_parts = 0
            while True:
                try:
                    password_parts = int(input('Into how many parts should the password be split?\n-> '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    break

            password_separators = input('Would you like to use custom separators? (enter separators or \'n\' '
                                        'to choose default or \'enter\' use none)\n-> ')
            if password_separators == 'n':
                password_separators = None

            password_symbols = input('Would you like to use custom symbols? (enter symbols or \'n\' to '
                                     'choose default or \'enter\' to use none)\n-> ')
            if password_symbols == 'n':
                password_symbols = None

            password_should_uppercase = ''
            while password_should_uppercase != 'y' and password_should_uppercase != 'n':
                password_should_uppercase = input('Would you like to use uppercase letters?\n-> ')
            if password_should_uppercase == 'y':
                password_should_uppercase = True
            else:
                password_should_uppercase = False

            password_should_numbers = ''
            while password_should_numbers != 'y' and password_should_numbers != 'n':
                password_should_numbers = input('Would you like to use numbers?\n-> ')
            if password_should_numbers == 'y':
                password_should_numbers = True
            else:
                password_should_numbers = False

            print(passgen.generate_password(password_length, password_parts, password_separators, password_symbols,
                                            password_should_uppercase, password_should_numbers))

        if password_style == '2':
            password_parts = 0
            while password_parts <= 0:
                try:
                    password_parts = int(input('How many words should the password have? (0 for random)\n-> '))
                except ValueError:
                    print('Please enter a number.')
                else:
                    break

            password_separators = input('Would you like to use custom separators? (enter separators or \'n\' '
                                        'to choose default or \'enter\' use none)\n-> ')
            if password_separators == 'n':
                password_separators = None

            password_should_uppercase = ''
            while password_should_uppercase != 'y' and password_should_uppercase != 'n':
                password_should_uppercase = input('Would you like to use uppercase letters?\n-> ')
            if password_should_uppercase == 'y':
                password_should_uppercase = True
            else:
                password_should_uppercase = False

            password_should_numbers = ''
            while password_should_numbers != 'y' and password_should_numbers != 'n':
                password_should_numbers = input('Would you like to use numbers?\n-> ')
            if password_should_numbers == 'y':
                password_should_numbers = True
            else:
                password_should_numbers = False

            print(passgen.generate_word_password(password_parts, password_separators,
                                                 password_should_uppercase, password_should_numbers))
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
