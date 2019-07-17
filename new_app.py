import os
from constants import PLAYERS, TEAMS

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

teams = []

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
            pass
            dog = player['guardians']
            guard.append(dog[:player['guardians'].find(' and ')])
            guard.append(dog[player['guardians'].find(' and ') + 5:])


    #print(player['guardians'])
    #print(gaurd)
    # print(type(player['guardians']))
    #slice eeach character, if character is ' and ', provide action.

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
