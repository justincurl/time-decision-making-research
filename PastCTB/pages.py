import random
import json
import datetime

from ._builtin import Page
from .models import Constants

class Start(Page):
    pass

class BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = "player"
    form_fields = ["question_answers"]

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return (
            self.player.get_current_block()
            and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        step = self.player.get_current_block_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()

        questions_to_page = (len(current_block.left_values) * (step - 1)) + 1

        question_instructions = "Jobs created"

        return {
            "step": step,
            "block_index": block_index,
            "questions_to_page": questions_to_page,
            "num_blocks": self.session.config["past_num_blocks"],
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": question_instructions,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_block_step()


class PastInstructions(Page):
    def error_message(self, values):
        pass

    def is_displayed(self):
        return json.loads(self.participant.vars["consent_answer"]) == 1

class SectionDivider12(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )

    def is_displayed(self):
        valid_round = -1
        if self.player.section_order[0] == "12":
            valid_round = 1 # 1 + 0*num_sliders_per_section (6)
        elif self.player.section_order[1] == "12":
            valid_round = 7 # 1 + 1*num_sliders_per_section (6)
        elif self.player.section_order[2] == "12":
            valid_round = 13 # 1 + 2*num_sliders_per_section (6)
        return self.player.round_number == valid_round

class SectionDivider13(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        valid_round = -1
        if self.player.section_order[0] == "13":
            valid_round = 1 # 1 + 0*num_sliders_per_section (6)
        elif self.player.section_order[1] == "13":
            valid_round = 7 # 1 + 1*num_sliders_per_section (6)
        elif self.player.section_order[2] == "13":
            valid_round = 13 # 1 + 2*num_sliders_per_section (6)
        return self.player.round_number == valid_round

class SectionDivider23(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        valid_round = -1
        if self.player.section_order[0] == "23":
            valid_round = 1 # 1 + 0*num_sliders_per_section (6)
        elif self.player.section_order[1] == "23":
            valid_round = 7 # 1 + 1*num_sliders_per_section (6)
        elif self.player.section_order[2] == "23":
            valid_round = 13 # 1 + 2*num_sliders_per_section (6)
        return self.player.round_number == valid_round

def generate_page_sequence():
    return (
        [PastInstructions]
        + [SectionDivider12]
        + [BlockPage] * 6
        + [SectionDivider13]
        + [BlockPage] * 6
        + [SectionDivider23]
        + [BlockPage] * 6 
    )

page_sequence = generate_page_sequence()