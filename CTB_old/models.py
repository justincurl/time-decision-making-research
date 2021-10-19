import json
from typing import Optional, List

import random

from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

from .block import Block
from .plot import Plot
from .config import BLOCKS, PLOTS, RANDOMIZE_PLOTS, RANDOMIZE_BLOCKS

author = "Justin Curl <jcurl@princeton.edu>"

doc = """
use Convex Time Budget analysis to analyze 
"""


class Constants(BaseConstants):
    name_in_url = "CTB"
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        """Initializes the 
        session and creates the order in which the Blocks should be run through
        """
        import itertools

        randomFirst = random.choice([True, False])
        ordering = itertools.cycle([randomFirst, not randomFirst])
        for player in self.get_players():
            if self.round_number == 1:
                player.hl_second = next(ordering)
            else:
                player.hl_second = not player.in_round(
                    self.round_number - 1).hl_second
            if player.hl_second:

                plot_order = [i for i in range(len(PLOTS))]
                if RANDOMIZE_PLOTS:
                    random.shuffle(plot_order)
                player.plot_order = json.dumps(plot_order)
            else:
                block_order = [i for i in range(len(BLOCKS))]
                if RANDOMIZE_BLOCKS:
                    random.shuffle(block_order)
                player.block_order = json.dumps(block_order)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    start_time = models.StringField()
    finish_time = models.StringField()
    total_time = models.StringField()

    device_type = models.IntegerField(
        choices=[
            [1, 'Desktop Computer'],
            [2, 'Laptop Computer'],
            [3, 'Smartphone'],
            [4, 'Tablet'],
            [5, 'Something Else']
        ], blank=True
    )

    race = models.StringField()
    education = models.IntegerField(
        choices=[
            [1, 'I do not have a high school degree or GED '],
            [2, 'Regular high school degree '],
            [3, 'GED or alternative credential '],
            [4, 'Some college credit, no degree'],
            [5, 'Associate’s degree (for example: AA, AS) '],
            [6, 'Bachelor’s degree (for example: BA, BS) '],
            [7, 'Graduate or professional degree ']
        ], blank=True, widget=widgets.RadioSelect
    )

    gender = models.IntegerField(blank=True, choices=[
        [1, 'Male'],
        [2, 'Female'],
    ], widget=widgets.RadioSelect)

    ethnicity = models.BooleanField(blank=True, choices=[
        [True, 'Yes'],
        [False, 'No']
    ], widget=widgets.RadioSelect)

    age = models.IntegerField(blank=True, min=18, max=110)

    zipcode = models.IntegerField(blank=True, min=0, max=99999)

    lottery_answer = models.FloatField(blank=True, min=0, max=10000)

    dice_answer = models.FloatField(blank=True, min=0, max=10000)

    disease_answer = models.FloatField(blank=True, min=0, max=10000)

    feedback = models.LongStringField(blank=True)

    current_block_step = models.IntegerField(initial=0)
    """Current step the user is in
    """
    current_plot_step = models.IntegerField(initial=0)

    hl_second = models.BooleanField(initial=False)

    consent_answer = models.StringField(initial="")

    question_answers = models.StringField(initial="")
    """Serialized JSON array representing the players answers
    
    The JSON array is two dimensional - the elements of the array represent
    the selected choices per block where the element index matches the index
    of the block in config.BLOCKS (0-based). The elements itself are also arrays where
    each number inside the element represents the index of the choice the
    player made in the respective question - starting from 1.
    """

    plot_order = models.StringField(initial="")
    block_order = models.StringField(initial="")
    attention_check = models.StringField(initial="")

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
        if self.current_block_step < len(BLOCKS):
            return json.loads(self.block_order)[self.current_block_step]
        else:
            return -1

    def get_current_block(self) -> Optional[Block]:
        """Get the current Block to display

        This function returns `None` if there is nothing left to display.

        :return: Block to display or `None`
        """
        block_index = self.get_current_block_index()
        if 0 <= block_index < len(BLOCKS):
            return BLOCKS[block_index]
        else:
            return False

    def get_current_plot(self) -> Optional[Plot]:
        if self.current_plot_step < len(PLOTS):
            plot_index = json.loads(self.plot_order)[
                self.current_plot_step]
            if 0 <= plot_index < len(PLOTS):
                return PLOTS[plot_index]
        else:
            print("none executed from get current plot")
            return False

    def get_next_plot(self) -> Optional[Plot]:
        if self.current_plot_step + 1 < len(PLOTS):
            plot_index = json.loads(self.plot_order)[
                self.current_plot_step + 1]
            if 0 <= plot_index < len(PLOTS):
                return PLOTS[plot_index]
        else:
            return False
