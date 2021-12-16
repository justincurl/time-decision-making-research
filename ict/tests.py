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
        # ------------------------------------------------------------------------------------------------------------ #
        # make decisions
        # ------------------------------------------------------------------------------------------------------------ #
        if self.player.staircase_condition == 2:
                yield (pages.FutureDecision, {'choice': random.choice(['A', 'B'])})
        if self.player.staircase_condition == 1:
                yield (pages.PastDecision, {'choice': random.choice(['A', 'B'])})