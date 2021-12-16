import json
import datetime

from ._builtin import Page
from .models import Constants

class Start(Page):
    pass

######################################################################## FUTURE PAGES ########################################################################
class FG1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FG1_2_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FG_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )

    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_2_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_2_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_2_start_time), "%H:%M:%S")
        self.player.instructions_2_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FG2_G_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FG2_1V_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FG_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FG2_2V_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FG_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FG_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FG_Main(Page):
    form_model = "player"
    form_fields = ["grid_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
        if check_condition and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

    def vars_for_template(self):
        question_instructions = "Jobs created"
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FG":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""
        elif self.player.second == "FG":
            if self.player.first == "FV":
                if self.player.round_number - Constants.num_sliders == 1 or self.player.round_number - Constants.num_sliders == 6 or self.player.round_number - Constants.num_sliders == 11:
                    note = ""
            elif self.player.first == "PG":
                if self.player.round_number - Constants.num_grids == 1 or self.player.round_number - Constants.num_grids == 6 or self.player.round_number - Constants.num_grids == 11:
                    note = ""

        earlier_values = [self.player.earlier_max + x*(0-self.player.earlier_max)/(6-1) for x in range(6)]
        for i in range(len(earlier_values)):
            earlier_values[i] = "{:,.0f}".format(float(earlier_values[i]))

        later_values = [self.player.later_max + x*(0-self.player.later_max)/(6-1) for x in range(6)]
        for i in range(len(later_values)):
            later_values[i] = "{:,.0f}".format(float(later_values[i]))
        later_values.reverse()

        return dict(
            note=note,
            earlier_values=earlier_values,
            later_values=later_values,
            idxs=[i for i in range(6)],
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            question_instructions=question_instructions,
        )

class FG2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FG3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "FG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "FG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 11:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FV1_2_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FV_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True
        
        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_2_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_2_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_2_start_time), "%H:%M:%S")
        self.player.instructions_2_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FV2_1G_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FV_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FV2_2G_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/FV_01.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/FV_15.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FV2_V_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class FV2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 11:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class FV_12(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_slider_two', 'slider_two_last_clicked']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            check_future_slider_locations = True
        
        if check_condition and check_future_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        last_click = self.player.field_maybe_none('slider_two_last_clicked')
        if last_click:
            self.player.future_slider_two = self.player.later_max - self.player.future_slider_two
        return super().before_next_page()

class FV_13(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_slider_two', 'slider_two_last_clicked']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            check_future_slider_locations = True
        
        if check_condition and check_future_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        last_click = self.player.field_maybe_none('slider_two_last_clicked')
        if last_click:
            self.player.future_slider_two = self.player.later_max - self.player.future_slider_two
        return super().before_next_page()

class FV_23(Page):
    form_model = 'player'
    form_fields = ['future_slider_one', 'future_slider_two', 'slider_two_last_clicked']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "FV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "FV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "FV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "FV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True

        check_future_slider_locations = False
        if self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            check_future_slider_locations = True
        
        if check_condition and check_future_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        last_click = self.player.field_maybe_none('slider_two_last_clicked')
        if last_click:
            self.player.future_slider_two = self.player.later_max - self.player.future_slider_two
        return super().before_next_page()

################################################################################################### PAST PAGES BELOW ##############################################################################################################
class PG1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PG1_2_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PG_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_2_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_2_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_2_start_time), "%H:%M:%S")
        self.player.instructions_2_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PG2_G_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PG2_1V_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PG_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PG2_2V_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PG_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PG_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PG_Main(Page):
    form_model = "player"
    form_fields = ["grid_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                check_condition = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
        if check_condition and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

    def vars_for_template(self):
        question_instructions = "Jobs created"
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PG":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""
        elif self.player.second == "PG":
            if self.player.first == "PV":
                if self.player.round_number - Constants.num_sliders == 1 or self.player.round_number - Constants.num_sliders == 6 or self.player.round_number - Constants.num_sliders == 11:
                    note = ""
            elif self.player.first == "FG":
                if self.player.round_number - Constants.num_grids == 1 or self.player.round_number - Constants.num_grids == 6 or self.player.round_number - Constants.num_grids == 11:
                    note = ""


        earlier_values = [self.player.earlier_max + x*(0-self.player.earlier_max)/(6-1) for x in range(6)]
        for i in range(len(earlier_values)):
            earlier_values[i] = "{:,.0f}".format(float(earlier_values[i]))
        earlier_values.reverse()

        later_values = [self.player.later_max + x*(0-self.player.later_max)/(6-1) for x in range(6)]
        for i in range(len(later_values)):
            later_values[i] = "{:,.0f}".format(float(later_values[i]))

        return dict(
            note=note,
            earlier_values=earlier_values,
            later_values=later_values,
            idxs=[i for i in range(6)],
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            question_instructions=question_instructions,
        )

class PG2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PG3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PG":
            if self.round_number <= Constants.num_grids:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "FG":
            if self.player.second == "PG":
                if self.round_number > Constants.num_grids and self.round_number < 2 * Constants.num_grids + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "PV":
            if self.player.second == "PG":
                if self.round_number > Constants.num_sliders and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 11:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV1_1_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PV1_2_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PV_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 1:
                check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_2_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_2_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_2_start_time), "%H:%M:%S")
        self.player.instructions_2_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PV2_V_Instructions(Page):
    def vars_for_template(self):
        return dict(
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PV2_1G_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PV_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False

        if self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PV2_2G_Instructions(Page):
    def vars_for_template(self):
        image_link = ""
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            image_link = "App1/images-updated/PV_15.png"
        elif self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_05.png"
        elif self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            image_link = "App1/images-updated/PV_01.png"
        return dict(
            image_link=image_link,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )
    
    def is_displayed(self):
        check_condition = False
        check_round_number = False

        if self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 1:
                    check_round_number = True

        if check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.instructions_1_start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.instructions_1_finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.instructions_1_start_time), "%H:%M:%S")
        self.player.instructions_1_total_time = json.dumps(str(finish_time - start_time))
        return super().before_next_page()

