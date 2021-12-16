from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Justin Curl'

doc = """
Initial consent app that can be prepended onto other apps
"""


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent_answer = models.StringField(initial="")
    is_mobile = models.BooleanField()
    is_mobile_original_method = models.StringField(initial="")
    device_type = models.IntegerField(
        choices=[
            [1, "Desktop Computer"],
            [2, "Laptop Computer"],
            [3, "Smartphone"],
            [4, "Tablet"],
            [5, "Something Else"],
        ],
        blank=True,
    )    
