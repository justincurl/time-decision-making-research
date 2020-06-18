import random
from ._builtin import Page, WaitPage
from .config import BLOCKS, PLOTS

class Start(Page):
    pass

class HLPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = 'player'
    form_fields = ['question_answers']

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return self.player.hl_second and self.player.get_current_plot() 

    def vars_for_template(self):
        step = self.player.current_plot_step + 1
        current_plot = self.player.get_current_plot()
        num_plots = len(PLOTS)

        return {
            'step': step,
            'num_plots': num_plots,
            'progress': round(step * 100 / num_plots),
            'plot': current_plot
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_plot_step()

class BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = 'player'
    form_fields = ['question_answers']

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return not self.player.hl_second and self.player.get_current_block()

    def vars_for_template(self):
        step = self.player.get_current_block_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()
        num_blocks = len(BLOCKS)
        
        title = "Personal Income Growth"
        question_instructions = "Personal Income Growth"

        return {
            'step': step,
            'block_index': block_index,
            'num_blocks': num_blocks,
            'progress': round(step * 100 / num_blocks),
            'curr_block': current_block,
            'num_choices': current_block.number_of_choices,
            'title': title,
            'question_instructions': question_instructions
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_block_step()


class Results(Page):
    def is_displayed(self):
        return self.round_number == 2

class NextSection(Page):
    def before_next_page(self):
        self.player.hl_second = not self.player.hl_second
    def is_displayed(self):
        return self.round_number == 1

class InstructionsCTB(Page):
    def vars_for_template(self):
        title = "Personal Income Growth Selection between Two Years"
        if self.round_number == 1:
            instructions_pt1 = """
                On the following pages, you will see measurements of how much better off people are in two years of a hypothetical 
                U.S. president's term. The measurements shown are percent change in 
            """
            instructions_bold = "personal income growth"
            instructions_pt2 = ", which provides a good measure of the strength of the national economy."
            instructions_pt3 = """
                After looking at the values for income growth in the two years, choose the combination of growth rates that you rate as the strongest economy.
                As you can see, there is a trade-off: As the growth rate goes down for one year, it goes up for the other.
            """
        else:
            instructions_pt1 = """
                On the following pages, you will see measurements of how much better off people are in two years of a hypothetical 
                U.S. president's term. The measurements shown are again percent change in 
            """
            instructions_bold = "personal income growth"
            instructions_pt2 = ""
            instructions_pt3 = """
                After looking at the values for income growth in the two years, choose the combination of growth rates that you rate as the strongest economy.
                As you can see, there is a trade-off: As the growth rate goes down for one year, it goes up for the other.
            """

        return {
            'instructions_pt1': instructions_pt1, 
            'instructions_bold': instructions_bold, 
            'instructions_pt2': instructions_pt2,
            'instructions_pt3': instructions_pt3,
            'title': title,
            'round_number' : self.round_number
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return not self.player.hl_second

class InstructionsHL(Page):
    def vars_for_template(self):
        title = "Personal Income Growth Evaluation of Plots"
        if self.round_number == 1:
            instructions_pt1 = """
                On the following pages, you will see figures with measurements of how much better off people are during hypothetical 
                U.S. presidents' terms. The measurements shown are percent change in 
            """
            instructions_bold = "personal income growth"
            instructions_pt2 = ", which provides a good measure of the strength of the national economy."
            instructions_pt3 = """
                After looking at a figure, evaluate the economy during this period. Would you say it is very bad, fairly bad, fairly good, or very good?
            """
        else:
            instructions_pt1 = """
                On the following pages, you will see figures with measurements of how much better off people are during hypothetical U.S. presidents' terms. 
                The measurements shown are again percent change in 
            """
            instructions_bold = "personal income growth"
            instructions_pt2 = ""
            instructions_pt3 = """
                After looking at a figure, evaluate the economy during this period. Would you say it is very bad, fairly bad, fairly good, or very good?
            """
        return {
            'instructions_pt1': instructions_pt1, 
            'instructions_bold': instructions_bold, 
            'instructions_pt2': instructions_pt2,
            'instructions_pt3': instructions_pt3,
            'title': title,
            'round_number' : self.round_number
        }
    def error_message(self, values):
        pass

    def is_displayed(self):
        return self.player.hl_second


def generate_page_sequence():
    return [InstructionsHL] + [InstructionsCTB] + [HLPage] * len(PLOTS) + [BlockPage] * len(BLOCKS) + [NextSection] + [Results]


page_sequence = generate_page_sequence()
