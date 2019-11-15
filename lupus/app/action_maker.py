from app.constants.Roles import *
from app.models import Player
from app.roles.contadino import Contadino
#...


class ActionMaker(object):

    @classmethod
    def doAction(id, paramsDict):
        clazz = retrieveClass(id)
        result = clazz.performAction(id, paramsDict)
        return result

    @classmethod
    def retrieveClass(id):
        role = Player.objects.filter(pk=id)[0].role
        if role == CONTADINO:
            return Contadino
        if role == LUPO:
            return #...
        #VEGGENTE
        #MAGO
        #GUARDIA
        #UNTORE
        #MASSONI
        #CRICETO
