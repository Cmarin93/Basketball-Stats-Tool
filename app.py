from constants import TEAMS as teams
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def invalid_option():
    clear()
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
                team_menu()
            elif option == 2:
                break
            else:
                invalid_option()
        except ValueError:
            invalid_option()

def team_menu():
    menu_looping = True
    while menu_looping:
        try:
            clear()
            print('\n')
            print('Teams')
            print('\n\n')
            # make teams list into dictionary with numbers stored.
            for team, num in zip(teams, '123'):
                print("%s) %s" % (num, team))
            print('\n')
            choice = int(input('>>> '))
            if choice == 1:
                input('showing team1 stats')
            elif choice == 2:
                input('showing team2 stats')
            elif choice == 3:
                input('showing team3 stats')
            else:
                invalid_option()
        except ValueError:
            invalid_option()

if __name__ == '__main__':
    print('running program...')
    menu()
