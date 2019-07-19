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
    for team_tuple in enumerate(teams, 1):  # each team is paired w/ a #
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
                experienced_players.append(player)
            else:
                player['experience'] = False
                inexperienced_players.append(player)


# balances players based on experience
def team_assign():
    car = copy.copy(experienced_players)
    boat = copy.copy(inexperienced_players)

    for i in range(len(team_list)): #loops thru every team.
        while len(team_list[i]['exp_registar']) < 3:
            team_list[i]['exp_registar'].append(car[0])
            car.remove(car[0])

        while len(team_list[i]['inexp_registar']) < 3:
            team_list[i]['inexp_registar'].append(boat[0])
            boat.remove(boat[0])

def menu():
    pass

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    data_conversion()
    team_assign()
