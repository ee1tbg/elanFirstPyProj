'''
Created on Jan 31, 2019

@author: Winterberger
'''
'''
Define list of playable letters and separate list of points. Realistically this would be defined as a dictionary but are defined separately to practice creating a dict by zipping 2 lists.
'''
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

'''
Create aforementioned dictionary mapping letters to points, add a special case where spaces are 0 points?
'''
letters_to_points = {letter:point for letter,point in zip(letters,points) }
letters_to_points.update({' ':0})
print(letters_to_points)

'''
Function that calculates the score for a passed-in word.
'''
def score_word(word):
    point_total = 0
    for lLetter in word:
        point_total += letters_to_points.get(lLetter.upper(),0)
    return point_total

# test on the word brownie with an invalid character
#print(score_word("brownie!"))

''' Determine who's playing
'''
players_list = []
num_players = int(input('How many players are participating?'))
for player in range(num_players):
    #print(player)
    players_list.append(input('Who is player #{}'.format(player+1)))

''' Initialize word dicts
'''
player_to_words = {player:[] for player in players_list}
#print(player_to_words)
'''
Function to accumulate the scores for each word for a given player
'''
def add_scores(player):
    player_point_total = 0
    for word in player_to_words.get(player,0):
        print(word)
        player_point_total += score_word(word)
        print(player_point_total)
    return player_point_total

'''
Create dict containing each player and their total score
'''
player_to_points={player:add_scores(player) for player in player_to_words}
print (player_to_points)

'''
Function that takes in a new word for a given player
'''
def play_word(player,word):
    players_words = player_to_words[player]
    #print(players_words)
    players_words.append(word)
    player_to_words.update({player: players_words})
    print(player, player_to_words[player])

'''
Function that plays a full round
'''
def play_rounds():
    rounds = int(input("How many rounds do you want to play?"))
    for current_round in range(rounds):
        for player in player_to_words:
            print(player)
            word = input('New word for %s: ' % player)
            play_word(player,word)
        player_to_points.update({player:add_scores(player) for player in player_to_words})
        print (player_to_points)

'''
Actually play
'''    
play_rounds()
 
 
'''
Determine Winner
'''
def determine_winners():
    points = [player_to_points[lplayer] for lplayer in player_to_points]
    #print(points)
    most_points = max(points)
    '''
    TODO determine index of most points
    '''
    most_points_index = points.find(most_points)
    print("Highest score is {} found at index {}".format(most_points,most_points_index))
    
    # Need to account for multiple winners
    winners = [lplayer for lplayer in player_to_points if player_to_points[lplayer] == most_points]
    print(winners)
    '''
    TODO Pretty print for no/multiple/single winners
    if len(winners) == 0 or len(winners) == len(players_list):
        print("Literally everyone lost.")
    elif len(winners) == 1:
        print("The winner is {}!!".format(players_list[]))
        print ("It's a {}-way tie!".format(len(winners)))
    '''
determine_winners()