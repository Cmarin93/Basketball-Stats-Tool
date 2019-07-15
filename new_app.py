import os
from constants import PLAYERS, TEAMS

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

teams = []
for team_tuple in enumerate(TEAMS, 1): # each team is paired w/ a #
    team = {}
    team["team{0}".format(team_tuple[0])] = team_tuple[1]
    teams.append(team)

print(teams)
# WORK TBD: Each team is it's own dictionary.



    # TEAMS = {{team_number : 1, Name : Panthers, Players : a list of handled players}}


# print(PLAYERS) # [{'name' : 'Carlos Marin', 'exp' : 'Yes', etc...}]
# print(TEAMS) # ['1', '2', '3']
# print(type(PLAYERS)) # a list w/ dictionaries
# print(type(TEAMS)) # a list.
# print('')
# print('x'*25)
# print('')
# print(PLAYERS[0]) # dictionary of the 1st player.
# print(type(PLAYERS[0])) # dictionary.
# print(dir(PLAYERS[0]))
# print('')
# player1 = PLAYERS[0].items()
# print(player1)
# print(PLAYERS[0].values())
# print(PLAYERS[0].keys())
# print(PLAYERS[0]['name'])
# print('')
