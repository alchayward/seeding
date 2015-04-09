from django.contrib import admin
from seeding.models import Tournament, Session, Team, Game
from seeding.models import UserProfile
from seeding.source.staging import update_session

#from seeding import views

# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'tournament')
    exclude = ('slug',)


    def update_session_score(modeladmin, request, queryset):
        session = queryset.values('id')
        games = Game.objects.filter(session = session)
        teams = TournamentTeam.objects.filter(session = session)
        #This should update the Kl info about the session too.
        #Should I write to the database from the source files?
        update_session(games,teams)
    update_session_score.short_description = "update scores"

    def stage_round(modeladmin, request, queryset):
        pass
    update_session_score.short_description = "stage round"

    actions = [update_session_score, stage_round]
    filter = ['tournament']
admin.site.register(Session, SessionAdmin)

class TeamInline(admin.StackedInline):
    model = Team
    extra = 1

class SessionInline(admin.StackedInline):
    model = Session
    extra = 0

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'public_view')
    exclude = ('slug',)
   
    def run_tournament(modeladmin,request,queryset):
        qv = queryset.values('id')
        if len(queryset) != 1:
           self.message_user(request,
             "only 1 tournament please")
           return request
        else:
           # response = views.tourn_admin(qv)
            return response

    actions = [run_tournament]
    #inlines = [TeamInline,SessionInline]
    inlines = [SessionInline]

admin.site.register(Tournament, TournamentAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'member1', 'member2', 'member3' )
    list_filter = ['tournament','session']
admin.site.register(Team,TeamAdmin)

admin.site.register(UserProfile)

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','team_1', 'team_2', 'completed' )
    list_filter = ['tournament','session']
admin.site.register(Game,GameAdmin)
