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
    name_in_url = 'Module2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent_answer = models.StringField(initial="")
    check_slider_one_year = models.IntegerField()
    slider_one_year = models.StringField()
    check_slider_direct_growth = models.IntegerField()
    slider_direct_growth = models.StringField()
    check_slider_five_year = models.IntegerField()
    slider_five_year = models.StringField()
    direct_growth = models.IntegerField(choices=[[1, "4% this year and no growth next year"], [2, "4% next year and no growth this year"]], widget=widgets.RadioSelect,)