class PV2_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 6:
                check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 6:
                    check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 6:
                    check_round_number = True

        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV3_Divider(Page):
    def vars_for_template(self):
        return dict(
            earlier_time = self.player.earlier_time,
            later_time = self.player.later_time
        )
    def is_displayed(self):
        check_condition = False
        check_round_number = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True
            if self.player.round_number == 11:
                check_round_number = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_sliders + 11:
                    check_round_number = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True
                if self.player.round_number == Constants.num_grids + 11:
                    check_round_number = True
        return (
            check_condition and check_round_number and json.loads(self.participant.vars["consent_answer"]) == 1
        )

class PV_12(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True

        check_past_slider_locations = False
        if self.player.t_earliest == self.player.earlier_time and self.player.t_middle == self.player.later_time:
            check_past_slider_locations = True
        
        if check_condition and check_past_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        self.player.past_slider_one = self.player.earlier_max - self.player.past_slider_one
        return super().before_next_page()

class PV_13(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True

        check_past_slider_locations = False
        if self.player.t_earliest == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            check_past_slider_locations = True
        
        if check_condition and check_past_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        self.player.past_slider_one = self.player.earlier_max - self.player.past_slider_one
        return super().before_next_page()

class PV_23(Page):
    form_model = 'player'
    form_fields = ['past_slider_one', 'past_slider_two']

    def vars_for_template(self):
        note = "Note that the total number of jobs that can be created over the two periods is different than in the last question."
        if self.player.first == "PV":
            if self.round_number == 1 or self.round_number == 6 or self.round_number == 11:
                note = ""

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number == Constants.num_sliders + 1 or self.round_number == Constants.num_sliders + 6 or self.round_number == Constants.num_sliders + 11:
                    note = ""

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number == Constants.num_grids + 1 or self.round_number == Constants.num_grids + 6 or self.round_number == Constants.num_grids + 11:
                    note = ""

        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time,
            t_earliest=self.player.t_earliest,
            t_middle=self.player.t_middle,
            t_latest=self.player.t_latest,
            note=note
        )

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV":
            if self.round_number <= Constants.num_sliders:
                check_condition = True

        elif self.player.first == "FV":
            if self.player.second == "PV":
                if self.round_number > Constants.num_sliders and self.round_number < 2 * Constants.num_sliders + 1:
                    check_condition = True

        elif self.player.first == "PG":
            if self.player.second == "PV":
                if self.round_number > Constants.num_grids and self.round_number < Constants.num_grids + Constants.num_sliders + 1:
                    check_condition = True


        check_past_slider_locations = False
        if self.player.t_middle == self.player.earlier_time and self.player.t_latest == self.player.later_time:
            check_past_slider_locations = True
        
        if check_condition and check_past_slider_locations and json.loads(self.participant.vars["consent_answer"]) == 1:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.player.start_time = json.dumps(current_time)
            return True
        else:
            return False

    def before_next_page(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.player.finish_time = json.dumps(current_time)
        finish_time = datetime.datetime.strptime(current_time, "%H:%M:%S")
        start_time = datetime.datetime.strptime(json.loads(self.player.start_time), "%H:%M:%S")
        self.player.total_time = json.dumps(str(finish_time - start_time))
        self.player.past_slider_one = self.player.earlier_max - self.player.past_slider_one
        return super().before_next_page()

class Check1(Page):
    form_model = "player"
    form_fields = ["check_1"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grids:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

class Check2(Page):
    form_model = "player"
    form_fields = ["check_2"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == Constants.num_sliders + Constants.num_grids:
                    check_condition = True
            else:
                if self.round_number == 2 * Constants.num_sliders:
                    check_condition = True

        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.player.second == "PG" or self.player.second == "FG":
                if self.round_number == 2 * Constants.num_grids:
                    check_condition = True
            else:
                if self.round_number == Constants.num_sliders + Constants.num_grids:
                    check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

class Dice(Page):
    form_model = "player"
    form_fields = ["dice_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grids:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

class Disease(Page):
    form_model = "player"
    form_fields = ["disease_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grids:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

class Lottery(Page):
    form_model = "player"
    form_fields = ["lottery_answer"]

    def is_displayed(self):
        check_condition = False
        if self.player.first == "PV" or self.player.first == "FV":
            if self.round_number == Constants.num_sliders:
                check_condition = True
        
        elif self.player.first == "PG" or self.player.first == "FG":
            if self.round_number == Constants.num_grids:
                check_condition = True
        
        return (
            check_condition and (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

def generate_page_sequence():
    return (
        [FG1_1_Instructions]
        + [FG1_2_Instructions]
        + [FG2_1V_Instructions]
        + [FG2_2V_Instructions]
        + [FG2_G_Instructions]
        + [FG2_Divider]
        + [FG3_Divider]
        + [FG_Main]
        + [FV1_1_Instructions]
        + [FV1_2_Instructions]
        + [FV2_V_Instructions]
        + [FV2_1G_Instructions]
        + [FV2_2G_Instructions]
        + [FV2_Divider]
        + [FV3_Divider]
        + [FV_12]
        + [FV_13]
        + [FV_23]
        + [PG1_1_Instructions]
        + [PG1_2_Instructions]
        + [PG2_1V_Instructions]
        + [PG2_2V_Instructions]
        + [PG2_G_Instructions]
        + [PG2_Divider]
        + [PG3_Divider]
        + [PG_Main]
        + [PV1_1_Instructions]
        + [PV1_2_Instructions]
        + [PV2_V_Instructions]
        + [PV2_1G_Instructions]
        + [PV2_2G_Instructions]
        + [PV2_Divider]
        + [PV3_Divider]
        + [PV_12]
        + [PV_13]
        + [PV_23]
        + [Check1]
        + [Dice]
        + [Lottery]
        + [Disease]
        + [Check2]
    )

page_sequence = generate_page_sequence()