from app.models import *
from app.action_maker import ActionMaker


class GameEngine(object):

    @classmethod
    def addPlayer(name):
        game = Game.objects.all()[0]
        try:
            player = Player.objects.create(name=name,
                                           role=-1,
                                           active=True,
                                           game=game)
            return player.pk
        except Exception:
            return -1

    @classmethod
    def checkAllPlayers():
        players = Player.objects.all()
        game = Game.objects.all()[0]
        if len(players) == game.numPlayers:
            return True
        return False

    @classmethod
    def changeGameState(state):
        game = Game.objects.all()
        game.state=state
        game.save()
