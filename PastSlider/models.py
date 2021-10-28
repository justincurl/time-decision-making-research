import json
import random


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
    name_in_url = "PastSlider"
    players_per_group = None
    num_rounds = 21

class Subsession(BaseSubsession):
    def creating_session(self):
        t_options = self.session.config['past_t_options'].split(', ')
        t_earliers = self.session.config['past_t_earliers'].split(', ')
        t_laters = self.session.config['past_t_laters'].split(', ')
        payment_earliers = self.session.config['past_payment_earliers'].split(', ')
        payment_laters = self.session.config['past_payment_laters'].split(', ')

        round_configs = []
        for i in range(self.session.config['past_num_sliders']):
            round_configs.append((t_earliers[i], t_laters[i], payment_earliers[i], payment_laters[i]))

        for i, p in enumerate(self.get_players()):
            p.t_earliest = t_options[0]
            p.t_middle = t_options[1]
            p.t_latest = t_options[2]
            if self.session.config["past_randomize_sliders"]:
                if self.round_number == 1:
                    # randomize slider order for each player
                    slider_order = [j for j in range(self.session.config['past_num_sliders'])]
                    random.shuffle(slider_order)
                    p.slider_order = json.dumps(slider_order)
                else:
                    p.slider_order = p.in_round(self.round_number - 1).slider_order
                if self.round_number <= self.session.config['past_num_sliders']:
                    # only go for the configurable number of sliders
                    player_config = round_configs[json.loads(p.slider_order)[self.round_number - 1]]
                    p.earlier_time = player_config[0]  # example: today
                    p.later_time = player_config[1]
                    p.earlier_max = int(player_config[2])
                    p.later_max = int(player_config[3])
            else:
                if self.round_number <= self.session.config['past_num_sliders']:
                    player_config = round_configs[self.round_number - 1]
                    p.earlier_time = player_config[0]  # example: today
                    p.later_time = player_config[1]
                    p.earlier_max = int(player_config[2])
                    p.later_max = int(player_config[3])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    t_earliest = models.StringField()
    t_middle = models.StringField()
    t_latest = models.StringField()
    slider_order = models.StringField()
    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    earlier_max = models.IntegerField()
    later_max = models.IntegerField()
    earlier_time = models.StringField()
    later_time = models.StringField()

    slider_value = models.IntegerField()
    slider_one = models.IntegerField()
    check_slider_one = models.IntegerField(blank=True)
    slider_two = models.IntegerField()
    check_slider_two = models.IntegerField(blank=True)