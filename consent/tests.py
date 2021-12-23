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
        yield (pages.DeviceType, {'device_type': random.choice(['1','2','3','4','5'])})
        if self.player.device_type == 3 or self.player.device_type == 4 or self.player.device_type == 5:
                yield pages.PhoneDevice
        yield (pages.Consent, {'consent_answer': random.choice(['1'])})