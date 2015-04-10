from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField('date')
    public_view = models.BooleanField(default = 'True')
    slug = models.SlugField(max_length=160,blank=True,editable=False)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return "/seeding/tournaments/%s/%s/" % (self.id, self.slug)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
            super(Tournament,self).save()

class Session(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField('date')
    tournament = models.ForeignKey(Tournament)
    number_of_rounds = models.IntegerField()
    slug = models.SlugField(max_length=160,blank=True,editable=False)
    
    UPDATING = 'UP'
    READY = 'RD'
    status_choices = (
        (UPDATING, 'Updating'),
        (READY, 'Ready'),
    )

    status= models.CharField(max_length=2,
            choices=status_choices,
            default=READY)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return "%s%s" % (self.tournament.get_absolute_url(), self.slug)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
            super(Session,self).save()


class Round(models.Model):
    models.ForeignKey(Session)
    models.IntegerField(default=0)
    COMPLETED = 'CP'
    IN_PROGRESS = 'IP'
    FUTURE = 'FU'
    status_choices = (
        (COMPLETED, 'Completed'),
        (IN_PROGRESS, 'In Progress'),
        (FUTURE, 'To Be Played'),
    )

    status= models.CharField(max_length=2,
            choices=status_choices,
            default=FUTURE)

class Team(models.Model):
    session = models.ForeignKey('Session',null=True)
    name = models.CharField(max_length=250)
    member1 = models.CharField(max_length=250,default = "member 1")
    member2 = models.CharField(max_length=250,default = "member 2")
    member3 = models.CharField(max_length=250,default = "member 3")
    score = models.FloatField(default = 0.0)
    rank= models.IntegerField(default = 0)

    def __unicode__(self):
        return '%s' % self.name

class Game(models.Model):
	
    team_1 = models.ForeignKey(Team, related_name = 'game_team1')
    team_2 = models.ForeignKey(Team, related_name = 'game_team2')
    completed = models.BooleanField(default = 'FALSE') 
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    session = models.ForeignKey(Session, default = None)
    round = models.IntegerField(default = 0)
    staged = models.BooleanField(default = 'FALSE') 
    #duration = models.TimeField(default = ) 
    #ref = models.ForeignKey(Player, related_name='game_ref')
    #ass_ref = models.ForeignKey(Player, related_name = 'game_ass_ref')

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    tournmaments =  models.ManyToManyField('Tournament')

    def __unicode__(self):
        return self.user.username

