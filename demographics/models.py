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
import random


author = 'Justin Curl'

doc = """
short demographics questionnaire that can be appended to end of other apps
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        for player in self.get_players():
            player.code = str(random.randrange(10 ** 11, 10 ** 12))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    race = models.StringField()

    code = models.StringField()

    education = models.IntegerField(
        choices=[
            [1, "I do not have a high school degree or GED "],
            [2, "Regular high school degree "],
            [3, "GED or alternative credential "],
            [4, "Some college credit, no degree"],
            [5, "Associate’s degree (for example: AA, AS) "],
            [6, "Bachelor’s degree (for example: BA, BS) "],
            [7, "Graduate or professional degree "],
        ],
        blank=True,
        widget=widgets.RadioSelect,
    )

    gender = models.IntegerField(
        blank=True,
        choices=[
            [1, "Male"],
            [2, "Female"],
        ],
        widget=widgets.RadioSelect,
    )

    ethnicity = models.BooleanField(
        blank=True, choices=[[True, "Yes"], [False, "No"]], widget=widgets.RadioSelect
    )

    age = models.IntegerField(blank=True, min=18, max=110)

    feedback = models.LongStringField(blank=True)


    zipcode = models.IntegerField(blank=True, min=0, max=99999)
