import json
from typing import Optional, List

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Justin Curl <jcurl@princeton.edu>'

doc = """
use Convex Time Budget analysis to analyze 
"""


class Constants(BaseConstants):
    name_in_url = 'individual'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    political_affiliation = models.StringField()

