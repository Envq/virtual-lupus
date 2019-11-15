from django.core.management.base import BaseCommand
from app.models import Game
from app.constants.GameStates import APERTO


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'numPlayers',
            type=int,
            help="Number of players"
        )

    def handle(self, *args, **options):
        games = list(Game.objects.all())
        for game in games:
            game.delete()
        numPlayers = options['numPlayers']
        Game.objects.create(state=APERTO,
                            numPlayers=numPlayers)
