import random
import json
from .models import Constants
import datetime
from ._builtin import Page, WaitPage
from otree.api import safe_json


class Start(Page):
    pass


class Slider(Page):
    form_model = 'player'
    form_fields = ['slider_one', 'check_slider_one', 'slider_two', 'check_slider_two']

    def vars_for_template(self):
        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)
        return (
            (self.player.round_number <= self.player.session.config["num_sliders"]) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def error_message(self, value):
        if value["slider_one"] == None or value['slider_two'] == None:
            return 'Please use the slider to make a decision.'
    
    def before_next_page(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(
            json.loads(self.player.start_time), "%H:%M:%S"
        )
        self.player.total_time = json.dumps(str(finish_time - start_time))

        self.player.slider_one = self.player.earlier_max - self.player.slider_one
        return super().before_next_page()

class PastInstructions(Page):
    def is_displayed(self):
        return (
            json.loads(self.participant.vars["consent_answer"]) == 1
        )

def generate_page_sequence():
    return (
        [PastInstructions] +
        [Slider]
    )


page_sequence = generate_page_sequence()