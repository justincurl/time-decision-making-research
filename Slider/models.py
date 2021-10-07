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
from otree.models import player

author = "Justin Curl <jcurl@princeton.edu>"


class Constants(BaseConstants):
    name_in_url = "Slider"
    players_per_group = None
    num_rounds = 14

class Subsession(BaseSubsession):
    def creating_session(self):
        t_earliers = self.session.config['t_earliers'].split(', ')
        t_laters = self.session.config['t_laters'].split(', ')
        payment_earliers = self.session.config['payment_earliers'].split(', ')
        payment_laters = self.session.config['payment_laters'].split(', ')

        round_configs = []
        for i in range(self.session.config['num_sliders']):
            round_configs.append((t_earliers[i], t_laters[i], payment_earliers[i], payment_laters[i]))

        import itertools, random
        round_configs = itertools.cycle(round_configs)
        if self.round_number == 1:
            start_idx = random.randrange(self.session.config['num_sliders'])
        else:
            idx_candidate = self.get_players()[0].in_round(self.round_number - 1).condition_idx + 1
            if idx_candidate >= self.session.config['num_sliders']:
                start_idx = 1
            else:
                start_idx = idx_candidate
    
        iteration_start = itertools.islice(round_configs, start_idx, None)

        for p in self.get_players():
            player_config = next(iteration_start)
            p.condition_idx = start_idx
            p.earlier_time = player_config[0]  # example: today
            p.later_time = player_config[1]
            p.earlier_max = int(player_config[2])
            p.later_max = int(player_config[3])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    condition_idx = models.IntegerField()
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
