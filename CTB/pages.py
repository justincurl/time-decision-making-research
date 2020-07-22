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
            progress_num = (step + 10) * 100
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


class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]

    def is_displayed(self):
        return self.round_number == 2 and (json.loads(self.player.consent_answer) == 1)


class Results(Page):
    def __datetime(self, date_str):
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
        title = "Choose the Strongest Economy"
        i_pt1 = """
            On the following 6 pages, you will see figures with measurements of how much better off people are in two different years of a hypothetical U.S. president’s term. The figures only show the economy for """
        i_pt2 = """
            presidents in their second terms. 
        """
        i_pt4 = """
            After looking at the values for income growth in two different years, choose the combination of growth that you evaluate as the strongest economy overall. As you can see, there is a trade-off: As growth goes down for one year, it goes up for the other. 
        """
        i_pt5 = """
            For example, the figure below asks you to pick a combination of growth in the second year of the president’s term and growth in the final year of the president’s term. The leftmost response button combines 2 percent growth in the final year of the president’s term and 0 percent growth in the second year. The rightmost button combines 0 percent growth in the final year and 2.5 percent growth in the second year of the president’s term. 
        """
        i_pt6 = """
            You can select any combination of growth. If you thought that 1 percent growth in the second year and 1.2 percent in the final year of the term are the strongest economy overall, you would mark the third button from the left, as in the example. 
        """
        instructions_image_link = "none"
        i_pt7 = """
            To start the task, click “next”. 
        """
        if self.round_number == 1:
            i_pt3 = """
               The measurements shown are personal income growth: the percentage by which the average person’s income increased in a given year. This provides a good measure of the strength of the national economy.             
            """
        else:
            i_pt3 = """
                The measurements shown are again personal income growth: the percentage by which the average person’s income increased in a given year. 
            """
        return {
            "i_pt1": i_pt1,
            "i_pt2": i_pt2,
            "i_pt3": i_pt3,
            "i_pt4": i_pt4,
            "i_pt5": i_pt5,
            "i_pt6": i_pt6,
            "i_pt7": i_pt7,
            "instructions_image_link": instructions_image_link,
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
        i_pt1 = """
            On the following 9 pages, you will see figures with measurements of how much better off people are during hypothetical U.S. presidents’ terms. The figures only show the economy for 
        """
        i_pt2 = """
            presidents in their second terms. 
        """
        i_pt4 = """
            For example, the figure below shows that incomes grew by 1.9 percent in the first year of the president’s term, by 2.1 percent in the second year, by 2.5 percent in the third year, and by 2.0 percent in the final year of the president’s term. 
        """
        i_pt5 = """
            After looking at a figure, evaluate the economy during this period. Would you say it is very good, fairly good, fairly bad, or very bad? 
        """
        i_pt6 = """
            To start the task, click “next”. 
        """
        instructions_image_link = "none"

        if self.round_number == 1:
            i_pt3 = """
                The measurements shown are personal income growth, the percentage by which the average person’s income increased in a given year. This provides a good measure of the strength of the national economy. 
            """
        else:
            i_pt3 = """
                The measurements shown are again personal income growth: the percentage by which the average person’s income increased in a given year. 
            """
        return {
            "i_pt1": i_pt1,
            "i_pt2": i_pt2,
            "i_pt3": i_pt3,
            "i_pt4": i_pt4,
            "i_pt5": i_pt5,
            "i_pt6": i_pt6,
            "instructions_image_link": instructions_image_link,
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


class Consent(Page):
    form_model = "player"
    form_fields = ["consent_answer"]

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)

        return self.round_number == 1


class PhoneDevice(Page):
    def is_displayed(self):
        return self.player.round_number == 1 and self.player.device_type == 3


class DeviceType(Page):
    form_model = "player"
    form_fields = ["device_type"]

    def is_displayed(self):
        return self.player.round_number == 1


def generate_page_sequence():
    return (
        [Consent]
        + [DeviceType]
        + [PhoneDevice]
        + [InstructionsHL]
        + [InstructionsCTB]
        + [HLPage] * len(PLOTS)
        + [BlockPage] * len(BLOCKS)
        + [Attention]
        + [Feedback]
        + [Results]
        + [NonConsent]
    )


page_sequence = generate_page_sequence()
