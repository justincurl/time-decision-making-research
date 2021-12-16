from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


# **********************************************************************************************************************
# *** BOT
# **********************************************************************************************************************
class PlayerBot(Bot):

    def play_round(self):
        # define page as round_number
        page = self.subsession.round_number
        
        if self.round_number == 1:
                yield pages.Instructions
                        
        if self.player.direct_condition == 1:
                if self.round_number == 1:
                        yield pages.DirectGrowthBefore, dict(slider_direct_growth="1", direct_growth=1)


        if self.player.plot_condition == 1:
                if self.round_number <= Constants.num_choices:
                        yield (pages.DecisionPast, {'past_choice': random.choice(['A', 'B'])})
                if self.round_number == Constants.num_choices:
                        yield pages.Check1, dict(check_1="1")
                if self.round_number > Constants.num_choices:
                        yield (pages.DecisionFuture, {'future_choice': random.choice(['A', 'B'])})
                if self.round_number == 2*Constants.num_choices:
                        yield pages.Check2, dict(check_2="1")
        else:
                if self.round_number <= Constants.num_choices:
                        yield (pages.DecisionFuture, {'future_choice': random.choice(['A', 'B'])})        
                if self.round_number == Constants.num_choices:
                        yield pages.Check1, dict(check_1="1")
                if self.round_number > Constants.num_choices:
                        yield (pages.DecisionPast, {'past_choice': random.choice(['A', 'B'])})
                if self.round_number == 2*Constants.num_choices:
                        yield pages.Check2, dict(check_2="1")
                                
        if self.player.direct_condition == 2:
                if self.round_number == Constants.num_rounds:
                        yield pages.DirectGrowthAfter, dict(slider_direct_growth="1", direct_growth=1)                                