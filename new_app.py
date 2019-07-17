import os
from constants import PLAYERS, TEAMS

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

teams = []
# Need to acess total of players on teams.

for player in PLAYERS: # selects every player.
    #player['height']  <== change to int
    if type(player['height']) != int:
        player['height'] = int(player['height'][0:2])

    if type(player['guardians']) == str:
        player['guardians'] # here is the power.

    print(player['guardians'])
        # select easch gaurdian and put them into own string.
        #1) we can look for 2nd space. if not present, put into list.\
        #    if present, remove " and " then place both ends into the list as seperate values.

# pairing teams w/ #'s.
for team_tuple in enumerate(TEAMS, 1): # each team is paired w/ a #
    team = {}
    team['name'] = team_tuple[1]
    team['number'] = team_tuple[0]
    teams.append(team)

experienced_players = []
inexperienced_players = []

#1st change all players height.

print(teams)
print(teams[0])



#I must replicate the PLAYERS (a list of dictionaries)
# I must access every PLAYERS['height'] & convert to int.
# I must access PLAYERS['experience'] & convert to bool.
# I must acess PLAYERS['gaurdians'] & convert to a list of strings (remove 'and')

# WORK TBD: {Players : [{Alex}, {Carlos}, {Dan}]}
#           Must clean Player Data.



    # teams = {{team_number : 1, Name : Panthers, Players : a list of handled players}}
