import json
from typing import Optional, List


from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    widgets,
)

author = "Justin Curl <jcurl@princeton.edu>"


class Constants(BaseConstants):
    name_in_url = "Slider"
    players_per_group = None
    num_rounds = 12
    

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.earlier_time = p.session.config['earlier_time']  # example: today
            p.later_time = p.session.config['later_time']
            p.earlier_max = p.session.config['earlier_payment'] 
            p.later_max = p.session.config['later_payment']

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    consent_answer = models.StringField(initial="")

    earlier_max = models.IntegerField()
    later_max = models.IntegerField()
    earlier_time = models.StringField()
    later_time = models.StringField()

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

    race = models.StringField()

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

    attention_check = models.StringField(initial="")

    slider_value = models.IntegerField()
    slider_one = models.IntegerField()
    check_slider_one = models.IntegerField(blank=True)
    slider_two = models.IntegerField()
    check_slider_two = models.IntegerField(blank=True)
