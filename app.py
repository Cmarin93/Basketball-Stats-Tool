import os
from constants import PLAYERS
from constants import TEAMS


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def total_players():
    total_players = 0
    for player in PLAYERS:
        total_players += 1
    return total_players

def total_teams():
    total_teams = 0
    for team in TEAMS:
        total_teams += 1
    return total_teams
players_per_team = (total_players() / total_teams())
input(players_per_team)
# list of xp_player & in-xp_players
def seperation():
    experienced_players = []
    inexperienced_players = []
    for player in PLAYERS: #acessing each player dictionary
        if player['experience'] == 'YES':
            experienced_players.append(player)
        elif player['experience'] == 'NO':
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players

experienced_players, inexperienced_players = seperation()
input(len(experienced_players))
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
    menu_looping1 = True
    while menu_looping1:
        try:
            clear()
            print('\n')
            print('Teams')
            print('\n\n')
            # make teams dict. into a numbered list.
            # for num, team in teams:
            #     print("%s) %s" % (num, team))
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
    menu()
