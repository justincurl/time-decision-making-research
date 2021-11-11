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
    name_in_url = "FutureSlider"
    players_per_group = None
    num_rounds = 21
    sliders_per_section = 6

class Subsession(BaseSubsession):
    def creating_session(self):
        t_options = self.session.config['future_t_options'].split(', ')
        
        t_earliers = self.session.config['future_t_earliers'].split(' | ')
        for i in range(len(t_earliers)):
            t_earliers[i] = t_earliers[i].split(", ")
        
        t_laters = self.session.config['future_t_laters'].split(' | ')
        for i in range(len(t_laters)):
            t_laters[i] = t_laters[i].split(", ")

        payment_earliers = self.session.config['future_payment_earliers'].split(' | ')
        for i in range(len(payment_earliers)):
            payment_earliers[i] = payment_earliers[i].split(", ")

        payment_laters = self.session.config['future_payment_laters'].split(' | ')
        for i in range(len(payment_laters)):
            payment_laters[i] = payment_laters[i].split(", ")
        
        round_configs = []
        round_section = []
        for i in range(len(t_earliers)):
            for j in range(Constants.sliders_per_section):
                round_section.append((t_earliers[i][j], payment_earliers[i][j], t_laters[i][j], payment_laters[i][j]))
            round_configs.append(round_section)
            round_section = []

        for i, p in enumerate(self.get_players()):
            p.t_earliest = t_options[0]
            p.t_middle = t_options[1]
            p.t_latest = t_options[2]
            if self.round_number == 1:
                if self.session.config["future_randomize_sliders"]:
                    random.shuffle(round_configs)
                p.round_configs = json.dumps(round_configs)
            else:
                p.round_configs = p.in_round(self.round_number - 1).round_configs
                
            if self.round_number <= self.session.config['future_num_sliders']:
                # only go for the configurable number of sliders
                player_config = json.loads(p.round_configs)[(self.round_number - 1)//6][(self.round_number - 1) % 6]
                p.earlier_time = player_config[0]  # example: today
                p.earlier_max = int(player_config[1])
                p.later_time = player_config[2]
                p.later_max = int(player_config[3])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_configs = models.StringField()
    t_earliest = models.StringField()
    t_middle = models.StringField()
    t_latest = models.StringField()
    
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