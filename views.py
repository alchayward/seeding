from django.shortcuts import render, render_to_response
from seeding.models import Tournament, Team, Session, Game
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from itertools import chain

def tournament_list(request):
    tourn_list = Tournament.objects.all()
    return render_to_response('seeding/tournament_list.html',
    {'tournaments': tourn_list })

def tournament(request, tournament_id):
    tour = Tournament.objects.get(id__exact=tournament_id)
    sessions = Session.objects.filter(tournament=tournament_id)

    return render_to_response('seeding/tournament.html',
    {'tour':tour,'sessions':sessions})

def session(request, tournament_id, session_name):
    sess = Session.objects.get(tournament=tournament_id,
        slug=session_name)
    tour = Tournament.objects.get(id__exact=tournament_id)
   
    sess.teams = Team.objects.filter(session=sess.id)
    for team in sess.teams:
        games_1 = Game.objects.filter(session=sess.id,team_1=team.id)
        for game in games_1:
            game.opp_name = Team.objects.get(id=game.team_2.id).name
            if game.completed:
                result = "%s -- %s" % (game.score_1,game.score_2)
            else:
                result = "unplayed"
            game.result = result
        games_2 = Game.objects.filter(session=sess.id,team_2=team.id)
        for game in games_2:
            game.opp_name = Team.objects.get(id=game.team_1.id).name
            if game.completed:
                result = "%s -- %s" % (game.score_2,game.score_1)
            else:
                result = "unplayed"
            game.result = result
        team.games = list(chain(games_1,games_2))

    return render_to_response('seeding/session.html',
        {'tour': tour, 
        'sess': sess})

def run_session(request, tournament_id, session_name):
    context = RequestContext(request)
    
    #Check for permission

    #Check for which action is being preformed
        #no action
        #add games
        #change scores
        #stage next round (automatic?)
        #add a round
        

    if add_game:
        pass   
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        

        action = request.POST['action']
        password = request.POST['password']

        

#Not used yet
def game_list(request,session_id):
    return render_to_response('seeding/game_list.html',
    {'tournaments': Tournament.title.all()
    })

def team_list(request,tournament_name):
    return render_to_response('seeding/team_list.html',
    {'tournaments': Team.title.all()
    })

#Not used yet
def team_info(request, team_name):
    return render_to_response('seeding/team_info.html',
    {'team': Data.team_info(team_id) } )

#def tourn_admin(request, tour_id):
#    return render_to_response('seeding/run_tournament.html',
#        {'sessions': sessions, teams} )

##def tourn_admin(request, session_id):
#    return render_to_response('seeding/run_session.html',
#        {'session_id': session_id} )


#Generate Tournament object from database? Doesn't matter if ineffiecent. 
#Need an app for admin. Simple object editor.
#cookies? No point. This can be completely staeless at this point. 
#Though admin needs to log in. 

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/seeding/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('seeding/login.html', {}, context)

