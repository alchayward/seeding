# Current problems/restrictions:
# Can't play the same team more than once.
import tournament 
from tournament import Session,Game
import networkx as nx
import numpy as np
import pymc
from scipy import cosh, rand, log
from scipy.special import gammaincc, gammaln
from numpy import dot,exp,array
#import matplotlib.pyplot as plt

def log_2_pois_like(d,a,s1,s2): #taken out the max_score  limit for now
    dp = np.sign(d)*np.power(np.abs(d),1.5)
    return ( log(a)*(s1+s2)+dp*(5+s2-s1) -2*a*cosh(dp) -
             gammaln(s1+1) - gammaln(s2+1) )

def log_diff_exp_likr(d,a,s1,s2):
    return exp( (-(d + (s1-s2))**2)/a )


def log_d_pois_like_trunc_5(d,s1,s2,a,p):
    """double poisson w max 5 goals"""
    #dp = np.sign(d)*np.power(np.abs(d),p)
    dp = 1.5*np.arctan(d)    #print(dp)
    return ( log(a)*(s1+s2)+dp*(s1-s2) - 2*a*cosh(dp)
         -gammaln(s1+1) - gammaln(s2+1) 
        -log(gammaincc(6,a*exp(-dp))*gammaincc(6,a*exp(dp)) ) ) 
    
class double_model():
    
    def plot_thetas(self,teams = None):
        if teams is None:
            teams = self.teams
        fig = plt.figure()
        ax = plt.subplot(111)
        plt.xlim(-5,5)
        for ii in range(len(teams)):
            ax.hist(self.mcmc.theta.trace.gettrace()[:,teams[ii].session_id],
            bins=50,histtype='step',normed=True, 
             label = '{}'.format(teams[ii].name))
        ax.legend(loc='upper center', bbox_to_anchor=(1.2, 0.9),
                  ncol=1, fancybox=True, shadow=True)
        plt.show()    
        return ax
    
    def get_data(self):
        n_games = len(self.games)
        data_games = []
        for g in self.games:
            if g.completed:
                data_games.append(g)

        team_idx = np.zeros([len(data_games),self.n_teams])
        scores = []
        for ind,game in enumerate(data_games):
            score = [game.score_1,game.score_2]
            scores.append(score)   
            team_idx[ind,game.s_team_1] = 1
            team_idx[ind,game.s_team_2] = -1
        
        return np.array(scores),np.array(team_idx)

    def make_model(self):
        
        scores,team_idx = self.get_data()

        n_teams = self.n_teams
        n_games = len(scores)
        prob_func = self.prob_func
        scale = self.scale
        #Just set as a constant now, too lazy
        scale = pymc.TruncatedNormal(
           'scale',mu = self.scale, tau = np.power(1/5.0,2),value=self.scale
                ,a = 0,b = 10)
        
        #expo = pymc.Uniform( 'expo',0.45,1,value=0.5)
        expo = 0.5

        #need to put in initial seeding stuff
        theta_i = pymc.Normal('theta_i',
            mu = 0, tau = np.power(1/3.0,2), value=self.inital_theta )

        @pymc.deterministic()
        def theta(beta=theta_i):
            return beta - sum(beta)/(1.0*n_teams)

        @pymc.stochastic(observed=True)
        def games_played(value=scores ,sp=scale,alpha = theta,pow=expo):
            return sum(prob_func(dot(team_idx, alpha),
                 value[:,0], value[:,1], sp, pow))
            
        @pymc.deterministic()
        def marginal_delta(beta = theta):
            return np.dot(self.marginal_mat,beta)
        
        return pymc.Model(locals())
    
    def fit_model(self):
        m = self.make_model()
        for key in m.__dict__.keys():
            if not isinstance(key, basestring):
                del m.__dict__[key]
        self.mcmc = pymc.MCMC(m)
        self.mcmc.use_step_method(pymc.AdaptiveMetropolis, self.mcmc.theta_i)
        print('running MCMC')
        self.mcmc.sample(self.mc_points,self.mc_burn ,self.mc_steps ,
             progress_bar=True)
        
        self.Update_After_Fit()

    def Update_After_Fit(self):
        self.update_count = self.update_count+1
        self.scale = self.mcmc.scale.stats()['mean']
        #self.update_KL_graph() # dont do this unless staging.

    def update_KL_graph(self):
        for edge in self.infoGraph.edges():
            self.infoGraph[edge[0]][edge[1]]['weight'].info

    def make_marginal_mat(self):
        mat = np.zeros([self.n_teams*(self.n_teams-1)/2,self.n_teams]) 
        self.marginal_ind = []
        count = 0
        for ii in range(self.n_teams):
            for jj in range(ii+1,self.n_teams):
                mat[count,ii] = 1.0
                mat[count,jj] = -1.0
                self.marginal_ind.append([ii,jj])
                count=count+1
        self.marginal_mat = mat

    def __init__(self):
        # Model Parameters
        #self.n_teams = n_teams
        n_teams = self.n_teams
        self.inital_theta = rand(self.n_teams)*0.0*3.0-1.5
        self.prob_func = log_d_pois_like_trunc_5
        self.max_score = 5
        self.scale = 2.5
        
        # MC parameters
        self.mc_points = 100000
        self.mc_burn = 10000
        self.mc_steps = 5
    
        # This counter changes after refitting, it is rembmered by entities
        # that need to update
        self.update_count = 0
        
        #KL Info init
        self.make_marginal_mat()   
        G = nx.Graph()
        G.add_nodes_from(range(self.n_teams))
        for ii in range(self.n_teams):
            
            for jj in range(ii+1,n_teams):
                v = KLvertex([ii,jj],self)
                G.add_edge(ii,jj,{'weight': v})
        if n_teams & 0x1: #Check if odd team numbers
            G.add_node(n_teams)
            for ii in range(n_teams):
                v = KLvertex([n_teams,ii],self)
                G.add_edge(n_teams,jj,{'value': v.info})

        self.infoGraph = G
    def delta_expect(self,ind,fn):
        # should check if traces exist
        tr = self.mcmc.marginal_delta.trace[:,ind]
        return np.sum(fn(tr))/len(tr)

    def KL_info_teams(self,ind):
        scores = range(self.max_score+1)
        f = self.prob_func
        a = self.scale
        expect = lambda x:self.delta_expect(ind,x)
        Epr = np.array([[expect( lambda x: exp(f(x,a,s1,s2)))
                 for s1 in scores] for s2 in scores])
        Elogpr = np.array([[expect( lambda x: f(x,a,s1,s2) )
                 for s1 in scores] for s2 in scores])
        Eprlogpr = np.array( [[expect(lambda x: exp(f(x,a,s1,s2))*f(x,a,s1,s2)) 
                 for s1 in scores ] for s2 in scores])
        
        return np.sum(Eprlogpr)-np.sum(Epr*Elogpr)
    
   # def graph_info(self,t_list):
   #     n_teams = self.n_teams
   #        #only do this for the teams we need to stage
   #     for ii in range(n_teams*(n_teams-1)/2):
   #        if all([s in t_list for s in self.marginal_ind[ii]]):
   #        self.km_info  info =  [kl_info(self.mcmc.marginal_delta.trace[:,ii])
        
    def get_info_weight(n1,n2):
        return self.infoGraph[n1][n2]['value']

    def stage_teams(self,edge_list):
        """Pass a list of team-team indices that need to be staged"""
        n_teams = self.n_teams
        F= nx.Graph()
        F.add_edges_from( [(e[0],e[1], 
            {'weight':self.infoGraph[e[0]][e[1]]['weight'].info}) 
            for e in edge_list])
        count = 0
        # when to put in instamix team?
        return nx.max_weight_matching(F)
