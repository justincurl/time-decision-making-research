import random
import json
from .models import Constants
import datetime
from ._builtin import Page, WaitPage
from otree.api import safe_json


class Start(Page):
    pass


class FutureGrid(Page):
    form_model = 'player'
    form_fields = ['future_grid_answer']

    def vars_for_template(self):
        question_instructions = "Jobs created"
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
            note = ""

        start_values = [self.player.earlier_max + x*(0-self.player.earlier_max)/(6-1) for x in range(6)]
        for i in range(len(start_values)):
            start_values[i] = "{:,.0f}".format(float(start_values[i]))

        end_values = [self.player.later_max + x*(0-self.player.later_max)/(6-1) for x in range(6)]
        for i in range(len(end_values)):
            end_values[i] = "{:,.0f}".format(float(end_values[i]))

        return dict(
            note=note,
            start_values=start_values,
            end_values=end_values,
            idxs=[i for i in range(6)],
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            question_instructions=question_instructions,
        )

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)
        return (
            (self.round_number <= self.player.session.config["future_num_blocks"])
        )

class FutureALL(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        return (
            self.round_number == 1
        )


class SectionDivider2(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        # display = False
        # if self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
        #     display = True
        return self.round_number == 6

class SectionDivider3(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        # display = False
        # if self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
        #     display = True
        return self.round_number == 11

def generate_page_sequence():
    return (
        [FutureALL] +
        [FutureGrid]
    )


page_sequence = generate_page_sequence()