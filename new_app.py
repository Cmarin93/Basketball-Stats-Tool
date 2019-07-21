import copy
import os
from constants import PLAYERS, TEAMS

border = ('☰' * 35)
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
team_list = []
experienced_players = []
inexperienced_players = []


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
            if guardians_slice_index == -1:   # if ' and ' is not found.
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
    xp_list = copy.copy(experienced_players)
    inxp_list = copy.copy(inexperienced_players)

    for i in range(len(team_list)):  # loops thru every team.
        teams_exprienced_players = team_list[i]['exp_registar']
        teams_inexperienced_players = team_list[i]['inexp_registar']
        while len(teams_exprienced_players) < 3:
            teams_exprienced_players.append(xp_list[0])
            xp_list.remove(xp_list[0])

        while len(teams_inexperienced_players) < 3:
            teams_inexperienced_players.append(inxp_list[0])
            inxp_list.remove(inxp_list[0])


def menu():
    while True:
        clear()
        print('--⭐-- Basketball Stats Tool --⭐--'.center(50))
        print('Made By: Carlos A. Marin ☕'.center(50) )
        print(border)
        print('')
        print('Here are your choices:')
        print('  1) Display Team Stats')
        print('  2) Quit')
        print('')
        try:
            choice = int(input('Enter an option ⭢ '))
            if choice == 1:
                team_menu()
            elif choice == 2:
                print('ending program...')
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
        print('⚡ TEAMS ⚡'.center(50))
        print(border)
        print('')
        # list of teams assigned to their team number.
        for team in team_list:
            print(str(team['number']) + ') ' + team['name'])
        print('4) Back to main menu')
        print('')
        try:
            choice = int(input('Enter an option: ⭢ '))
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


def team_stats(choice):
    team = team_list[choice - 1]
    pre_registar = team['exp_registar'] + team['inexp_registar']
    pre_height = 0
    registar = []
    team_guardians = []
    x = ', '
    for player in pre_registar:  # i is player (dict)
            registar.append(player['name'])
            pre_height += player['height']
            for guardian in player['guardians']:
                team_guardians.append(guardian)
    avg_height = (pre_height / team['total'])
    clear()
    print('⚞' + team['name'] + '⚟' + 'Page(1/2)'.center(70))
    print(border)
    print('Players on team:')
    print(x.join(registar))
    print('')
    print('Teams average height: ' + str(avg_height) + '"')
    print('')
    input('Press [Enter] to continue...')
    clear()
    print('⚞' + team['name'] + '⚟' + 'Page(2/2)'.center(70))
    print(border)
    print('Experienced players: ' + str(len(team['exp_registar'])))
    print('Inexperienced players: ' + str(len(team['inexp_registar'])))
    print('')
    print('Guardians of players on team: ')
    print(x.join(team_guardians))
    print('')
    input('Press [Enter] to continue...')


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def invalid_option():
    print('Please enter a valid entry.\n')
    input('Press [Enter] to continue...')


if __name__ == '__main__':
    data_conversion()
    team_assign()
    menu()
