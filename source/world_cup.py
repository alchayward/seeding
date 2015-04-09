import tournament

class WorldCup(object):
    
    def __init__(self):
        pass    
    
    

def sort_groups(num_groups, num_teams, teams = []):
    """
    Sorts out the teams in terms of rankings.
    teams is a list of teams in order of ranking, with highest ranked in first
    position.
    """

    #check for valid numbers of teams/groups 


    if teams == []:
        teams = [str(num) for num in range(1, 1+num_teams)]
 
    #min number of teams per group
    ( min_teams, extra_teams ) = divmod(num_teams, num_groups)

    groups = [[] for ii in range(num_groups) ]

    gi = 0
    dir = 1
    for ii in range(num_teams):
        groups[gi].append(teams.pop(0))
        print gi
        gi = gi + dir
        if gi >= num_groups or gi < 0:  
            dir = dir*-1
            gi = gi+dir
        
    return groups
   
