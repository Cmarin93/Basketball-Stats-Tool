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
        client = player
        height = client['height']
        guardians_slice_index = client['guardians'].find(' and ')

        # slices string of 'height' then converts to int.
        if type(height) != int:
            client['height'] = int(height[0:2])

        # converts each string of 'guardians' into a list of strings.
        if type(client['guardians']) == str:
            guardians = []
            if guardians_slice_index == -1:
                guardians.append(client['guardians'])
                client['guardians'] = guardians
            else:
                dog = client['guardians']
                guardians.append(dog[:guardians_slice_index])
                guardians.append(dog[guardians_slice_index + 5:])
                client['guardians'] = guardians
            # sorted players list based on experience.
            if client['experience'] == 'YES':
                client['experience'] = True
                experienced_players.append(client)
            else:
                client['experience'] = False
                inexperienced_players.append(client)
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
