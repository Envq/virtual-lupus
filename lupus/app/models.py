from django.db import models

# Create your models here.
class Game(models.Model):

    state = models.IntegerField()
    numPlayers = models.IntegerField()


class Player(models.Model):

    name = models.CharField(max_lenght=32, unique=True)
    role = models.IntegerField()
    active = models.BooleanField()
    game = models.ForeignKey(Game,
                            on_delete=models.CASCADE,
                            related_name='players')
