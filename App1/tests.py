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
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                if self.round_number == 1:
                    yield pages.FG1_1_Instructions
                    yield pages.FG1_2_Instructions
                if self.round_number == 6:
                    yield pages.FG2_Divider
                elif self.round_number == 11:
                    yield pages.FG3_Divider
                yield (pages.FG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})

        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                if self.round_number == 1:
                    yield pages.FV1_1_Instructions
                    yield pages.FV1_2_Instructions
                if self.round_number == 6:
                    yield pages.FV2_Divider
                elif self.round_number == 11:
                    yield pages.FV3_Divider
                if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                    yield pages.FV_12, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                    yield pages.FV_13, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                    yield pages.FV_23, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)

        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                if self.round_number == 1:
                    yield pages.PG1_1_Instructions
                    yield pages.PG1_2_Instructions
                if self.round_number == 6:
                    yield pages.PG2_Divider
                elif self.round_number == 11:
                    yield pages.PG3_Divider
                yield (pages.PG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})

        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                if self.round_number == 1:
                    yield pages.PV1_1_Instructions
                    yield pages.PV1_2_Instructions
                if self.round_number == 6:
                    yield pages.PV2_Divider
                elif self.round_number == 11:
                    yield pages.PV3_Divider
                if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                    yield pages.PV_12, dict(past_slider_one=500000, past_slider_two=0)
                elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                    yield pages.PV_13, dict(past_slider_one=500000, past_slider_two=0)
                elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                    yield pages.PV_23, dict(past_slider_one=500000, past_slider_two=0)


        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                yield pages.Check1, dict(check_1=1)
                yield pages.Dice, dict(dice_answer=2)
                yield pages.Lottery, dict(lottery_answer=2)
                yield pages.Disease, dict(disease_answer=2)

        if self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grids:
                yield pages.Check1, dict(check_1=1)
                yield pages.Dice, dict(dice_answer=2)
                yield pages.Lottery, dict(lottery_answer=2)
                yield pages.Disease, dict(disease_answer=2)

        if self.player.second == "FG":
            if self.player.first == "PG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    if self.player.round_number == Constants.num_grids + 1:
                        yield pages.FG2_G_Instructions
                    if self.player.round_number == Constants.num_grids + 6:
                        yield pages.FG2_Divider
                    elif self.player.round_number == Constants.num_grids + 11:
                        yield pages.FG3_Divider
                    yield (pages.FG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})
            elif self.player.first == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_sliders + 1:
                        yield pages.FG2_1V_Instructions
                        yield pages.FG2_2V_Instructions
                    if self.player.round_number == Constants.num_sliders + 6:
                        yield pages.FG2_Divider
                    elif self.player.round_number == Constants.num_sliders + 11:
                        yield pages.FG3_Divider
                    yield (pages.FG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})

        if self.player.second == "FV":
            if self.player.first == "FG":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_grids + 1:
                        yield pages.FV2_1G_Instructions
                        yield pages.FV2_2G_Instructions
                    if self.player.round_number == Constants.num_grids + 6:
                        yield pages.FV2_Divider
                    elif self.player.round_number == Constants.num_grids + 11:
                        yield pages.FV3_Divider
                    if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                        yield pages.FV_12, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                    elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.FV_13, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                    elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.FV_23, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
            elif self.player.first == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_sliders + 1:
                        yield pages.FV2_V_Instructions
                    if self.player.round_number == Constants.num_sliders + 6:
                        yield pages.FV2_Divider
                    elif self.player.round_number == Constants.num_sliders + 11:
                        yield pages.FV3_Divider
                    if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                        yield pages.FV_12, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                    elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.FV_13, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)
                    elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.FV_23, dict(future_slider_one=500000, future_slider_two=0, slider_two_last_clicked=0)


        if self.player.second == "PG":
            if self.player.first == "FG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    if self.player.round_number == Constants.num_grids + 1:
                        yield pages.PG2_G_Instructions
                    if self.player.round_number == Constants.num_grids + 6:
                        yield pages.PG2_Divider
                    elif self.player.round_number == Constants.num_grids + 11:
                        yield pages.PG3_Divider
                    yield (pages.PG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})
            elif self.player.first == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_sliders + 1:
                        yield pages.PG2_1V_Instructions
                        yield pages.PG2_2V_Instructions
                    if self.player.round_number == Constants.num_sliders + 6:
                        yield pages.PG2_Divider
                    elif self.player.round_number == Constants.num_sliders + 11:
                        yield pages.PG3_Divider
                    yield (pages.PG_Main, {'grid_answer': random.choice(['1', '2', '3', '4', '5', '6'])})

        if self.player.second == "PV":
            if self.player.first == "PG":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_grids + 1:
                        yield pages.PV2_1G_Instructions
                        yield pages.PV2_2G_Instructions
                    if self.player.round_number == Constants.num_grids + 6:
                        yield pages.PV2_Divider
                    elif self.player.round_number == Constants.num_grids + 11:
                        yield pages.PV3_Divider
                    if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                        yield pages.PV_12, dict(past_slider_one=500000, past_slider_two=0)
                    elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.PV_13, dict(past_slider_one=500000, past_slider_two=0)
                    elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.PV_23, dict(past_slider_one=500000, past_slider_two=0)
            elif self.player.first == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    if self.player.round_number == Constants.num_sliders + 1:
                        yield pages.PV2_V_Instructions
                    if self.player.round_number == Constants.num_sliders + 6:
                        yield pages.PV2_Divider
                    elif self.player.round_number == Constants.num_sliders + 11:
                        yield pages.PV3_Divider
                    if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
                        yield pages.PV_12, dict(past_slider_one=500000, past_slider_two=0)
                    elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.PV_13, dict(past_slider_one=500000, past_slider_two=0)
                    elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
                        yield pages.PV_23, dict(past_slider_one=500000, past_slider_two=0)

        if self.player.first == "PV" or self.player.first == "FV":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == Constants.num_sliders + Constants.num_grids:
                    yield pages.Check2, dict(check_2=1)
            else:
                if self.round_number == 2 * Constants.num_sliders:
                    yield pages.Check2, dict(check_2=1)

        if self.player.first == "PG" or self.player.first == "FG":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == 2 * Constants.num_grids:
                    yield pages.Check2, dict(check_2=1)
            else:
                if self.round_number == Constants.num_sliders + Constants.num_grids:
                    yield pages.Check2, dict(check_2=1)