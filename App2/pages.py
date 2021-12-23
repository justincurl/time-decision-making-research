from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class Start(Page):
    pass

class Instructions(Page):
    form_model = 'player'
    form_fields = ["is_mobile_original_method", "is_mobile"]

    def is_displayed(self):
        if self.round_number == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False
    
    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class DirectGrowthBefore(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'direct_growth', 'slider_direct_ever_clicked']

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
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.direct_start_time), "%H:%M:%S")
        self.player.direct_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()


class DirectGrowthAfter(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'direct_growth','slider_direct_ever_clicked']

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
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.direct_start_time), "%H:%M:%S")
        self.player.direct_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class DecisionPast(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['past_choice']

    def is_displayed(self):
        return (self.player.plot_condition == 1 and self.round_number <= Constants.num_choices) or (self.player.plot_condition == 2 and self.round_number > Constants.num_choices)


    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

        # specify info for progress bar
        if self.player.plot_condition == 1:
            page = self.subsession.round_number
        else:
            page = self.subsession.round_number - Constants.num_choices
        
        return {
            'page':            page,
            'payoff_delayed':  self.participant.vars['past_ictv_delayed_payoffs'][page - 1]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.past_set_delayed_payoffs()
        self.player.past_update_switching_row()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()
    
class DecisionFuture(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = models.Player
    form_fields = ['future_choice']

    def is_displayed(self):
        return (self.player.plot_condition == 2 and self.round_number <= Constants.num_choices) or (self.player.plot_condition == 1 and self.round_number > Constants.num_choices)

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

    # specify info for progress bar
        if self.player.plot_condition == 2:
            page = self.subsession.round_number
        else:
            page = self.subsession.round_number - Constants.num_choices
            
        
        return {
            'page':            page,
            'payoff_delayed':  self.participant.vars['future_ictv_delayed_payoffs'][page - 1]
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.future_set_delayed_payoffs()
        self.player.future_update_switching_row()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()


class Check1(Page):
    form_model = "player"
    form_fields = ["check_1"]

    def is_displayed(self):
        return (
            self.round_number == Constants.num_choices
        )

class Check2(Page):
    form_model = "player"
    form_fields = ["check_2"]

    def is_displayed(self):
        return (
            self.round_number == 2*Constants.num_choices
        )

# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
def generate_page_sequence():
    return (
        [Instructions] +
        [DirectGrowthBefore] +
        [DecisionPast] +
        [DecisionFuture] +
        [Check1] +
        [Check2] +
        [DirectGrowthAfter]
    )

page_sequence = generate_page_sequence()

