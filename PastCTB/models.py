import json
from typing import Optional, List

import random, pickle, codecs

from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

from .block import Block

author = "Justin Curl <jcurl@princeton.edu>"

doc = """
use Convex Time Budget analysis to analyze 
"""


class Constants(BaseConstants):
    name_in_url = "PastCTB"
    players_per_group = None
    num_rounds = 1
    max_blocks = 20
    questions_per_section = 4


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        """Initializes the 
        session and creates the order in which the Blocks should be run through
        """
        CTB_right_values = self.session.config["past_CTB_right_values"].split(", ")
        CTB_right_values = [float(i) for i in CTB_right_values]
        CTB_left_values = self.session.config["past_CTB_left_values"].split(", ")
        CTB_left_values = [float(i) for i in CTB_left_values]
        CTB_t_earliers = self.session.config['past_CTB_t_earliers'].split(', ')
        CTB_t_laters = self.session.config['past_CTB_t_laters'].split(', ')
        block_order = [i for i in range(self.session.config["past_num_blocks"])]

        block_size = self.session.config["past_block_size"]

        CTB_blocks_left = []
        CTB_blocks_right = []
        for i in range(self.session.config["past_num_blocks"]):
            CTB_blocks_left.append(CTB_left_values[i*block_size:(i+1)*block_size])
            CTB_blocks_right.append(CTB_right_values[i*block_size:(i+1)*block_size])

        Blocks = []
        for i in range(len(block_order)):
            Blocks.append(Block(
                left_values=CTB_blocks_left[i],
                right_values=CTB_blocks_right[i],
                t_earlier=CTB_t_earliers[i],
                t_later=CTB_t_laters[i],
                number_of_choices=6,
                block_index=i
                )
            )

        for player in self.get_players():
            player.blocks = codecs.encode(pickle.dumps(Blocks), "base64").decode()
            if self.round_number == 1:
                if self.session.config["past_randomize_blocks"]:
                    to_shuffle_block_order = [block_order[0:Constants.questions_per_section], block_order[Constants.questions_per_section:2*Constants.questions_per_section], block_order[2*Constants.questions_per_section:3*Constants.questions_per_section]]
                    random.shuffle(to_shuffle_block_order)
                    block_order = []
                    for i in range(len(to_shuffle_block_order)):
                        block_order += to_shuffle_block_order[i]
            else:
                block_order = player.in_round(self.round_number - 1).block_order
            player.block_order = json.dumps(block_order)
            

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    blocks = models.LongStringField(initial="")

    current_block_step = models.IntegerField(initial=0)
    """Current step the user is in
    """
    current_plot_step = models.IntegerField(initial=0)


    consent_answer = models.StringField(initial="")

    question_answers = models.StringField(initial="")
    """Serialized JSON array representing the players answers
    
    The JSON array is two dimensional - the elements of the array represent
    the selected choices per block where the element index matches the index
    of the block in config.BLOCKS (0-based). The elements itself are also arrays where
    each number inside the element represents the index of the choice the
    player made in the respective question - starting from 1.
    """

    block_order = models.StringField(initial="")

    def goto_next_plot_step(self) -> None:
        self.current_plot_step += 1

    def goto_next_block_step(self) -> None:
        """Advances the player to the next step
        """
        self.current_block_step += 1

    def get_current_block_step(self) -> int:
        """The player's current step

        :return: Current step
        """
        return self.current_block_step

    def get_current_block_index(self) -> int:
        """Get the index of the block to be currently displayed

        This function returns the 0-based index of the block in `config.BLOCKS`
        to be displayed to the player taking into account the potentially
        randomized order.
        This method will return `-1` if `self.current_step` exceed the number
        of configured blocks.

        :return: Index of block to display or `-1`
        """
        
        if self.current_block_step < len(pickle.loads(codecs.decode(self.blocks.encode(), "base64"))):
            return json.loads(self.block_order)[self.current_block_step]
        else:
            return -1

    def get_current_block(self) -> Optional[Block]:
        """Get the current Block to display

        This function returns `None` if there is nothing left to display.

        :return: Block to display or `None`
        """
        block_index = self.get_current_block_index()
        if 0 <= block_index < len(pickle.loads(codecs.decode(self.blocks.encode(), "base64"))):
            return pickle.loads(codecs.decode(self.blocks.encode(), "base64"))[block_index]
        else:
            return False