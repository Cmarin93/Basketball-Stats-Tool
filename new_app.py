import copy
import os
from constants import PLAYERS, TEAMS


experienced_players = []
inexperienced_players = []
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
team_list = []
players_names_dict = {}

def start_program():

    # creation of team_list (a list of dictionaries))
    for team_tuple in enumerate(teams, 1):  # each team is paired w/ a #
        team = {}
        team['team_name'] = team_tuple[1]
        team['team_number'] = team_tuple[0]
        team['team_total'] = int(len(players) / len(teams))
        team['exp_registar'] = []
        team['inexp_registar'] = []
        team_list.append(team)

    # player data conversion
    for player in players:
        height = player['height']
        guardians_slice_index = player['guardians'].find(' and ')

        # slices string of 'height' then converts to int.
        if type(height) != int:
            player['height'] = int(height[0:2])

        # converts each string of 'guardians' into a list of strings.
        if type(player['guardians']) == str:
            guardians = []
            if guardians_slice_index == -1:  # if no ' and ' is found.
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
            else:
                player['experience'] = False


# balances players based on experience
def team_assign():
    for player_dict in players:
        print(player_dict)
        print(player_dict['name'])
        players_names_dict['%s'].format(player_dict['name']) = player_dict
        #pass
    for i in range((len(players))): # i accesses each player dictionary.
        dog = players[i]


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    start_program()
    team_assign()
    players_names_dict()

    # for team_property in team_list:
    #     print(team_property)
        # team_property
