"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
# Add your functions here.
def mc_trial(board,player):
    '''
    #monte carlo simulation 
    #for a particular board situation 
    #played a full game
    '''
    location = ()
    current_player = player
    while True:
        if board.check_win() != None:
            break
        else:
            location = board.get_empty_squares()
            pick_a_move = random.randint(0,len(location)-1)
            board.move(location[pick_a_move][0],location[pick_a_move][1],current_player)
            current_player = provided.switch_player(current_player)


def mc_update_scores(scores,board,player):
    '''
    #update the scores from the simulation function mc_trails
    #based on the moves
    #return the list/dictionary
    '''
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            if board.check_win()== player:
                if board.square(dummy_row,dummy_col) == board.check_win():
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                elif board.square(dummy_row,dummy_col) == 1:
                    scores[dummy_row][dummy_col] += 0
                else:
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
                    
            elif board.check_win()== provided.switch_player(player):
                if board.square(dummy_row,dummy_col) == board.check_win():
                    scores[dummy_row][dummy_col] += SCORE_OTHER
                elif board.square(dummy_row,dummy_col) == 1:
                    scores[dummy_row][dummy_col] += 0
                else:
                    
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
            else:
                scores[dummy_row][dummy_col] += 0

def get_best_move(board,scores):
    '''
    #based on the updated list from function
    #mc_update_scores
    #find the best move
    #return the next move
    '''
    find_max_score = []
    max_location = []
    location = board.get_empty_squares()
    if len(location) == 0:
        return (0,0)
    else:
        for square in location:
            find_max_score.append(scores[square[0]][square[1]])
        for square in location:
            if max(find_max_score) == scores[square[0]][square[1]]:
                max_location.append(square)     
        return max_location[random.randint(0,len(max_location)-1)]

def mc_move(board,player,trials):
    '''
    #get the move from function
    #mc_best_move
    #return the move to the board
    '''
    scores = [[] for dummy_x in range(board.get_dim())]
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            scores[dummy_row].append(0)
    for dummy_i in range(trials):
        boards = board.clone()
        mc_trial(boards,player)
        mc_update_scores(scores,boards,player) 
        
    return get_best_move(board,scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
