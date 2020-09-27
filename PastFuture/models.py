import json
from typing import Optional, List

import random

from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

from .block import Block
from .plot import Plot
from .config import BLOCKS1, BLOCKS2, PLOTS1, PLOTS2, RANDOMIZE_PLOTS, RANDOMIZE_BLOCKS

author = "Justin Curl <jcurl@princeton.edu>"

doc = """
use Convex Time Budget analysis to analyze 
"""


class Constants(BaseConstants):
    name_in_url = "PastFuture"
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        """Initializes the 
        session and creates the order in which the Blocks should be run through
        """
        import itertools
        listOfOptions = [
            (0, 'HLPast', 'HLFuture'),
            (1, 'HLPast', 'CTBPast'),
            (2, 'HLPast', 'CTBFuture'),
            (3, 'HLFuture', 'CTBPast'),
            (4, 'HLFuture', 'CTBFuture'),
            (5, 'CTBPast', 'CTBFuture'),
            (6, 'HLFuture', 'HLPast'),
            (7, 'CTBPast', 'HLPast'),
            (8, 'CTBFuture', 'HLPast'),
            (9, 'CTBPast', 'HLFuture'),
            (10, 'CTBFuture', 'HLFuture'),
            (11, 'CTBFuture', 'CTBPast'),
        ]

        rand_choice = random.choice(listOfOptions)
        ordering = itertools.cycle(listOfOptions)
        start_at_random = itertools.islice(ordering, rand_choice[0], None)
        for player in self.get_players():
            player_order = next(start_at_random)
            player.first = player_order[1]
            player.second = player_order[2]

            if player.first[:2] == 'HL':
                plot1_order = [i for i in range(len(PLOTS1))]
                if RANDOMIZE_PLOTS:
                    random.shuffle(plot1_order)
                player.plot1_order = json.dumps(plot1_order)
            else:
                block1_order = [i for i in range(len(BLOCKS1))]
                if RANDOMIZE_BLOCKS:
                    random.shuffle(block1_order)
                player.block1_order = json.dumps(block1_order)

            if player.second[:2] == 'HL':
                plot2_order = [i for i in range(len(PLOTS1))]
                if RANDOMIZE_PLOTS:
                    random.shuffle(plot2_order)
                player.plot2_order = json.dumps(plot2_order)
            else:
                block2_order = [i for i in range(len(BLOCKS1))]
                if RANDOMIZE_BLOCKS:
                    random.shuffle(block2_order)
                player.block2_order = json.dumps(block2_order)


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

    take_risks = models.IntegerField(
        choices=[
            [0, '0 unwilling to take risks'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10 fully prepared to take risks']
        ], widget=widgets.RadioSelect, blank=True
    )

    benefit_today = models.IntegerField(
        choices=[
            [0, '0 completely unwilling to do so'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10 very willing to do so']
        ], widget=widgets.RadioSelect, blank=True
    )

    impulsive = models.IntegerField(
        choices=[
            [0, '0 not at all impulsive'],
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10 very impulsive']
        ], widget=widgets.RadioSelect, blank=True
    )

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
    current_plot_step = models.IntegerField(initial=0)

    first = models.StringField(initial="")
    second = models.StringField(initial="")
    set_1 = models.BooleanField(initial=True)

    consent_answer = models.StringField(initial="")

    question_answers = models.StringField(initial="")
    """Serialized JSON array representing the players answers
    
    The JSON array is two dimensional - the elements of the array represent
    the selected choices per block where the element index matches the index
    of the block in config.BLOCKS (0-based). The elements itself are also arrays where
    each number inside the element represents the index of the choice the
    player made in the respective question - starting from 1.
    """

    block1_order = models.StringField(initial="")

    block2_order = models.StringField(initial="")

    plot1_order = models.StringField(initial="")
    
    plot2_order = models.StringField(initial="")

    denominator = models.IntegerField(initial=0)

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
        if self.set_1:
            if self.current_block_step < len(BLOCKS1):
                return json.loads(self.block1_order)[self.current_block_step]
            else:
                return -1
        else:
            if self.current_block_step < len(BLOCKS2):
                return json.loads(self.block2_order)[self.current_block_step]
            else:
                return -1

    def get_current_block(self) -> Optional[Block]:
        """Get the current Block to display

        This function returns `None` if there is nothing left to display.

        :return: Block to display or `None`
        """
        if self.set_1:
            block_index = self.get_current_block_index()
            if 0 <= block_index < len(BLOCKS1):
                return BLOCKS1[block_index]
            else:
                return False
        else:
            block_index = self.get_current_block_index()
            if 0 <= block_index < len(BLOCKS2):
                return BLOCKS2[block_index]
            else:
                return False

    def get_current_plot(self) -> Optional[Plot]:
        if self.set_1:
            if self.current_plot_step < len(PLOTS1):
                plot_index = json.loads(self.plot1_order)[
                    self.current_plot_step]
                if 0 <= plot_index < len(PLOTS1):
                    return PLOTS1[plot_index]
            else:
                print("none executed from get current plot")
                return False
        else:
            if self.current_plot_step < len(PLOTS2):
                plot_index = json.loads(self.plot2_order)[
                    self.current_plot_step]
                if 0 <= plot_index < len(PLOTS2):
                    return PLOTS2[plot_index]
            else:
                print("none executed from get current plot")
                return False

    def get_next_plot(self) -> Optional[Plot]:
        if self.set_1:
            if self.current_plot_step + 1 < len(PLOTS1):
                plot_index = json.loads(self.plot1_order)[
                    self.current_plot_step + 1]
                if 0 <= plot_index < len(PLOTS1):
                    return PLOTS1[plot_index]
            else:
                return False
        else:
            if self.current_plot_step + 1 < len(PLOTS2):
                plot_index = json.loads(self.plot2_order)[
                    self.current_plot_step + 1]
                if 0 <= plot_index < len(PLOTS2):
                    return PLOTS2[plot_index]
            else:
                return False
