import copy
import os
from constants import PLAYERS, TEAMS


BUTTONS = ['❶', '❷', '❸']
press_enter = "\nPress [Enter] to continue..."
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
team_list = []
experienced_players = []
inexperienced_players = []

def BORDER(string):
    print("\n  ╔" + ((len(string)+2) * "═") + "╗")
    print("  ║ " + string + " ║")
    print("  ╚" + ((len(string)+2) * "═") + "╝")
    	
def data_conversion():
    for team_tuple in enumerate(teams, 1): # loop thru teams
        team = {}
        team['number'] = team_tuple[0]
        team['number_icon'] = BUTTONS[team['number'] - 1]
        team['name'] = team_tuple[1]
        team['total'] = int(len(players) / len(teams))
        team['exp_registar'] = []
        team['inexp_registar'] = []
        team_list.append(team)

    for player in players:
        height = player['height']
        guardians_slice_index = player['guardians'].find(' and ')   # The starting index of " and "

        if type(height) != int:
            player['height'] = int(height[0:2])

        # guardian data conversion + xp list creation
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
            # xp list sorting.
            if player['experience'] == 'YES':
                player['experience'] = True
                experienced_players.append(player)
            else:
                player['experience'] = False
                inexperienced_players.append(player)

def team_assignments():
    xp_list = copy.copy(experienced_players)
    inxp_list = copy.copy(inexperienced_players)

    for i in range(len(team_list)):  # loops thru every team.
        teams_exprienced_players = team_list[i]['exp_registar']
        teams_inexperienced_players = team_list[i]['inexp_registar']
        while len(teams_exprienced_players) < 3:
            teams_exprienced_players.append(xp_list[0]) # adds to register
            xp_list.remove(xp_list[0])  # removes from pool
        while len(teams_inexperienced_players) < 3:
            teams_inexperienced_players.append(inxp_list[0])
            inxp_list.remove(inxp_list[0])

def menu():
    while True:
        menu_text()
        try:
            choice = int(input(' Enter an option: '))
            if choice == 1:
                team_menu()
            elif choice == 2:
                BORDER('Program Terminated')
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            invalid_option()
            continue

def menu_text():
    clear()
    BORDER('Basketball Stats Tool')
    print('   coded by: Carlos A. Marin\n\n Here are your choices:')
    print('  ❶ Display Team Stats')
    print('  ❷ Quit\n')


def team_menu():
    while True:
        team_text()
        try:
            choice = int(input(' Enter an option: '))
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


def team_text():
    clear()
    BORDER('TEAMS')
    for team in team_list:
        print('\n ' + str(team['number_icon']) + ' ' + team['name'] + '\n ❹ Back to main menu\n')
    #print('\n ❹ Back to main menu\n')


def team_stats(choice):
    team = team_list[choice - 1]
    pre_registar = team['exp_registar'] + team['inexp_registar']
    pre_height = 0
    registar = []
    team_guardians = []
    # sum of player heights, guardians + players list.
    for player in pre_registar:
            registar.append(player['name'])
            pre_height += player['height']
            for guardian in player['guardians']:
                team_guardians.append(guardian)
    avg_height = (pre_height / team['total'])
    team_stats_text(team, registar, avg_height, team_guardians)


def team_stats_text(team, registar, avg_height, team_guardians):
    team_title = '■  ' + team['name'] + '  ■'
    seperator = ', '
    clear()
    # Page 1
    BORDER(team_title)
    print('\nPlayers on team:')
    print(seperator.join(registar))
    print('\nTeams average height: ' + str(avg_height) + '"')
    print('\nPage(1/2)')
    input(press_enter)
    clear()
    # Page 2
    BORDER(team_title)
    print('\nExperienced players: ' + str(len(team['exp_registar'])))
    print('Inexperienced players: ' + str(len(team['inexp_registar'])))
    print('\nGuardians of players on team: ')
    breakpoint()
    print(seperator.join(team_guardians))
    print('\nPage(2/2)')
    input(press_enter)


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


def invalid_option():
    BORDER('Please enter a valid entry.')
    input(press_enter)


if __name__ == '__main__':
    data_conversion()
    team_assignments()
    menu()
