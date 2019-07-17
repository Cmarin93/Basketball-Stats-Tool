import os
from constants import PLAYERS, TEAMS

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

teams = []
experienced_players = []
inexperienced_players = []

#for loop to create filtered data.
for player in PLAYERS:

    #converts each string of 'height' into an integer.
    if type(player['height']) != int:
        player['height'] = int(player['height'][0:2])

    #converts each string of 'guardians' into a list of strings.
    if type(player['guardians']) == str:
        guard = []
        name = ''
        if player['guardians'].find(' and ') == -1:
            guard.append(player['guardians'])
        else:
            dog = player['guardians']
            guard.append(dog[:player['guardians'].find(' and ')])
            guard.append(dog[player['guardians'].find(' and ') + 5:])
            player['guardians'] = guard

        if player['experience'] == 'YES':
            player['experience'] = True
            experienced_players.append(player)
        else:
            player['experience'] = False
            inexperienced_players.append(player)

# creation of team dictionaries
for team_tuple in enumerate(TEAMS, 1): # each team is paired w/ a #
    team = {}
    team['name'] = team_tuple[1]
    team['number'] = team_tuple[0]
    teams.append(team)

print(experienced_players)
print(inexperienced_players)



    # teams = {{team_number : 1, Name : Panthers, Players : a list of handled players}}
