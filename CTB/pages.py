import random
from ._builtin import Page, WaitPage
from .config import BLOCKS, VISUALIZE_CHOICES_AS_SLIDER


instructions = """
On the following pages, you will see measurements of how much better off people are in two years of a hypothetical U.S. presidents' term. 
The measurements shown are percent change in PERSONAL INCOME GROWTH, which provides a good measure of the strength of the national economy. 

For each pair of years, you will see different combinations of income growth. As you can see, there is a trade-off: as one growth rate goes down,
the other growth rate goes up. Mark the combination of growth rates that you evaluate as the strongest economy.

"""

class Start(Page):
    pass

class BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = 'player'
    form_fields = ['question_answers']

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        return self.player.get_current_block()

    def vars_for_template(self):
        step = self.player.get_current_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()
        num_blocks = len(BLOCKS)

        title = "Economic Growth"
        question_instructions = "Economic Growth"

        return {
            'step': step,
            'block_index': block_index,
            'num_blocks': num_blocks,
            'progress': round(step * 100 / num_blocks),
            'curr_block': current_block,
            'use_slider': VISUALIZE_CHOICES_AS_SLIDER,
            'num_choices': current_block.number_of_choices,
            'instructions': instructions,
            'title': title,
            'question_instructions': question_instructions
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_step()


class Results(Page):
    pass

class Instructions(Page):
    def vars_for_template(self):  
        title = "Economic Growth"
        return {'instructions': instructions, 'title': title}

    def error_message(self, values):
        pass


def generate_page_sequence():
    return [Instructions] + [BlockPage] * len(BLOCKS) + [Results]

page_sequence = generate_page_sequence()
