from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import json
import datetime


# Fixation cross
class Fixation(Page):
    form_model = "player"
    timeout_seconds = 0.5

    def is_displayed(self):
        return (self.round_number > 1) and self.session.config["fixation_on"]


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class FutureDecision(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['choice']
    def is_displayed(self):
        return self.player.staircase_condition == 2

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

        # specify info for progress bar
        page = self.subsession.round_number

        return {
            'page':            page,
            'payoff_delayed':  self.participant.vars['ict_delayed_payoffs'][page - 1]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_delayed_payoffs()
        self.player.update_switching_row()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PastDecision(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['choice']
    
    def is_displayed(self):
        return self.player.staircase_condition == 1

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

        # specify info for progress bar
        page = self.subsession.round_number

        return {
            'page':            page,
            'payoff_delayed':  self.participant.vars['ict_delayed_payoffs'][page - 1]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_delayed_payoffs()
        self.player.update_switching_row()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [
    Fixation, PastDecision, FutureDecision
]
