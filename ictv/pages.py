from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class Start(Page):
    pass

class Instructions(Page):
    def is_displayed(self):
        if self.round_number == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False
    
    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class DirectGrowthBefore(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'direct_growth']

    def is_displayed(self):
        check_condition = False
        if self.player.direct_condition == 1 and self.round_number == 1:
            check_condition = True

        if check_condition:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.direct_start_time = json.dumps(current_time)
            return True
        else:
            return False
    
    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.direct_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.direct_start_time), "%H:%M:%S")
        self.player.direct_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()


class DirectGrowthAfter(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'direct_growth']

    def is_displayed(self):
        check_condition = False
        if self.player.direct_condition == 2 and self.round_number == Constants.num_rounds:
            check_condition = True

        if check_condition:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.direct_start_time = json.dumps(current_time)
            return True
        else:
            return False
    
    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.direct_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.direct_start_time), "%H:%M:%S")
        self.player.direct_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()
# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.direct_start_time = json.dumps(current_time)

        # specify info for progress bar
        page = self.subsession.round_number
        
        return {
            'page':            page,
            'payoff_delayed':  self.participant.vars['ictv_delayed_payoffs'][page - 1]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_delayed_payoffs()
        self.player.update_switching_row()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.direct_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.direct_start_time), "%H:%M:%S")
        self.player.direct_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
def generate_page_sequence():
    return (
        [Instructions] +
        [DirectGrowthBefore] +
        [Decision] +
        [DirectGrowthAfter]
    )

page_sequence = generate_page_sequence()

