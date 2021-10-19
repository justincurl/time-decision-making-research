import random
import json
import datetime
from ._builtin import Page

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

        question_instructions = "Personal Income Growth"

        return {
            "step": step,
            "block_index": block_index,
            "questions_to_page": questions_to_page,
            "num_blocks": self.session.config["num_blocks"],
            "curr_block": current_block,
            "num_choices": current_block.number_of_choices,
            "question_instructions": question_instructions,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_block_step()


class InstructionsCTB(Page):
    def vars_for_template(self):
        title = "Choose the Best Economy"
        i_pt1 = """
            On the following 6 pages, you will see figures with measurements of how much better off people are in two different years of a hypothetical U.S. president’s term. The figures only show the economy for """
        i_pt2 = """
            presidents in their second terms.
        """
        i_pt4 = """
            If you could choose how much income growth to have in two different years of a president’s term, what combination of growth rates would you consider the best? 
        """
        i_pt5 = """
            In the following questions, you’ll be asked to choose combinations of growth rates. As you will see, there is a trade-off: As growth goes down for one year, it goes up for the other. Each screen asks about a different pair of years. 
        """
        i_pt6 = """
            Here’s an example: 
        """
        instructions_image_link = "https://i.imgur.com/yan1jln.png"
        i_pt7 = """
            The example asks a respondent to pick a combination of growth in the final year of the president’s term and growth earlier, in the second year of the president’s term. There are six different options to choose from. For example, the leftmost response button combines 2 percent growth in the final year of the president’s term and 0 percent growth in the second year. The rightmost button combines 0 percent growth in the final year and 2.5 percent growth in the second year of the president’s term.  
        """
        i_pt8 = """
            In this example, the respondent thought that 1.2 percent in the final year and 1 percent growth in the second year of the term was the best economy overall, and therefore marked the third button from the left. 
        """
        i_pt9 = """
            To start the task, click “next”. 
        """
        i_pt3 = """
            The measurements shown are personal income growth: the percentage by which the average person’s income increased in a given year. This provides a good measure of the strength of the national economy. 
        """
        return {
            "i_pt1": i_pt1,
            "i_pt2": i_pt2,
            "i_pt3": i_pt3,
            "i_pt4": i_pt4,
            "i_pt5": i_pt5,
            "i_pt6": i_pt6,
            "i_pt7": i_pt7,
            "i_pt8": i_pt8,
            "i_pt9": i_pt9,
            "instructions_image_link": instructions_image_link,
            "title": title,
            "round_number": self.round_number,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return json.loads(self.participant.vars["consent_answer"]) == 1




def generate_page_sequence():
    return (
        [InstructionsCTB]
        + [BlockPage] * 3
    )


page_sequence = generate_page_sequence()
