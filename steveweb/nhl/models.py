from django.db import models

NHL_TEAMS = (('ANA', 'AnaheimDucks'), ('ARI', 'ArizonaCoyotes'),
        ('BOS', 'BostonBruins'), ('BUF', 'BuffaloSabres'),
        ('CAR', 'CarolinaHurricanes'), ('CBJ', 'ColumbusBlueJackets'),
        ('CGY', 'CalgaryFlames'), ('CHI', 'ChicagoBlackhawks'),
        ('COL', 'ColoradoAvalanche'), ('DAL', 'DallasStars'),
        ('DET', 'DetroitRedWings'), ('EDM', 'EdmontonOilers'),
        ('FLA', 'FloridaPanthers'), ('LAK', 'LosAngelesKings'),
        ('MIN', 'MinnesotaWild'), ('MTL', 'MontréalCanadiens'),
        ('NJD', 'NewJerseyDevils'), ('NSH', 'NashvillePredators'),
        ('NYI', 'NewYorkIslanders'), ('NYR', 'NewYorkRangers'),
        ('OTT', 'OttawaSenators'), ('PHI', 'PhiladelphiaFlyers'),
        ('PIT', 'PittsburghPenguins'), ('SJS', 'SanJoseSharks'),
        ('STL', 'St.LouisBlues'), ('TBL', 'TampaBayLightning'),
        ('TOR', 'TorontoMapleLeafs'), ('VAN', 'VancouverCanucks'),
        ('WPG', 'WashingtonCapitals'), ('WSH', 'WinnipegJets'))

# Create your models here.
class NHLGame(models.Model):
    game_date = models.DateField()
    home_team = models.CharField( max_length=3,
                                  choices = NHL_TEAMS )
    away_team = models.CharField( max_length=3,
                                  choices = NHL_TEAMS )
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    game_id = models.CharField( max_length=20 )

