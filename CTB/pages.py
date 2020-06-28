import random
import json
import datetime
from ._builtin import Page, WaitPage
from .config import BLOCKS, PLOTS

PROGRESS_DENOM = len(PLOTS) + len(BLOCKS) + 1


class Start(Page):
    pass


class HLPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.
    form_model = "player"
    form_fields = ["question_answers"]

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return (
            self.player.hl_second
            and self.player.get_current_plot()
            and (json.loads(self.player.consent_answer) == 1)
        )

    def vars_for_template(self):
        step = self.player.current_plot_step + 1
        current_plot = self.player.get_current_plot()
        num_plots = len(PLOTS)
        if self.player.round_number == 2:
            progress_num = (step + 7) * 100
        else:
            progress_num = (step) * 100
        progress = round(progress_num / PROGRESS_DENOM)

        return {
            "step": step,
            "num_plots": num_plots,
            "progress": progress,
            "plot": current_plot,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_plot_step()


class BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = "player"
    form_fields = ["question_answers"]

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return (
            not self.player.hl_second
            and self.player.get_current_block()
            and (json.loads(self.player.consent_answer) == 1)
        )

    def vars_for_template(self):
        step = self.player.get_current_block_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()
        num_blocks = len(BLOCKS)

        if self.player.round_number == 2:
            progress_num = (step + 25) * 100
        else:
            progress_num = (step) * 100
        progress = round(progress_num / PROGRESS_DENOM)

        questions_to_page = (len(current_block.left_values) * (step - 1)) + 1

        question_instructions = "Personal Income Growth"

        return {
            "step": step,
            "block_index": block_index,
            "questions_to_page": questions_to_page,
            "num_blocks": num_blocks,
            "progress": progress,
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": question_instructions,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_block_step()


class Results(Page):
    def __datetime(date_str):
        return datetime.strptime(date_str, "%H:%M:%S")

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(
            json.loads(self.player.start_time), "%H:%M:%S"
        )
        self.player.total_time = json.dumps(str(finish_time - start_time))

        return self.round_number == 2 and (json.loads(self.player.consent_answer) == 1)


class NonConsent(Page):
    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 0


class Consent(Page):
    form_model = "player"
    form_fields = ["consent_answer"]

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

        return self.round_number == 1


class Attention(Page):
    form_model = "player"
    form_fields = ["attention_check"]

    def before_next_page(self):
        self.player.hl_second = not self.player.hl_second

    def is_displayed(self):
        return self.round_number == 1 and (json.loads(self.player.consent_answer) == 1)

    def vars_for_template(self):
        if not self.player.hl_second:
            progress = 6 / PROGRESS_DENOM * 100
        else:
            progress = 24 / PROGRESS_DENOM * 100
        values = [
            "France",
            "Germany",
            "Switzerland",
            "Mauritania",
            "Syria",
            "Iran",
            "Canada",
            "Mexico",
            "None of the Above",
        ]
        return {
            "values": values,
            "choices": range(1, len(values) + 1),
            "progress": progress,
        }


class InstructionsCTB(Page):
    def vars_for_template(self):
        title = "Choose the Best Economy under Hypothetical, Second-Term Presidents"
        if self.round_number == 1:
            instructions_pt1 = """
                On each of the following 6 pages, you will see measurements of how much better off people are in two years of a hypothetical 
                U.S. president's four-year term. The measurements shown are percent change in personal income growth, which provides a 
                good measure of the strength of the national economy."""
            instructions_pt2 = """
                After looking at the values for income growth in the two years, choose the combination of growth rates that you rate as the strongest economy.
                As you can see, there is a trade-off: As the growth rate goes down for one year, it goes up for the other.
            """
        else:
            instructions_pt1 = """
                On each of the following 6 pages, you will see measurements of how much better off people are in two years of a hypothetical 
                U.S. president's four-year term. The measurements shown are again percent change in personal income growth
            """
            instructions_pt2 = """
                After looking at the values for income growth in the two years, choose the combination of growth rates that you rate as the strongest economy.
                As you can see, there is a trade-off: As the growth rate goes down for one year, it goes up for the other.
            """

        return {
            "instructions_pt1": instructions_pt1,
            "instructions_pt2": instructions_pt2,
            "title": title,
            "round_number": self.round_number,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return not self.player.hl_second and (
            (json.loads(self.player.consent_answer) == 1)
        )


class InstructionsHL(Page):
    def vars_for_template(self):
        title = "Evaluate the Economy under Hypothetical, Second-Term Presidents"
        if self.round_number == 1:
            instructions_pt1 = """
                On each of the following 24 pages, you will see a figure with measurements of how much better off people are during a hypothetical 
                U.S. president's four-year term. The measurements shown are percent change in personal income growth, which provides a 
                good measure of the strength of the national economy."""
            instructions_pt2 = """
                After looking at a figure, evaluate the economy during this period. Would you say it is very bad, fairly bad, 
                fairly good, or very good?
            """
        else:
            instructions_pt1 = """
                On each of the following 24 pages, you will see a figure with measurements of how much better off people are during a hypothetical 
                U.S. president's four-year term. The measurements shown are again percent change in personal income growth
                """
            instructions_pt2 = """
                After looking at a figure, evaluate the economy during this period. Would you say it is very bad, fairly bad, 
                fairly good, or very good?"""
        return {
            "instructions_pt1": instructions_pt1,
            "instructions_pt2": instructions_pt2,
            "title": title,
            "round_number": self.round_number,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        if self.player.round_number == 2:
            self.player.consent_answer = self.player.in_round(
                self.round_number - 1
            ).consent_answer
        return self.player.hl_second and (json.loads(self.player.consent_answer) == 1)


def generate_page_sequence():
    return (
        [Consent]
        + [InstructionsHL]
        + [InstructionsCTB]
        + [HLPage] * len(PLOTS)
        + [BlockPage] * len(BLOCKS)
        + [Attention]
        + [Results]
        + [NonConsent]
    )


page_sequence = generate_page_sequence()
