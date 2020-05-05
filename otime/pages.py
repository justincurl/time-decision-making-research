import random
from ._builtin import Page, WaitPage
from .config import BLOCKS, VISUALIZE_CHOICES_AS_SLIDER

economic_instructions = """In this example, you are asked to choose your favorite combination of payment today and payment in future weeks. 
    As you can see, the sooner payment varies in value from $19 to $0 and the later payment varies in value from $0 to $20. 
    Note that there is a trade-off between the sooner payment and the later payment across the options. 
    As the sooner payment goes down, the later payment goes up. In this set of questions, we are not providing any actual payout to you. 
    However, we nevertheless ask you to carefully think about each decision that you make in the sur-vey, 
    and to think about how you would respond if money was at stake. Hence, please make your choices between options as if 
    the amounts would in fact be paid out to you at the sooner and later date stated in the questions.
"""
political_instructions = """In this example, you are asked to choose your favorite combination of economic growth this year and in future years. 
    As you can see, the sooner economic growth varies in value from 5% to 0% and the later payment varies in value from 0% to 5%. 
    Note that there is a trade-off between short term economic growth and long term economic growth across the options. 
    As the short term growth goes down, the long term growth goes up. However, we nevertheless ask you to carefully think about
    each decision that you make in the sur-vey, and to think about how you would respond if money was at stake. Hence, please 
    make your choices between options as if your payment would depend on your answers stated in the questions.

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

        if self.player.is_econ:
            instructions = economic_instructions
            title =  "Payment Preferences"
            question_instructions = "Payment"
        else:
            instructions = political_instructions
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

class Individual(Page):
    pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == 2

class Instructions(Page):
    def vars_for_template(self):  
        if self.player.is_econ:
            instructions = economic_instructions
            title =  "Payment Preferences"
        else:
            instructions = political_instructions
            title = "Economic Growth"
            
        return {'instructions': instructions, 'title': title}

    def error_message(self, values):
        pass

class Video(Page):
    def before_next_page(self):
        self.player.is_econ = not self.player.is_econ
    def is_displayed(self):
        return self.round_number == 1

class Policy(Page):
    pass

def generate_page_sequence():
    return [Instructions] + [BlockPage] * len(BLOCKS) + [Video] + [Results]

page_sequence = generate_page_sequence()
