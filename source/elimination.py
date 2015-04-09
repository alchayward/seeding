import tournament
import numpy as np

class Single_Elim(object):
    
    def __init__(self, teams):
        n_teams = length(teams)
        n_rounds = np.ceil(np.log2(teams,2))
        n_games = n_teams-1
        
           

        
    def current_games(self):
        return     
    
def games_tree(n_teams):
    class node(object):
        def __init__(self, val):
        self.l = None
        self.r = None
        self.v = None
    games  = range(n_teams//2).reverse()
    for g in games:
        
        
        

