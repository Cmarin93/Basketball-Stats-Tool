import copy
import os
from constants import PLAYERS, TEAMS


experienced_players = []
inexperienced_players = []
teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)
team_list = []


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
                team_assign(player)
                #lopp thru teams, and if exp slot is open, insert
            else:
                player['experience'] = False 
                team_assign(player)
    # creation of team dictionaries
    for team_tuple in enumerate(teams, 1):  # each team is paired w/ a #
        team = {}
        team['team_name'] = team_tuple[1]
        team['team_number'] = team_tuple[0]
        team['team_total'] = int(len(players) / len(teams))
        #should this be derived from len(exp_players)?
        team['team_exp_total_limit'] = int(len(experienced_players) / len(teams))
        team['team_inexp_total_limit'] = int(len(inexperienced_players) / len(teams))
        team['exp_registar'] = []
        team['inexp_registar'] = []

        team_list.append(team)
    print(team_list[0])
    print(len(team['exp_registar']))
    print(experienced_players)

def team_assign(player):
    if player['experience'] == True:
        experienced_players.append(player)
        print('HOTDOGHOTDOG')
    else:
        inexperienced_players.append(player)
        print('WTF')
    #add player to a team with less then

    #team_list - everytime we loop thru a player.
            #team_name \/
            #team_number \/
            #team_total:\/
                #  total_players / #_of_teams = players_per_team
            #team_exp
                #  total_exp_players / #_of_teams = XP_players_per_group
            #team_inexp
                # total_exp_players / #_of_teams = XP_players_per_group
            #team_players
                # we must loop thru each team & assign them a xpPlayer until all xpPlayers are done?

        #BALANCE: same # of total players on each team.
        #BALANCE_XP: same # of experienced vs inexperienced_players



def clear():
    os.system('clear' if os.name == 'posix' else 'cls')


if __name__ == '__main__':
    start_program()