class KLvertex():
    
    def __init__(self, teams, parent,insta=False):
        """pass a team in the tourament, needs to know the parent object """
        self.parent=parent
        self.teams = teams
        self.update_count = 0
        self._info = 0
        for ind,e in enumerate(parent.marginal_ind):
            if all([t in e for t in teams]): 
                self.mat_ind = ind
        self.is_instamix = insta
        if self.is_instamix:
            self.info = 0
            self._info = 0
            self.is_current = True
    @property 
    def info(self):
        if not self.is_current():
            self._info = self.parent.KL_info_teams(
                self.mat_ind)           
            self.update_count = self.parent.update_count
        
        return self._info
    def is_current(self):
        if self.update_count == self.parent.update_count:
            return True
        else:
            return False


class Seeding(Session,double_model):
    """Adaptive style seeding section"""

    def __init__(self,teams): 
        self.n_teams = len(teams)
        
        #super(self.__class__, self).__init__()
        double_model.__init__(self)
        Session.__init__(self,teams)
        #self.current_round = tournament.Round(1)

    def get_teams_to_seed(self,round):
        neg_list = []   
        for g in self.games:
            if g.round <= round:
                neg_list.append([t.session_id for t in g.teams])
        edge_list = []
        for ii in range(self.n_teams):
            for jj in range(ii+1,self.n_teams):
                if not  any([ [ii,jj] in neg_list, [jj,ii] in neg_list]):
                    edge_list.append([ii,jj])
        return edge_list

    def stage_round(self,round):
        e_list = self.get_teams_to_seed(round)
        stage = self.stage_teams(e_list)
        games = [ [k, stage[k] ] for k in stage.keys()]
        game_list = []
        gg_list = []
        for g in games:
            if not [g[1],g[0]] in gg_list:
                gg_list.append(g)
                game = tournament.Game(
                    teams = [self.teams[g[0]],self.teams[g[1]]])
                game.staged = True
                game.completed = False
                game.round = round
                game_list.append(game)
        return game_list

def update_session(games, teams):
    #Since the staging takes no time at all, and it can only be done after
    #updating, maybe it's better to suggest those games straight away in this
    #function.
    
    # create model instance
    S = Seeding(teams)
    S.games = games

        # pass games and team list.
        # team list is pretty irrelevant, just need a labeling

    # run model
    # validate 

    pass

def stage_first_round(teams):
    n_teams = length(teams)
    n_games = n_games//2
    new_games = []
    for ii in range(n_games):
        g=Game()
        g.round = 1
        g.id = 0
        g.teams = [ teams[ii],teams[ii+1] ]
        g.completed = False
        g.scores = [0,0]
        new_games.append(g)
    return new_games

def stage_second_round(games,teams):
    pass

def stage_round(round):
    if round == 1:
       stage_first_round(n_teams)
    pass


