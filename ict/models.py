from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from ict.setup import *
import random


author = 'Based on Felix Holzmeister code - modified by AA'
doc = 'Staircase time preference elicitation task as proposed by Falk et al. (2016), Working Paper.'


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs for first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        r_verbal_staircase_options = [
            (1, "Past"),
            (2, "Future"),
        ]

        for player in self.get_players():
            if self.round_number == 1:
                player.participant.vars['ict_delayed_payoffs'] = [Constants.payoff_delayed]
                player.participant.vars['ict_switching_row'] = 1

                player.participant.vars['ict_now'] = Constants.now
                player.participant.vars['ict_delayed'] = Constants.delayed
                player.participant.vars['ict_payoff_now'] = Constants.payoff_now
                player.staircase_condition = random.choice(r_verbal_staircase_options)[0]
            else:
                player.staircase_condition = player.in_round(self.round_number - 1).staircase_condition


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # add model fields to class player
    delayed_payoff = models.FloatField()
    choice = models.StringField()
    switching_row = models.IntegerField()
    staircase_condition = models.IntegerField()

    start_time = models.StringField()
    total_time = models.StringField()

    # set delayed payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def set_delayed_payoffs(self):

        # add current round's sure payoff to model field
        self.delayed_payoff = self.participant.vars['ict_delayed_payoffs'][self.round_number - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        if not self.round_number == Constants.num_choices:

            if self.choice == 'A':
                self.participant.vars['ict_delayed_payoffs'].append(
                    self.participant.vars['ict_delayed_payoffs'][self.round_number - 1]
                    + Constants.delta / 2 ** (self.round_number - 1)
                )

            elif self.choice == 'B':
                self.participant.vars['ict_delayed_payoffs'].append(
                    self.participant.vars['ict_delayed_payoffs'][self.round_number - 1]
                    - Constants.delta / 2 ** (self.round_number - 1)
                )

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def update_switching_row(self):

        if self.choice == 'B':
            self.participant.vars['ict_switching_row'] += 2 ** (Constants.num_choices - self.round_number)

        elif self.choice == 'I':
            self.participant.vars['ict_switching_row'] /= 2


            # implied switching row
            # --------------------------------------------------------------------------------------------------------
            self.in_round(choice_to_pay).switching_row = self.participant.vars['ict_switching_row']
