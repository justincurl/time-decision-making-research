from typing import Optional
import random, pickle, codecs, json, itertools
from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets
from .block import Block

author = "Justin Curl <jcurl@princeton.edu>"

class Constants(BaseConstants):
    name_in_url = "Module1"
    players_per_group = None
    num_rounds = 30
    num_per_section = 5
    num_sliders = 15
    num_grid_rounds = 1


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
        future_CTB_right_values = self.session.config["future_CTB_right_values"].split(", ")
        future_CTB_right_values = [float(i) for i in future_CTB_right_values]
        future_CTB_left_values = self.session.config["future_CTB_left_values"].split(", ")
        future_CTB_left_values = [float(i) for i in future_CTB_left_values]
        future_CTB_t_earliers = self.session.config['future_CTB_t_earliers'].split(', ')
        future_CTB_t_laters = self.session.config['future_CTB_t_laters'].split(', ')
        future_block_order = [i for i in range(self.session.config["future_num_blocks"])]

        future_block_size = self.session.config["future_block_size"]

        future_CTB_blocks_left = []
        future_CTB_blocks_right = []
        for i in range(self.session.config["future_num_blocks"]):
            future_CTB_blocks_left.append(future_CTB_left_values[i*future_block_size:(i+1)*future_block_size])
            future_CTB_blocks_right.append(future_CTB_right_values[i*future_block_size:(i+1)*future_block_size])

        future_Blocks = []
        for i in range(len(future_block_order)):
            future_Blocks.append(
                Block(
                    left_values=future_CTB_blocks_left[i],
                    right_values=future_CTB_blocks_right[i],
                    earlier_time=future_CTB_t_earliers[i],
                    later_time=future_CTB_t_laters[i],
                    number_of_choices=6,
                    block_index=i
                )
            )

    ###################################################################################################### PAST GRID SET UP ######################################################################################################
        past_CTB_right_values = self.session.config["past_CTB_right_values"].split(", ")
        past_CTB_right_values = [float(i) for i in past_CTB_right_values]
        past_CTB_left_values = self.session.config["past_CTB_left_values"].split(", ")
        past_CTB_left_values = [float(i) for i in past_CTB_left_values]
        past_CTB_t_earliers = self.session.config['past_CTB_t_earliers'].split(', ')
        past_CTB_t_laters = self.session.config['past_CTB_t_laters'].split(', ')
        past_block_order = [i for i in range(self.session.config["past_num_blocks"])]

        past_block_size = self.session.config["past_block_size"]

        past_CTB_blocks_left = []
        past_CTB_blocks_right = []
        for i in range(self.session.config["past_num_blocks"]):
            past_CTB_blocks_left.append(past_CTB_left_values[i*past_block_size:(i+1)*past_block_size])
            past_CTB_blocks_right.append(past_CTB_right_values[i*past_block_size:(i+1)*past_block_size])

        past_Blocks = []
        for i in range(len(past_block_order)):
            past_Blocks.append(
                Block(
                    left_values=past_CTB_blocks_left[i],
                    right_values=past_CTB_blocks_right[i],
                    earlier_time=past_CTB_t_earliers[i],
                    later_time=past_CTB_t_laters[i],
                    number_of_choices=6,
                    block_index=i
                )
            )

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
        
        future_round_configs = []
        future_round_section = []
        for i in range(len(future_t_earliers)):
            for j in range(Constants.num_per_section):
                future_round_section.append((future_t_earliers[i][j], future_payment_earliers[i][j], future_t_laters[i][j], future_payment_laters[i][j]))
            future_round_configs.append(future_round_section)
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
        
        past_round_configs = []
        past_round_section = []
        for i in range(len(past_t_earliers)):
            for j in range(Constants.num_per_section):
                past_round_section.append((past_t_earliers[i][j], past_payment_earliers[i][j], past_t_laters[i][j], past_payment_laters[i][j]))
            past_round_configs.append(past_round_section)
            past_round_section = []

    ###################################################################################################### PLAYERS SET UP ###################################################################################################### 
        for player in self.get_players():
            
            if self.round_number == 1:
                player_order = next(start_at_random)
                player.condition = player_order[0]
                player.first = player_order[1]
                player.second = player_order[2]
            else:
                player.condition = player.in_round(self.round_number - 1).condition
                player.first = player.in_round(self.round_number - 1).first
                player.second = player.in_round(self.round_number - 1).second
        
        ################################################################################################### IF CONDITION 1 or 2 ###################################################################################################
            if player.first == "PV":
                ################################################################################################### PAST VISUAL WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_sliders:
                    player.past_t_earliest = past_t_options[0]
                    player.past_t_middle = past_t_options[1]
                    player.past_t_latest = past_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["past_randomize_sliders"]:
                            random.shuffle(past_round_configs)
                        player.past_round_configs = json.dumps(past_round_configs)
                    else:
                        player.past_round_configs = player.in_round(self.round_number - 1).past_round_configs
                    if self.round_number <= Constants.num_sliders:    
                        past_player_config = json.loads(player.past_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                        player.past_earlier_time = past_player_config[0]  # example: today
                        player.past_earlier_max = int(past_player_config[1])
                        player.past_later_time = past_player_config[2]
                        player.past_later_max = int(past_player_config[3])

                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if player.second == "FV":
                        player.future_t_earliest = future_t_options[0]
                        player.future_t_middle = future_t_options[1]
                        player.future_t_latest = future_t_options[2]
                        if self.round_number - Constants.num_sliders == 1:
                            if self.session.config["future_randomize_sliders"]:
                                random.shuffle(future_round_configs)
                            player.future_round_configs = json.dumps(future_round_configs)
                        else:
                            player.future_round_configs = player.in_round(self.round_number - 1).future_round_configs    
                            future_player_config = json.loads(player.future_round_configs)[(self.round_number - Constants.num_sliders - 1)//Constants.num_per_section][(self.round_number - Constants.num_sliders - 1) % Constants.num_per_section]
                            player.future_earlier_time = future_player_config[0]  # example: today
                            player.future_earlier_max = int(future_player_config[1])
                            player.future_later_time = future_player_config[2]
                            player.future_later_max = int(future_player_config[3])

                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_sliders + Constants.num_grid_rounds + 1:    
                    if player.second == "PG":
                        player.past_blocks = codecs.encode(pickle.dumps(past_Blocks), "base64").decode()
                        if self.session.config["past_randomize_blocks"]:
                            past_to_shuffle_block_order = [past_block_order[0:Constants.num_per_section], past_block_order[Constants.num_per_section:2*Constants.num_per_section], past_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                            random.shuffle(past_to_shuffle_block_order)
                            past_block_order = []
                            for i in range(len(past_to_shuffle_block_order)):
                                past_block_order += past_to_shuffle_block_order[i]
                        player.past_block_order = json.dumps(past_block_order)

        ################################################################################################### IF CONDITION 3 or 4 ###################################################################################################
            elif player.first == "FV":
                ################################################################################################### FUTURE VISUAL WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_sliders:
                    player.future_t_earliest = future_t_options[0]
                    player.future_t_middle = future_t_options[1]
                    player.future_t_latest = future_t_options[2]
                    if self.round_number == 1:
                        if self.session.config["future_randomize_sliders"]:
                            random.shuffle(future_round_configs)
                        player.future_round_configs = json.dumps(future_round_configs)
                    else:
                        player.future_round_configs = player.in_round(self.round_number - 1).future_round_configs
                        
                    future_player_config = json.loads(player.future_round_configs)[(self.round_number - 1)//Constants.num_per_section][(self.round_number - 1) % Constants.num_per_section]
                    player.future_earlier_time = future_player_config[0]  # example: today
                    player.future_earlier_max = int(future_player_config[1])
                    player.future_later_time = future_player_config[2]
                    player.future_later_max = int(future_player_config[3])
                
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if player.second == "PV":
                        player.past_t_earliest = past_t_options[0]
                        player.past_t_middle = past_t_options[1]
                        player.past_t_latest = past_t_options[2]
                        if self.round_number - Constants.num_sliders == 1:
                            if self.session.config["past_randomize_sliders"]:
                                random.shuffle(past_round_configs)
                            player.past_round_configs = json.dumps(past_round_configs)
                        else:
                            player.past_round_configs = player.in_round(self.round_number - 1).past_round_configs
                            
                        past_player_config = json.loads(player.past_round_configs)[(self.round_number - Constants.num_sliders - 1)//Constants.num_per_section][(self.round_number - Constants.num_sliders - 1) % Constants.num_per_section]
                        player.past_earlier_time = past_player_config[0]  # example: today
                        player.past_earlier_max = int(past_player_config[1])
                        player.past_later_time = past_player_config[2]
                        player.past_later_max = int(past_player_config[3])
                
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_sliders + Constants.num_grid_rounds + 1: 
                    if player.second == "FG":
                        player.future_blocks = codecs.encode(pickle.dumps(future_Blocks), "base64").decode()
                        if self.session.config["future_randomize_blocks"]:
                            future_to_shuffle_block_order = [future_block_order[0:Constants.num_per_section], future_block_order[Constants.num_per_section:2*Constants.num_per_section], future_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                            random.shuffle(future_to_shuffle_block_order)
                            future_block_order = []
                            for i in range(len(future_to_shuffle_block_order)):
                                future_block_order += future_to_shuffle_block_order[i]
                        player.future_block_order = json.dumps(future_block_order)

        ################################################################################################### IF CONDITION 5 or 6 ###################################################################################################
            elif player.first == "PG":
                ################################################################################################### PAST GRID WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_grid_rounds:
                    player.past_blocks = codecs.encode(pickle.dumps(past_Blocks), "base64").decode()
                    if self.session.config["past_randomize_blocks"]:
                        past_to_shuffle_block_order = [past_block_order[0:Constants.num_per_section], past_block_order[Constants.num_per_section:2*Constants.num_per_section], past_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                        random.shuffle(past_to_shuffle_block_order)
                        past_block_order = []
                        for i in range(len(past_to_shuffle_block_order)):
                            past_block_order += past_to_shuffle_block_order[i]
                    player.past_block_order = json.dumps(past_block_order)

                if self.round_number > Constants.num_grid_rounds and self.round_number < 2*Constants.num_grid_rounds + 1:
                    if player.second == "FG":
                        player.future_blocks = codecs.encode(pickle.dumps(future_Blocks), "base64").decode()
                        if self.session.config["future_randomize_blocks"]:
                            future_to_shuffle_block_order = [future_block_order[0:Constants.num_per_section], future_block_order[Constants.num_per_section:2*Constants.num_per_section], future_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                            random.shuffle(future_to_shuffle_block_order)
                            future_block_order = []
                            for i in range(len(future_to_shuffle_block_order)):
                                future_block_order += future_to_shuffle_block_order[i]
                        player.future_block_order = json.dumps(future_block_order)
                
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    if player.second == "PV":
                        player.past_t_earliest = past_t_options[0]
                        player.past_t_middle = past_t_options[1]
                        player.past_t_latest = past_t_options[2]
                        if self.round_number - Constants.num_grid_rounds == 1:
                            if self.session.config["past_randomize_sliders"]:
                                random.shuffle(past_round_configs)
                            player.past_round_configs = json.dumps(past_round_configs)
                        else:
                            player.past_round_configs = player.in_round(self.round_number - 1).past_round_configs
                        
                        past_player_config = json.loads(player.past_round_configs)[(self.round_number - Constants.num_grid_rounds - 1)//Constants.num_per_section][(self.round_number - Constants.num_grid_rounds - 1) % Constants.num_per_section]
                        player.past_earlier_time = past_player_config[0]  # example: today
                        player.past_earlier_max = int(past_player_config[1])
                        player.past_later_time = past_player_config[2]
                        player.past_later_max = int(past_player_config[3])

        ################################################################################################### IF CONDITION 7 or 8 ###################################################################################################
            elif player.first == "FG":
                ################################################################################################### FUTURE GRID WITHIN-PLAYER RANDOMIZATION ###################################################################################################
                if self.round_number <= Constants.num_grid_rounds:
                    player.future_blocks = codecs.encode(pickle.dumps(future_Blocks), "base64").decode()
                    if self.session.config["future_randomize_blocks"]:
                        future_to_shuffle_block_order = [future_block_order[0:Constants.num_per_section], future_block_order[Constants.num_per_section:2*Constants.num_per_section], future_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                        random.shuffle(future_to_shuffle_block_order)
                        future_block_order = []
                        for i in range(len(future_to_shuffle_block_order)):
                            future_block_order += future_to_shuffle_block_order[i]
                    player.future_block_order = json.dumps(future_block_order)

                if self.round_number > Constants.num_grid_rounds and self.round_number < 2*Constants.num_grid_rounds + 1:
                    if player.second == "PG":
                        player.past_blocks = codecs.encode(pickle.dumps(past_Blocks), "base64").decode()
                        if self.session.config["past_randomize_blocks"]:
                            past_to_shuffle_block_order = [past_block_order[0:Constants.num_per_section], past_block_order[Constants.num_per_section:2*Constants.num_per_section], past_block_order[2*Constants.num_per_section:3*Constants.num_per_section]]
                            random.shuffle(past_to_shuffle_block_order)
                            past_block_order = []
                            for i in range(len(past_to_shuffle_block_order)):
                                past_block_order += past_to_shuffle_block_order[i]
                        player.past_block_order = json.dumps(past_block_order)

                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_sliders + Constants.num_grid_rounds + 1:
                    if player.second == "FV":
                        player.future_t_earliest = future_t_options[0]
                        player.future_t_middle = future_t_options[1]
                        player.future_t_latest = future_t_options[2]
                        if self.round_number - Constants.num_grid_rounds == 1:
                            if self.session.config["future_randomize_sliders"]:
                                random.shuffle(future_round_configs)
                            player.future_round_configs = json.dumps(future_round_configs)
                        else:
                            player.future_round_configs = player.in_round(self.round_number - 1).future_round_configs
                            
                        # only go for the configurable number of sliders
                        future_player_config = json.loads(player.future_round_configs)[(self.round_number - Constants.num_grid_rounds - 1)//Constants.num_per_section][(self.round_number - Constants.num_grid_rounds - 1) % Constants.num_per_section]
                        player.future_earlier_time = future_player_config[0]  # example: today
                        player.future_earlier_max = int(future_player_config[1])
                        player.future_later_time = future_player_config[2]
                        player.future_later_max = int(future_player_config[3])

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

################################################################################# FUTURE GRID PLAYER VARIABLES #################################################################################
    future_grid_start_time = models.StringField()
    future_grid_finish_time = models.StringField()
    future_grid_total_time = models.StringField()

    future_blocks = models.LongStringField(initial="")
    future_current_block_step = models.IntegerField(initial=0)
    """Current step the user is in
    """
    
    future_question_answers = models.StringField(initial="")
    """Serialized JSON array representing the players answers
    
    The JSON array is two dimensional - the elements of the array represent
    the selected choices per block where the element index matches the index
    of the block in config.BLOCKS (0-based). The elements itself are also arrays where
    each number inside the element represents the index of the choice the
    player made in the respective question - starting from 1.
    """
    future_block_order = models.StringField(initial="")

    def goto_next_future_block_step(self) -> None:
        """Advances the player to the next step
        """
        self.future_current_block_step += 1

    def get_current_future_block_step(self) -> int:
        """The player's current step

        :return: Current step
        """
        return self.future_current_block_step

    def get_current_future_block_index(self) -> int:
        """Get the index of the block to be currently displayed

        This function returns the 0-based index of the block in `config.BLOCKS`
        to be displayed to the player taking into account the potentially
        randomized order.
        This method will return `-1` if `self.current_step` exceed the number
        of configured blocks.

        :return: Index of block to display or `-1`
        """
        if self.future_current_block_step < len(pickle.loads(codecs.decode(self.future_blocks.encode(), "base64"))):
            return json.loads(self.future_block_order)[self.future_current_block_step]
        else:
            return -1

    def get_current_future_block(self) -> Optional[Block]:
        """Get the current Block to display

        This function returns `None` if there is nothing left to display.

        :return: Block to display or `None`
        """
        future_block_index = self.get_current_future_block_index()
        if 0 <= future_block_index < len(pickle.loads(codecs.decode(self.future_blocks.encode(), "base64"))):
            return pickle.loads(codecs.decode(self.future_blocks.encode(), "base64"))[future_block_index]
        else:
            return False

################################################################################# PAST GRID PLAYER VARIABLES #################################################################################

    past_grid_start_time = models.StringField()
    past_grid_finish_time = models.StringField()
    past_grid_total_time = models.StringField()

    past_blocks = models.LongStringField(initial="")
    past_current_block_step = models.IntegerField(initial=0)
    """Current step the user is in
    """
    
    past_question_answers = models.StringField(initial="")
    """Serialized JSON array representing the players answers
    
    The JSON array is two dimensional - the elements of the array represent
    the selected choices per block where the element index matches the index
    of the block in config.BLOCKS (0-based). The elements itself are also arrays where
    each number inside the element represents the index of the choice the
    player made in the respective question - starting from 1.
    """
    past_block_order = models.StringField(initial="")

    def goto_next_past_block_step(self) -> None:
        """Advances the player to the next step
        """
        self.past_current_block_step += 1

    def get_current_past_block_step(self) -> int:
        """The player's current step

        :return: Current step
        """
        return self.past_current_block_step

    def get_current_past_block_index(self) -> int:
        """Get the index of the block to be currently displayed

        This function returns the 0-based index of the block in `config.BLOCKS`
        to be displayed to the player taking into account the potentially
        randomized order.
        This method will return `-1` if `self.current_step` exceed the number
        of configured blocks.

        :return: Index of block to display or `-1`
        """
        
        if self.past_current_block_step < len(pickle.loads(codecs.decode(self.past_blocks.encode(), "base64"))):
            return json.loads(self.past_block_order)[self.past_current_block_step]
        else:
            return -1

    def get_current_past_block(self) -> Optional[Block]:
        """Get the current Block to display

        This function returns `None` if there is nothing left to display.

        :return: Block to display or `None`
        """
        past_block_index = self.get_current_past_block_index()
        if 0 <= past_block_index < len(pickle.loads(codecs.decode(self.past_blocks.encode(), "base64"))):
            return pickle.loads(codecs.decode(self.past_blocks.encode(), "base64"))[past_block_index]
        else:
            return False

################################################################################# FUTURE VISUAL PLAYER VARIABLES #################################################################################

    future_round_configs = models.StringField()
    future_t_earliest = models.StringField()
    future_t_middle = models.StringField()
    future_t_latest = models.StringField()
    
    future_visual_start_time = models.StringField()
    future_visual_finish_time = models.StringField()
    future_visual_total_time = models.StringField()

    future_earlier_max = models.IntegerField()
    future_later_max = models.IntegerField()
    future_earlier_time = models.StringField()
    future_later_time = models.StringField()

    future_slider_value = models.IntegerField()
    future_slider_one = models.IntegerField()
    future_check_slider_one = models.IntegerField(blank=True)
    future_slider_two = models.IntegerField()
    future_check_slider_two = models.IntegerField(blank=True)

################################################################################# PAST VISUAL PLAYER VARIABLES #################################################################################

    past_round_configs = models.StringField()
    past_t_earliest = models.StringField()
    past_t_middle = models.StringField()
    past_t_latest = models.StringField()
    
    past_visual_start_time = models.StringField()
    past_visual_finish_time = models.StringField()
    past_visual_total_time = models.StringField()

    past_earlier_max = models.IntegerField()
    past_later_max = models.IntegerField()
    past_earlier_time = models.StringField()
    past_later_time = models.StringField()

    past_slider_value = models.IntegerField()
    past_slider_one = models.IntegerField()
    past_check_slider_one = models.IntegerField(blank=True)
    past_slider_two = models.IntegerField()
    past_check_slider_two = models.IntegerField(blank=True)