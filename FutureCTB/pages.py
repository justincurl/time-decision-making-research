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
            "num_blocks": self.session.config["future_num_blocks"],
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": question_instructions,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_block_step()


class FutureALL(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        return (
            self.round_number == 1 and
            json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FutureCTB(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        return (
            self.round_number == 1 and
            json.loads(self.participant.vars["consent_answer"]) == 1
        )

class SectionDivider1(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_block()
        return dict(
            curr_block=current_block
        )

class SectionDivider2(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_block()
        return dict(
            curr_block=current_block
        )

class SectionDivider3(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_block()
        return dict(
            curr_block=current_block
        )


def generate_page_sequence():
    return (
        [FutureALL]
        + [FutureCTB]
        + [BlockPage] * 6
        + [SectionDivider2]
        + [BlockPage] * 6
        + [SectionDivider3]
        + [BlockPage] * 6
    )

page_sequence = generate_page_sequence()