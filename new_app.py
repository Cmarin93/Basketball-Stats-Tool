import copy
import os
from constants import PLAYERS, TEAMS


experienced_players = []
inexperienced_players = []
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
team_list = []


def data_conversion():
    # creation of team_list (a list of dictionaries))
    for team_tuple in enumerate(teams, 1):   # each team is paired w/ a #
        team = {}
        team['name'] = team_tuple[1]
        team['number'] = team_tuple[0]
        team['total'] = int(len(players) / len(teams))
        team['exp_registar'] = []
        team['inexp_registar'] = []
        team_list.append(team)

    # player data conversion + creation of sorted players list based on XP.
    for player in players:
        height = player['height']
        guardians_slice_index = player['guardians'].find(' and ')

        # slices string of 'height' then converts to int.
        if type(height) != int:
            player['height'] = int(height[0:2])

        # converts each string of 'guardians' into a list of strings.
        if type(player['guardians']) == str:
            guardians = []
            if guardians_slice_index == -1:   # if no ' and ' is found.
                guardians.append(player['guardians'])
                player['guardians'] = guardians
            else:
                guardian_string = player['guardians']
                guardians.append(guardian_string[:guardians_slice_index])
                guardians.append(guardian_string[guardians_slice_index + 5:])
                player['guardians'] = guardians
            # sorted players list based on experience.
            if player['experience'] == 'YES':
                player['experience'] = True
                experienced_players.append(player)
            else:
                player['experience'] = False
                inexperienced_players.append(player)


# balances players based on experience
def team_assign():
    car = copy.copy(experienced_players)
    boat = copy.copy(inexperienced_players)

    for i in range(len(team_list)):  # loops thru every team.
        while len(team_list[i]['exp_registar']) < 3:
            team_list[i]['exp_registar'].append(car[0])
            car.remove(car[0])

        while len(team_list[i]['inexp_registar']) < 3:
            team_list[i]['inexp_registar'].append(boat[0])
            boat.remove(boat[0])


def menu():
    while True:
        clear()
        print('---- MENU----'.center(50))
        print('Made By: Carlos A. Marin'.center(50))
        print('')
        print('Here are your choices:')
        print('  1) Display Team Stats')
        print('  2) Quit')
        print('')
        try:
            choice = int(input('Enter an option > '))
            if choice == 1:
                team_menu()
            elif choice == 2:
                print('quitting...')
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            invalid_option()
            continue


def team_menu():
    while True:
        clear()
        for team in team_list:
            print(str(team['number']) + ') ' + team['name'])
        print('4) Back to main menu')
        print('')
        try:
            choice = int(input('Enter an option: > '))
            if choice == 1:
                team_stats(1)
            elif choice == 2:
                team_stats(2)
            elif choice == 3:
                team_stats(3)
            elif choice == 4:
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            invalid_option()
            continue


def team_stats(team_number):
    team = team_list[team_number - 1]
    x = ', '


    clear()
    print('Team: ' + team['name'])
    print('-' * 50)
    print('Players on team:')
    pre_registar = team['exp_registar'] + team['inexp_registar']
    registar = []
    for i in pre_registar: # i is player (dict)
            registar.append(i['name'])
    print(x.join(registar))
    input('')



def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def invalid_option():
    print('Please enter a valid entry.\n')
    input('Press [Enter] to continue...')


if __name__ == '__main__':
    data_conversion()
    team_assign()
    menu()
