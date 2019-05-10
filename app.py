import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def invalid_option():
    print('Please enter a valid entery.\n')
    input('Press [Enter] to continue...')

def menu():
    menu_looping = True
    while menu_looping:
        try:
            clear()
            print('\n')
            print('Basketball Team Stats Tool')
            print('by Carlos A. Marin')
            print('\n\n')
            print('1) display team stats')
            print('2) quit')
            print('\n')
            option = int(input('>>> '))
            if option == 1:
                input('option 1 selected...')
                #show teamstuff
            elif option == 2:
                break
        except:
            input('please select a valid option.')


if __name__ == '__main__':
    print('running program...')
    menu()
