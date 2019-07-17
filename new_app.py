import copy
import os
from constants import PLAYERS, TEAMS


experienced_players = []
inexperienced_players = []
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
teams_list = []


def start_program():
    # Data restructuring
    for player in players:
        height = player['height']
        guardians_slice_index = player['guardians'].find(' and ')

        # slices string of 'height' then converts to int.
        if type(height) != int:
            player['height'] = int(height[0:2])

        # converts each string of 'guardians' into a list of strings.
        if type(player['guardians']) == str:
            guardians = []
            if guardians_slice_index == -1:
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
    # creation of team dictionaries
    for team_tuple in enumerate(teams, 1):  # each team is paired w/ a #
        team = {}
        team['name'] = team_tuple[1]
        team['number'] = team_tuple[0]
        teams_list.append(team)


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    start_program()
