team_name = 'one of one' # the new team name is defined as a string
strategy_name = 'Judas' # the name of the strategy is defined as a string
strategy_description = 'If the opponent betrays in either the most recent or two most recent moves, the decision to betray is made. Otherwise, the function decides to collude.'

def move(my_history, their_history, my_score, their_score): 
    if their_history[-2:] == ['b', 'b']: #function checks to see if the most recent two responses of opponent are 'b'
        return 'b' #the move to betray is made
    else: 
        if their_history[-1:] == 'b': #function checks to see if the most recent response of opponent is 'b'
            return 'b' #the move to betray is made
        else:
            return 'c' #if none of these conditions are satisfied, then the move to collude 'c' is made
