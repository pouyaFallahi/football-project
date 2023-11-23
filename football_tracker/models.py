from django.db import models



# Create your models here.
class PersonModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.FloatField()
    age = models.IntegerField()

    class Meta:
        abstract = True


class Player(PersonModel):
    position = models.CharField(max_length=100)
    player_id = models.IntegerField(primary_key=True, serialize=True)



class Coach(PersonModel):
    coach_id = models.IntegerField(primary_key=True, serialize=True)

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=100)
    shorthand = models.CharField(max_length=3)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='teams')
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, related_name='teams')
class LeaderBoard(models.Model):
    # leader_board_id = models.IntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    loses = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    standings = models.IntegerField()
    goals = models.IntegerField()
    goals_received = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')


class Match(models.Model):
    match_id = models.IntegerField(primary_key=True, serialize=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches')
    home_goals = models.CharField(max_length=100)
    away_goals = models.CharField(max_length=100)
