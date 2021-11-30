import random
import json
import datetime

from Module1 import block
from ._builtin import Page
from .models import Constants

class Start(Page):
    pass

######################################################################## FUTURE PAGES ########################################################################
class FG1_1_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        check_round_number = False
        if self.player.round_number == 1 or self.player.round_number == Constants.num_grid_rounds + 1 or self.player.round_number == Constants.num_sliders + 1:
            check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FG1_2_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FG2_G_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True
        
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FG2_V_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FG_BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = "player"
    form_fields = ["future_question_answers"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        # This page will only be displayed when there are blocks left
        return (
            check_condition and self.player.get_current_future_block() and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        step = self.player.get_current_future_block_step() + 1
        block_index = self.player.get_current_future_block_index() + 1
        current_block = self.player.get_current_future_block()

        questions_to_page = (len(current_block.left_values) * (step - 1)) + 1

        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if block_index == 1 or block_index == 6 or block_index == 11:
            note = ""

        return {
            "step": step,
            "block_index": block_index,
            "questions_to_page": questions_to_page,
            "num_blocks": self.session.config["future_num_blocks"],
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": "Jobs created",
            "note": note
        }

    def before_next_page(self):
        self.player.goto_next_future_block_step()


class FG2_Divider(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )
        

class FG3_Divider(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_future_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV1_2_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time,
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True
        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV2_G_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 1:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV2_V_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.future_earlier_time,
            later_time = self.player.future_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.future_earlier_time,
            later_time = self.player.future_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 11:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV_12(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_check_slider_one', 'future_slider_two', 'future_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.future_earlier_max,
            later_max=self.player.future_later_max,
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time,
            t_earliest=self.player.future_t_earliest,
            t_middle=self.player.future_t_middle,
            t_latest=self.player.future_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.future_t_earliest == self.player.future_earlier_time and self.player.future_t_middle == self.player.future_later_time:
            check_future_slider_locations = True
        
        return (
            check_condition and check_future_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.future_slider_one = self.player.future_earlier_max - self.player.future_slider_one
        return super().before_next_page()


class FV_13(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_check_slider_one', 'future_slider_two', 'future_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.future_earlier_max,
            later_max=self.player.future_later_max,
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time,
            t_earliest=self.player.future_t_earliest,
            t_middle=self.player.future_t_middle,
            t_latest=self.player.future_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.future_t_earliest == self.player.future_earlier_time and self.player.future_t_latest == self.player.future_later_time:
            check_future_slider_locations = True
        
        return (
            check_condition and check_future_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.future_slider_one = self.player.future_earlier_max - self.player.future_slider_one
        return super().before_next_page()


class FV_23(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_check_slider_one', 'future_slider_two', 'future_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.future_earlier_max,
            later_max=self.player.future_later_max,
            earlier_time=self.player.future_earlier_time,
            later_time=self.player.future_later_time,
            t_earliest=self.player.future_t_earliest,
            t_middle=self.player.future_t_middle,
            t_latest=self.player.future_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.future_t_middle == self.player.future_earlier_time and self.player.future_t_latest == self.player.future_later_time:
            check_future_slider_locations = True
        
        return (
            check_condition and check_future_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.future_slider_one = self.player.future_earlier_max - self.player.future_slider_one
        return super().before_next_page()


################################################################################################### PAST PAGES BELOW ##############################################################################################################
class PG1_1_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block,
        )
    
    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG1_2_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG2_G_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False

        if self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG2_V_Instructions(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False

        if self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG_BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = "player"
    form_fields = ["past_question_answers"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        # This page will only be displayed when there are blocks left
        return (
            check_condition and self.player.get_current_past_block() and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        step = self.player.get_current_past_block_step() + 1
        block_index = self.player.get_current_past_block_index() + 1
        current_block = self.player.get_current_past_block()

        questions_to_page = (len(current_block.left_values) * (step - 1)) + 1

        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if block_index == 1 or block_index == 6 or block_index == 11:
            note = ""


        return {
            "step": step,
            "block_index": block_index,
            "questions_to_page": questions_to_page,
            "num_blocks": self.session.config["past_num_blocks"],
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": "Jobs created",
            "note": note
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_past_block_step()


class PG2_Divider(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG3_Divider(Page):
    def vars_for_template(self):
        current_block = self.player.get_current_past_block()
        return dict(
            curr_block=current_block
        )
    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grid_rounds:
                check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grid_rounds and self.round_number < 2 * Constants.num_grid_rounds + 1:
                    check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
        return (
            check_condition and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV1_2_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time,
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV2_V_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV2_G_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False

        if self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 1:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.past_earlier_time,
            later_time = self.player.past_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.past_earlier_time,
            later_time = self.player.past_later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grid_rounds + 11:
                    check_round_number = True
        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV_12(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_check_slider_one', 'past_slider_two', 'past_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.past_earlier_max,
            later_max=self.player.past_later_max,
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time,
            t_earliest=self.player.past_t_earliest,
            t_middle=self.player.past_t_middle,
            t_latest=self.player.past_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True

        check_past_slider_locations = False
        if self.player.past_t_earliest == self.player.past_earlier_time and self.player.past_t_middle == self.player.past_later_time:
            check_past_slider_locations = True
        
        return (
            check_condition and check_past_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.past_slider_one = self.player.past_earlier_max - self.player.past_slider_one
        return super().before_next_page()


class PV_13(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_check_slider_one', 'past_slider_two', 'past_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.past_earlier_max,
            later_max=self.player.past_later_max,
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time,
            t_earliest=self.player.past_t_earliest,
            t_middle=self.player.past_t_middle,
            t_latest=self.player.past_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True

        check_past_slider_locations = False
        if self.player.past_t_earliest == self.player.past_earlier_time and self.player.past_t_latest == self.player.past_later_time:
            check_past_slider_locations = True
        
        return (
            check_condition and check_past_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.past_slider_one = self.player.past_earlier_max - self.player.past_slider_one
        return super().before_next_page()


class PV_23(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_check_slider_one', 'past_slider_two', 'past_check_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grid_rounds + 1 or self.round_number == Constants.num_grid_rounds + 6 or self.round_number == Constants.num_grid_rounds + 11:
                    note = ""

        return dict(
            earlier_max=self.player.past_earlier_max,
            later_max=self.player.past_later_max,
            earlier_time=self.player.past_earlier_time,
            later_time=self.player.past_later_time,
            t_earliest=self.player.past_t_earliest,
            t_middle=self.player.past_t_middle,
            t_latest=self.player.past_t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grid_rounds and self.round_number < Constants.num_grid_rounds + Constants.num_sliders + 1:
                    check_condition = True


        check_past_slider_locations = False
        if self.player.past_t_middle == self.player.past_earlier_time and self.player.past_t_latest == self.player.past_later_time:
            check_past_slider_locations = True
        
        return (
            check_condition and check_past_slider_locations and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )
    
    def before_next_page(self):
        self.player.past_slider_one = self.player.past_earlier_max - self.player.past_slider_one
        return super().before_next_page()


class Check1(Page):
    form_model = "player"
    form_fields = ["check_1"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grid_rounds:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
                return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )



class Check2(Page):
    form_model = "player"
    form_fields = ["check_2"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == Constants.num_sliders + Constants.num_grid_rounds:
                    check_condition = True
            else:
                if self.round_number == 2 * Constants.num_sliders:
                    check_condition = True

        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == 2 * Constants.num_grid_rounds:
                    check_condition = True
            else:
                if self.round_number == Constants.num_sliders + Constants.num_grid_rounds:
                    check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
                return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )


class Dice(Page):
    form_model = "player"
    form_fields = ["dice_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grid_rounds:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
                return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )



class Disease(Page):
    form_model = "player"
    form_fields = ["disease_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grid_rounds:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
                return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )


class Lottery(Page):
    form_model = "player"
    form_fields = ["lottery_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grid_rounds:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        return

def generate_page_sequence():
    return (
        [FG1_1_Instructions]
        + [FG1_2_Instructions]
        + [FG2_V_Instructions]
        + [FG2_G_Instructions]
        + [FG_BlockPage] * Constants.num_per_section
        + [FG2_Divider]
        + [FG_BlockPage] * Constants.num_per_section
        + [FG3_Divider]
        + [FG_BlockPage] * Constants.num_per_section
        + [FV1_1_Instructions]
        + [FV1_2_Instructions]
        + [FV2_V_Instructions]
        + [FV2_G_Instructions]
        + [FV2_Divider]
        + [FV3_Divider]
        + [FV_12]
        + [FV_13]
        + [FV_23]
        + [PG1_1_Instructions]
        + [PG1_2_Instructions]
        + [PG2_V_Instructions]
        + [PG2_G_Instructions]
        + [PG_BlockPage] * Constants.num_per_section
        + [PG2_Divider]
        + [PG_BlockPage] * Constants.num_per_section
        + [PG3_Divider]
        + [PG_BlockPage] * Constants.num_per_section
        + [PV1_1_Instructions]
        + [PV1_2_Instructions]
        + [PV2_V_Instructions]
        + [PV2_G_Instructions]
        + [PV2_Divider]
        + [PV3_Divider]
        + [PV_12]
        + [PV_13]
        + [PV_23]
        + [Check1]
        + [Dice]
        + [Lottery]
        + [Disease]
        + [Check2]
    )

page_sequence = generate_page_sequence()