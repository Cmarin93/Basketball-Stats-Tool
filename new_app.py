import constants

print(constants)
print(dir(constants))
print(constants.PLAYERS) # [{'name' : 'Carlos Marin', 'exp' : 'Yes', etc...}]
print(constants.TEAMS) # ['1', '2', '3']
print(type(constants.PLAYERS)) # a list w/ dictionaries
print(type(constants.TEAMS)) # a list.
print('')
print('x'*25)
print('')
print(constants.PLAYERS[0]) # dictionary of the 1st player.
print(type(constants.PLAYERS[0])) # dictionary.
print(dir(constants.PLAYERS[0]))
print('')
print(constants.PLAYERS[0].items())
print(constants.PLAYERS[0].values())
print(constants.PLAYERS[0].keys())
print(constants.PLAYERS[0]['name'])
print('')
