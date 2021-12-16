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
    name_in_url = "FutureGrid"
    players_per_group = None
    num_rounds = 21
    grids_per_section = 5

class Subsession(BaseSubsession):
    def creating_session(self):
        future_grid_right_values = self.session.config["future_grid_right_values"].split(", ")
        future_grid_right_values = [float(i) for i in future_grid_right_values]
        future_grid_left_values = self.session.config["future_grid_left_values"].split(", ")
        future_grid_left_values = [float(i) for i in future_grid_left_values]
        future_grid_t_earliers = self.session.config['future_grid_t_earliers'].split(', ')
        future_grid_t_laters = self.session.config['future_grid_t_laters'].split(', ')
        
        future_round_configs = []
        future_round_section = []
        for i in range(len(future_grid_left_values)//Constants.grids_per_section):
            for j in range(Constants.grids_per_section):
                future_round_section.append((future_grid_t_earliers[i*Constants.grids_per_section + j], future_grid_left_values[i*Constants.grids_per_section + j], future_grid_t_laters[i*Constants.grids_per_section + j], future_grid_right_values[i*Constants.grids_per_section + j]))
            future_round_configs.append(future_round_section)
            future_round_section = []

        for i, p in enumerate(self.get_players()):
            if self.round_number == 1:
                if self.session.config["future_randomize_blocks"]:
                    for i in range(len(future_round_configs)):
                        random.shuffle(future_round_configs[i])
                    random.shuffle(future_round_configs)
                p.future_round_configs = json.dumps(future_round_configs)
            else:
                p.future_round_configs = p.in_round(self.round_number - 1).future_round_configs
                
            if self.round_number <= self.session.config['future_num_blocks']:
                # only go for the configurable number of sliders
                player_config = json.loads(p.future_round_configs)[(self.round_number - 1)//Constants.grids_per_section][(self.round_number - 1) % Constants.grids_per_section]
                p.earlier_time = player_config[0]  # example: today
                p.earlier_max = int(player_config[1])
                p.later_time = player_config[2]
                p.later_max = int(player_config[3])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    future_round_configs = models.StringField()
    
    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    earlier_max = models.IntegerField()
    later_max = models.IntegerField()
    earlier_time = models.StringField()
    later_time = models.StringField()

    future_grid_answer = models.StringField()