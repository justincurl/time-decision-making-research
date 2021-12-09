from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants




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

# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [
    PastDecision, FutureDecision
]
