from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class Start(Page):
    pass

class Instructions(Page):
    pass

class DirectGrowth(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'direct_growth']

    def is_displayed(self):
        check_condition = False
        if self.player.direct_condition == 1 and self.round_number == 1:
            check_condition = True
        elif self.player.direct_condition == 2 and self.round_number == 2:
            check_condition = True

        if check_condition and json.loads(self.participant.vars["consent_answer"]) == 1:
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

def generate_page_sequence():
    return (
        [Instructions] +
        [DirectGrowth]
    )

page_sequence = generate_page_sequence()
