"""Implementation of the Game"""
import random


class Game:
    """The Lupus game"""

    def initGame(self, users, roles):
        self._winner = None
        self._roles = roles

        # Initialize players
        self._players = dict.fromkeys(users)
        for user in self._players:
            index = random.choice(range(len(roles)))
            self._players[user] = roles.pop(index)
    
    def getRole(self, user):
        return self._players[user]