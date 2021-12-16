from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from App2.setup import *
import random, itertools

author = 'Based on Felix Holzmeister code - modified by AA'
doc = 'Staircase time preference elicitation task as proposed by Falk et al. (2016), Working Paper.'


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):

    # initiate list of sure payoffs for first round
    # ------------------------------------------------------------------------------------------------------------
    def creating_session(self):
        r_direct_options = [
            (1, "Before"),
            (2, "After"),
        ]

        r_plot_options = [
            (1, "Past First"),
            (2, "Future First"),
        ]

        for player in self.get_players():
            if self.round_number == 1:
                player.direct_condition = random.choice(r_direct_options)[0]
                player.plot_condition = random.choice(r_plot_options)[0]

                player.participant.vars['past_ictv_delayed_payoffs'] = [Constants.payoff_delayed]
                player.participant.vars['past_ictv_switching_row'] = 1

                player.participant.vars['past_ictv_now'] = Constants.now
                player.participant.vars['past_ictv_delayed'] = Constants.delayed
                player.participant.vars['past_ictv_payoff_now'] = Constants.payoff_now

                player.participant.vars['future_ictv_delayed_payoffs'] = [Constants.payoff_delayed]
                player.participant.vars['future_ictv_switching_row'] = 1

                player.participant.vars['future_ictv_now'] = Constants.now
                player.participant.vars['future_ictv_delayed'] = Constants.delayed
                player.participant.vars['future_ictv_payoff_now'] = Constants.payoff_now
            else:
                player.plot_condition = player.in_round(self.round_number - 1).plot_condition
                player.direct_condition = player.in_round(self.round_number - 1).direct_condition
               


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):
    plot_condition = models.IntegerField()
    direct_condition = models.IntegerField()

    slider_direct_growth = models.StringField()
    direct_growth = models.IntegerField(choices=[[1, "4% this year and no growth next year"], [2, "4% next year and no growth this year"]], widget=widgets.RadioSelect)

    instructions_1_start_time = models.StringField()
    instructions_1_total_time = models.StringField()

    direct_start_time = models.StringField()
    direct_total_time = models.StringField()

    start_time = models.StringField()
    total_time = models.StringField()

    # add model fields to class player
    future_delayed_payoff = models.FloatField()
    future_choice = models.StringField()
    future_switching_row = models.IntegerField()

    check_1 = models.IntegerField(
        blank=True,
        choices=[[0, "Past personal income growth"], [1, "Future personal income growth"]],
        widget=widgets.RadioSelect,
    )
    check_2 = models.IntegerField(
        blank=True,
        choices=[[0, "Past personal income growth"], [1, "Future personal income growth"]],
        widget=widgets.RadioSelect,
    )

    # set delayed payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def future_set_delayed_payoffs(self):
        if self.plot_condition == 2:
            round = self.round_number
        else:
            round = self.round_number - Constants.num_choices

        # add current round's sure payoff to model field
        self.future_delayed_payoff = self.participant.vars['future_ictv_delayed_payoffs'][round - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        if not round == Constants.num_choices:

            if self.future_choice == 'A':
                self.participant.vars['future_ictv_delayed_payoffs'].append(
                    self.participant.vars['future_ictv_delayed_payoffs'][round - 1]
                    + Constants.delta / 2 ** (round - 1)
                )

            elif self.future_choice == 'B':
                self.participant.vars['future_ictv_delayed_payoffs'].append(
                    self.participant.vars['future_ictv_delayed_payoffs'][round - 1]
                    - Constants.delta / 2 ** (round - 1)
                )

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def future_update_switching_row(self):
        if self.plot_condition == 2:
            round = self.round_number
        else:
            round = self.round_number - Constants.num_choices
    
        if self.future_choice == 'B':
            self.participant.vars['future_ictv_switching_row'] += 2 ** (Constants.num_choices - round)

        elif self.future_choice == 'I':
            self.participant.vars['future_ictv_switching_row'] /= 2


    # add model fields to class player
    past_delayed_payoff = models.FloatField()
    past_choice = models.StringField()
    past_switching_row = models.IntegerField()

    # set delayed payoff for next choice
    # ----------------------------------------------------------------------------------------------------------------
    def past_set_delayed_payoffs(self):
        if self.plot_condition == 1:
            round = self.round_number
        else:
            round = self.round_number - Constants.num_choices
        # add current round's sure payoff to model field
        self.past_delayed_payoff = self.participant.vars['past_ictv_delayed_payoffs'][round - 1]

        # determine sure payoff for next choice and append list of sure payoffs
        if not round == Constants.num_choices:

            if self.past_choice == 'A':
                self.participant.vars['past_ictv_delayed_payoffs'].append(
                    self.participant.vars['past_ictv_delayed_payoffs'][round - 1]
                    + Constants.delta / 2 ** (round - 1)
                )

            elif self.past_choice == 'B':
                self.participant.vars['past_ictv_delayed_payoffs'].append(
                    self.participant.vars['past_ictv_delayed_payoffs'][round - 1]
                    - Constants.delta / 2 ** (round - 1)
                )

    # update implied switching row each round
    # ----------------------------------------------------------------------------------------------------------------
    def past_update_switching_row(self):
        if self.plot_condition == 1:
            round = self.round_number
        else:
            round = self.round_number - Constants.num_choices
        if self.past_choice == 'B':
            self.participant.vars['past_ictv_switching_row'] += 2 ** (Constants.num_choices - round)

        elif self.past_choice == 'I':
            self.participant.vars['past_ictv_switching_row'] /= 2
