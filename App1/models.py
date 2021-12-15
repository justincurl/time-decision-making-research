import random, json, itertools
from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

author = "Justin Curl <jcurl@princeton.edu>"

class Constants(BaseConstants):
    name_in_url = "App1"
    players_per_group = None
    num_rounds = 30
    num_per_section = 5
    num_sliders = 15
    num_grids = 15


class Subsession(BaseSubsession):
    def creating_session(self) -> None:

        listOfOptions = [
            (1, "PV", "FV"),
            (2, "PV", "PG"),
            (3, "FV", "PV"),
            (4, "FV", "FG"),
            (5, "PG", "FG"),
            (6, "PG", "PV"),
            (7, "FG", "PG"),
            (8, "FG", "FV"),
        ]

        rand_choice = random.choice(listOfOptions)
        ordering = itertools.cycle(listOfOptions)
        start_at_random = itertools.islice(ordering, rand_choice[0], None)

    ###################################################################################################### FUTURE GRID SET UP ######################################################################################################
        future_t_options = self.session.config['future_t_options'].split(', ')

        future_grid_laters = self.session.config["future_grid_laters"].split(", ")
        future_grid_laters = [float(i) for i in future_grid_laters]
        future_grid_earliers = self.session.config["future_grid_earliers"].split(", ")
        future_grid_earliers = [float(i) for i in future_grid_earliers]
        future_grid_t_earliers = self.session.config['future_grid_t_earliers'].split(', ')
        future_grid_t_laters = self.session.config['future_grid_t_laters'].split(', ')
        
        future_grid_round_configs = []
        future_round_section = []
        for i in range(len(future_grid_earliers)//Constants.num_per_section):
            for j in range(Constants.num_per_section):
                future_round_section.append((future_grid_t_earliers[i*Constants.num_per_section + j], future_grid_earliers[i*Constants.num_per_section + j], future_grid_t_laters[i*Constants.num_per_section + j], future_grid_laters[i*Constants.num_per_section + j]))
            future_grid_round_configs.append(future_round_section)
            future_round_section = []

    ###################################################################################################### PAST GRID SET UP ######################################################################################################
        past_t_options = self.session.config['past_t_options'].split(', ')
        
        past_grid_laters = self.session.config["past_grid_laters"].split(", ")
        past_grid_laters = [float(i) for i in past_grid_laters]
        past_grid_earliers = self.session.config["past_grid_earliers"].split(", ")
        past_grid_earliers = [float(i) for i in past_grid_earliers]
        past_grid_t_earliers = self.session.config['past_grid_t_earliers'].split(', ')
        past_grid_t_laters = self.session.config['past_grid_t_laters'].split(', ')
        
        past_grid_round_configs = []
        past_round_section = []
        for i in range(len(past_grid_earliers)//Constants.num_per_section):
            for j in range(Constants.num_per_section):
                past_round_section.append((past_grid_t_earliers[i*Constants.num_per_section + j], past_grid_earliers[i*Constants.num_per_section + j], past_grid_t_laters[i*Constants.num_per_section + j], past_grid_laters[i*Constants.num_per_section + j]))
            past_grid_round_configs.append(past_round_section)
            past_round_section = []
    
    ###################################################################################################### FUTURE VISUAL SET UP ###################################################################################################### 
        future_t_options = self.session.config['future_t_options'].split(', ')
        
        future_t_earliers = self.session.config['future_t_earliers'].split(' | ')
        for i in range(len(future_t_earliers)):
            future_t_earliers[i] = future_t_earliers[i].split(", ")
        
        future_t_laters = self.session.config['future_t_laters'].split(' | ')
        for i in range(len(future_t_laters)):
            future_t_laters[i] = future_t_laters[i].split(", ")

        future_payment_earliers = self.session.config['future_payment_earliers'].split(' | ')
        for i in range(len(future_payment_earliers)):
            future_payment_earliers[i] = future_payment_earliers[i].split(", ")

        future_payment_laters = self.session.config['future_payment_laters'].split(' | ')
        for i in range(len(future_payment_laters)):
            future_payment_laters[i] = future_payment_laters[i].split(", ")
        
        future_visual_round_configs = []
        future_round_section = []
        for i in range(len(future_t_earliers)):
            for j in range(Constants.num_per_section):
                future_round_section.append((future_t_earliers[i][j], future_payment_earliers[i][j], future_t_laters[i][j], future_payment_laters[i][j]))
            future_visual_round_configs.append(future_round_section)
            future_round_section = []

    ###################################################################################################### PAST VISUAL SET UP ###################################################################################################### 
        past_t_options = self.session.config['past_t_options'].split(', ')
        
        past_t_earliers = self.session.config['past_t_earliers'].split(' | ')
        for i in range(len(past_t_earliers)):
            past_t_earliers[i] = past_t_earliers[i].split(", ")
        
        past_t_laters = self.session.config['past_t_laters'].split(' | ')
        for i in range(len(past_t_laters)):
            past_t_laters[i] = past_t_laters[i].split(", ")

        past_payment_earliers = self.session.config['past_payment_earliers'].split(' | ')
        for i in range(len(past_payment_earliers)):
            past_payment_earliers[i] = past_payment_earliers[i].split(", ")

        past_payment_laters = self.session.config['past_payment_laters'].split(' | ')
        for i in range(len(past_payment_laters)):
            past_payment_laters[i] = past_payment_laters[i].split(", ")
        
        past_visual_round_configs = []
        past_round_section = []
        for i in range(len(past_t_earliers)):
            for j in range(Constants.num_per_section):
                past_round_section.append((past_t_earliers[i][j], past_payment_earliers[i][j], past_t_laters[i][j], past_payment_laters[i][j]))
            past_visual_round_configs.append(past_round_section)
            past_round_section = []
        

    ###################################################################################################### PLAYERS SET UP ###################################################################################################### 
        for player in self.get_players():
            if self.round_number == 1:
                player_order = next(start_at_random)
                player.condition = player_order[0]
                player.first = player_order[1]
                player.second = player_order[2]
                player.participant.vars["condition"] = player.condition
            else:
                player.condition = player.in_round(self.round_number - 1).condition
                player.first = player.in_round(self.round_number - 1).first
                player.second = player.in_round(self.round_number - 1).second
            
        
        ################################################################################################### IF CONDITION 1 or 2 ###################################################################################################
            if player.first == "PV":
                    ################################################################################################### PAST VISUAL WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_sliders:
                    player.t_earliest = past_t_options[0]
                    player.t_middle = past_t_options[1]
                    player.t_latest = past_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["past_randomize_sliders"]:
                            for i in range(len(past_visual_round_configs)):
                                random.shuffle(past_visual_round_configs[i])
                            random.shuffle(past_visual_round_configs)
                        player.past_visual_round_configs = json.dumps(past_visual_round_configs)
                    else:
                        player.past_visual_round_configs = player.in_round(self.round_number - 1).past_visual_round_configs
                    if self.round_number <= Constants.num_sliders:    
                        past_player_config = json.loads(player.past_visual_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                        player.earlier_time = past_player_config[0]  # example: today
                        player.earlier_max = int(past_player_config[1])
                        player.later_time = past_player_config[2]
                        player.later_max = int(past_player_config[3])

                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if player.second == "FV":
                        player.t_earliest = future_t_options[0]
                        player.t_middle = future_t_options[1]
                        player.t_latest = future_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["future_randomize_sliders"]:
                                for i in range(len(future_visual_round_configs)):
                                    random.shuffle(future_visual_round_configs[i]) 
                                random.shuffle(future_visual_round_configs)
                            player.future_visual_round_configs = json.dumps(future_visual_round_configs)
                        else:
                            player.future_visual_round_configs = player.in_round(self.round_number - 1).future_visual_round_configs
                            
                        # only go for the configurable number of sliders
                        future_player_config = json.loads(player.future_visual_round_configs)[(self.round_number - Constants.num_grids - 1)//Constants.num_per_section][(self.round_number - Constants.num_grids - 1) % Constants.num_per_section]
                        player.earlier_time = future_player_config[0]  # example: today
                        player.earlier_max = int(future_player_config[1])
                        player.later_time = future_player_config[2]
                        player.later_max = int(future_player_config[3])

                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_sliders + Constants.num_grids + 1:    
                    if player.second == "PG":
                        player.t_earliest = past_t_options[0]
                        player.t_middle = past_t_options[1]
                        player.t_latest = past_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["past_randomize_blocks"]:
                                for i in range(len(past_grid_round_configs)):
                                    random.shuffle(past_grid_round_configs[i])
                                random.shuffle(past_grid_round_configs)
                            player.past_grid_round_configs = json.dumps(past_grid_round_configs)
                        else:
                            player.past_grid_round_configs = player.in_round(self.round_number - 1).past_grid_round_configs

                        player_config = json.loads(player.past_grid_round_configs)[(self.round_number - Constants.num_sliders - 1)//Constants.num_per_section][(self.round_number - Constants.num_sliders - 1) % Constants.num_per_section]
                        player.earlier_time = player_config[0]  # example: today
                        player.earlier_max = int(player_config[1])
                        player.later_time = player_config[2]
                        player.later_max = int(player_config[3])

        ################################################################################################### IF CONDITION 3 or 4 ###################################################################################################
            elif player.first == "FV":
                ################################################################################################### FUTURE VISUAL WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_sliders:
                    player.t_earliest = future_t_options[0]
                    player.t_middle = future_t_options[1]
                    player.t_latest = future_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["future_randomize_sliders"]:
                            for i in range(len(future_visual_round_configs)):
                                random.shuffle(future_visual_round_configs[i]) 
                            random.shuffle(future_visual_round_configs)
                        player.future_visual_round_configs = json.dumps(future_visual_round_configs)
                    else:
                        player.future_visual_round_configs = player.in_round(self.round_number - 1).future_visual_round_configs
                        
                    future_player_config = json.loads(player.future_visual_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                    player.earlier_time = future_player_config[0]  # example: today
                    player.earlier_max = int(future_player_config[1])
                    player.later_time = future_player_config[2]
                    player.later_max = int(future_player_config[3])
                
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if player.second == "PV":
                        player.t_earliest = past_t_options[0]
                        player.t_middle = past_t_options[1]
                        player.t_latest = past_t_options[2]
                        if self.round_number - Constants.num_sliders == 1:
                            if self.session.config["past_randomize_sliders"]:
                                for i in range(len(past_visual_round_configs)):
                                    random.shuffle(past_visual_round_configs[i]) 
                                random.shuffle(past_visual_round_configs)
                            player.past_visual_round_configs = json.dumps(past_visual_round_configs)
                        else:
                            player.past_visual_round_configs = player.in_round(self.round_number - 1).past_visual_round_configs
                            
                        past_player_config = json.loads(player.past_visual_round_configs)[(self.round_number - Constants.num_sliders - 1)//Constants.num_per_section][(self.round_number - Constants.num_sliders - 1) % Constants.num_per_section]
                        player.earlier_time = past_player_config[0]  # example: today
                        player.earlier_max = int(past_player_config[1])
                        player.later_time = past_player_config[2]
                        player.later_max = int(past_player_config[3])
                
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_sliders + Constants.num_grids + 1: 
                    if player.second == "FG":
                        player.t_earliest = future_t_options[0]
                        player.t_middle = future_t_options[1]
                        player.t_latest = future_t_options[2]
                        if self.round_number - Constants.num_sliders == 1:
                            if self.session.config["future_randomize_blocks"]:
                                for i in range(len(future_grid_round_configs)):
                                    random.shuffle(future_grid_round_configs[i])
                                random.shuffle(future_grid_round_configs)
                            player.future_grid_round_configs = json.dumps(future_grid_round_configs)
                        else:
                            player.future_grid_round_configs = player.in_round(self.round_number - 1).future_grid_round_configs
            
                        player_config = json.loads(player.future_grid_round_configs)[(self.round_number - Constants.num_sliders - 1)//Constants.num_per_section][(self.round_number - Constants.num_sliders - 1) % Constants.num_per_section]
                        player.earlier_time = player_config[0]  # example: today
                        player.earlier_max = int(player_config[1])
                        player.later_time = player_config[2]
                        player.later_max = int(player_config[3])

        ################################################################################################### IF CONDITION 5 or 6 ###################################################################################################
            elif player.first == "PG":
                ################################################################################################### PAST GRID WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_grids:
                    player.t_earliest = past_t_options[0]
                    player.t_middle = past_t_options[1]
                    player.t_latest = past_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["past_randomize_blocks"]:
                            for i in range(len(past_grid_round_configs)):
                                random.shuffle(past_grid_round_configs[i])
                            random.shuffle(past_grid_round_configs)
                        player.past_grid_round_configs = json.dumps(past_grid_round_configs)
                    else:
                        player.past_grid_round_configs = player.in_round(self.round_number - 1).past_grid_round_configs

                    player_config = json.loads(player.past_grid_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                    player.earlier_time = player_config[0]  # example: today
                    player.earlier_max = int(player_config[1])
                    player.later_time = player_config[2]
                    player.later_max = int(player_config[3])

                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    if player.second == "FG":
                        player.t_earliest = future_t_options[0]
                        player.t_middle = future_t_options[1]
                        player.t_latest = future_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["future_randomize_blocks"]:
                                for i in range(len(future_grid_round_configs)):
                                    random.shuffle(future_grid_round_configs[i])
                                random.shuffle(future_grid_round_configs)
                            player.future_grid_round_configs = json.dumps(future_grid_round_configs)
                        else:
                            player.future_grid_round_configs = player.in_round(self.round_number - 1).future_grid_round_configs
            
                        player_config = json.loads(player.future_grid_round_configs)[(self.round_number - Constants.num_grids - 1)//Constants.num_per_section][(self.round_number - Constants.num_grids - 1) % Constants.num_per_section]
                        player.earlier_time = player_config[0]  # example: today
                        player.earlier_max = int(player_config[1])
                        player.later_time = player_config[2]
                        player.later_max = int(player_config[3])
                
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    if player.second == "PV":
                        player.t_earliest = past_t_options[0]
                        player.t_middle = past_t_options[1]
                        player.t_latest = past_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["past_randomize_sliders"]:
                                for i in range(len(past_visual_round_configs)):
                                    random.shuffle(past_visual_round_configs[i])
                                random.shuffle(past_visual_round_configs)
                            player.past_visual_round_configs = json.dumps(past_visual_round_configs)
                        else:
                            player.past_visual_round_configs = player.in_round(self.round_number - 1).past_visual_round_configs
                        
                        past_player_config = json.loads(player.past_visual_round_configs)[(self.round_number - Constants.num_grids - 1)//Constants.num_per_section][(self.round_number - Constants.num_grids - 1) % Constants.num_per_section]
                        player.earlier_time = past_player_config[0]  # example: today
                        player.earlier_max = int(past_player_config[1])
                        player.later_time = past_player_config[2]
                        player.later_max = int(past_player_config[3])

        ################################################################################################### IF CONDITION 7 or 8 ###################################################################################################
            elif player.first == "FG":
                ################################################################################################### FUTURE GRID WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_grids:
                    player.t_earliest = future_t_options[0]
                    player.t_middle = future_t_options[1]
                    player.t_latest = future_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["future_randomize_blocks"]:
                            for i in range(len(future_grid_round_configs)):
                                random.shuffle(future_grid_round_configs[i])
                            random.shuffle(future_grid_round_configs)
                        player.future_grid_round_configs = json.dumps(future_grid_round_configs)
                    else:
                        player.future_grid_round_configs = player.in_round(self.round_number - 1).future_grid_round_configs
        
                    player_config = json.loads(player.future_grid_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                    player.earlier_time = player_config[0]  # example: today
                    player.earlier_max = int(player_config[1])
                    player.later_time = player_config[2]
                    player.later_max = int(player_config[3])

                if self.round_number > Constants.num_grids and self.round_number < 2*Constants.num_grids + 1:
                    if player.second == "PG":
                        player.t_earliest = past_t_options[0]
                        player.t_middle = past_t_options[1]
                        player.t_latest = past_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["past_randomize_blocks"]:
                                for i in range(len(past_grid_round_configs)):
                                    random.shuffle(past_grid_round_configs[i])
                                random.shuffle(past_grid_round_configs)
                            player.past_grid_round_configs = json.dumps(past_grid_round_configs)
                        else:
                            player.past_grid_round_configs = player.in_round(self.round_number - 1).past_grid_round_configs

                        player_config = json.loads(player.past_grid_round_configs)[(self.round_number - Constants.num_grids - 1)//Constants.num_per_section][(self.round_number - Constants.num_grids - 1) % Constants.num_per_section]
                        player.earlier_time = player_config[0]  # example: today
                        player.earlier_max = int(player_config[1])
                        player.later_time = player_config[2]
                        player.later_max = int(player_config[3])

                if self.round_number > Constants.num_grids and self.round_number < Constants.num_sliders + Constants.num_grids + 1:
                    if player.second == "FV":
                        player.t_earliest = future_t_options[0]
                        player.t_middle = future_t_options[1]
                        player.t_latest = future_t_options[2]
                        if self.round_number - Constants.num_grids == 1:
                            if self.session.config["future_randomize_sliders"]:
                                for i in range(len(future_visual_round_configs)):
                                    random.shuffle(future_visual_round_configs[i]) 
                                random.shuffle(future_visual_round_configs)
                            player.future_visual_round_configs = json.dumps(future_visual_round_configs)
                        else:
                            player.future_visual_round_configs = player.in_round(self.round_number - 1).future_visual_round_configs
                            
                        # only go for the configurable number of sliders
                        future_player_config = json.loads(player.future_visual_round_configs)[(self.round_number - Constants.num_grids - 1)//Constants.num_per_section][(self.round_number - Constants.num_grids - 1) % Constants.num_per_section]
                        player.earlier_time = future_player_config[0]  # example: today
                        player.earlier_max = int(future_player_config[1])
                        player.later_time = future_player_config[2]
                        player.later_max = int(future_player_config[3])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    first = models.StringField()
    second = models.StringField()
    condition = models.IntegerField()
    consent_answer = models.StringField(initial="")

    lottery_answer = models.FloatField(blank=True, min=0, max=10000)
    dice_answer = models.FloatField(blank=True, min=0, max=10000)
    disease_answer = models.FloatField(blank=True, min=0, max=10000)
    check_1 = models.IntegerField(
        blank=True,
        choices=[[0, "Past jobs"], [1, "Future jobs"]],
        widget=widgets.RadioSelect,
    )
    check_2 = models.IntegerField(
        blank=True,
        choices=[[0, "Past jobs"], [1, "Future jobs"]],
        widget=widgets.RadioSelect,
    )

    earlier_max = models.IntegerField()
    later_max = models.IntegerField()
    earlier_time = models.StringField()
    later_time = models.StringField()

    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    instructions_1_start_time = models.StringField()
    instructions_1_finish_time = models.StringField()
    instructions_1_total_time = models.StringField()

    instructions_2_start_time = models.StringField()
    instructions_2_finish_time = models.StringField()
    instructions_2_total_time = models.StringField()

    t_earliest = models.StringField()
    t_middle = models.StringField()
    t_latest = models.StringField()

    grid_answer = models.StringField(blank=True)

################################################################################# FUTURE GRID PLAYER VARIABLES #################################################################################
    future_grid_round_configs = models.StringField()

################################################################################# PAST GRID PLAYER VARIABLES #################################################################################
    past_grid_round_configs = models.StringField()

################################################################################# FUTURE VISUAL PLAYER VARIABLES #################################################################################
    future_visual_round_configs = models.StringField()
    future_slider_one = models.IntegerField(blank=True)
    future_slider_two = models.IntegerField(blank=True)
    slider_two_last_clicked = models.IntegerField(blank=True)

################################################################################# PAST VISUAL PLAYER VARIABLES #################################################################################
    past_visual_round_configs = models.StringField()
    past_slider_one = models.IntegerField(blank=True)
    past_slider_two = models.IntegerField(blank=True)