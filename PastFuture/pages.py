import random
import json
import datetime
from ._builtin import Page, WaitPage
from .config import BLOCKS1, BLOCKS2, PLOTS1, PLOTS2


class Start(Page):
    pass


class HLPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.
    form_model = "player"
    form_fields = ["question1_answers", "question2_answers"]

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        if self.player.set_1:
            return (
                self.player.first[:2] == "HL"
                and self.player.get_current_plot()
                and (json.loads(self.player.consent_answer) == 1)
            )
        else:
            return (
                self.player.second[:2] == "HL"
                and self.player.get_current_plot()
                and (json.loads(self.player.consent_answer) == 1)
            )

    def vars_for_template(self):
        step1 = self.player.current_plot_step + 1
        plot1 = self.player.get_current_plot()
        step2 = self.player.current_plot_step + 2
        plot2 = self.player.get_next_plot()

        page = step2 // 2
        instructions1 = "How would you rate the condition of the "
        instructions3 = (
            " during this period? Very bad, fairly bad, fairly good, or very good?"
        )
        if self.player.set_1:
            progress_num = page * 100
            if self.player.first[2:] == "Past":
                instructions2 = "past national economy"
            else:
                instructions2 = "proposed national economy"
        else:
            if self.player.first[:2] == "HL":
                progress_num = (page + (len(PLOTS1) // 2) + 7) * 100
            else:
                progress_num = (page + len(BLOCKS1) + 7) * 100

            if self.player.second[2:] == "Past":
                instructions2 = "past national economy"
            else:
                instructions2 = "proposed national economy"

        progress = round(progress_num / self.player.denominator)

        return {
            "step1": step1,
            "step2": step2,
            "progress": progress,
            "plot1": plot1,
            "plot2": plot2,
            "block_index": page,
            "instructions1": instructions1,
            "instructions2": instructions2,
            "instructions3": instructions3,
        }

    def error_message(self, values):
        pass

    def before_next_page(self):
        self.player.goto_next_plot_step()
        self.player.goto_next_plot_step()


class BlockPage(Page):
    # Displays a `Block` to the player
    # This page will automatically retrieve the current `Block` to be displayed
    # to the player from the player's current block.

    form_model = "player"
    form_fields = ["question1_answers", "question2_answers"]

    def is_displayed(self):
        # This page will only be displayed when there are blocks left
        if self.player.set_1:
            return (
                self.player.first[:3] == "CTB"
                and self.player.get_current_block()
                and (json.loads(self.player.consent_answer) == 1)
            )
        else:
            return (
                self.player.second[:3] == "CTB"
                and self.player.get_current_block()
                and (json.loads(self.player.consent_answer) == 1)
            )

    def vars_for_template(self):
        step = self.player.get_current_block_step() + 1
        block_index = self.player.get_current_block_index() + 1
        current_block = self.player.get_current_block()
        instructions1 = "For each pair of years, mark the combination of "
        instructions3 = "that you rate as the best national economy in this period."
        if self.player.set_1:
            progress_num = (step) * 100
            num_blocks = len(BLOCKS1)
            if self.player.first[3:] == "Past":
                instructions2 = "past growth rates "
            else:
                instructions2 = "proposed growth rates "
        else:
            num_blocks = len(BLOCKS2)
            if self.player.first[:2] == "HL":
                progress_num = (step + (len(PLOTS1) // 2) + 7) * 100
            else:
                progress_num = (step + len(BLOCKS1) + 7) * 100
            if self.player.second[3:] == "Past":
                instructions2 = "past growth rates "
            else:
                instructions2 = "proposed growth rates "

        progress = round(progress_num / self.player.denominator)

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
            "instructions1": instructions1,
            "instructions2": instructions2,
            "instructions3": instructions3,
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
        return json.loads(self.player.consent_answer) == 1


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

        return json.loads(self.player.consent_answer) == 1


class NonConsent(Page):
    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 0


class Attention(Page):
    form_model = "player"
    form_fields = ["attention_check"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        if self.player.first[:2] == "HL":
            progress_num = ((len(PLOTS1) // 2) + 3) * 100
        else:
            progress_num = (len(BLOCKS1) + 3) * 100
        progress = progress_num / self.player.denominator
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


class CTBFuture(Page):
    def vars_for_template(self):
        title = "Choose the Best Future Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            self.player.set_1
            and self.player.first == "CTBFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class CTBPast(Page):
    def vars_for_template(self):
        title = "Choose the Best Past Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            self.player.set_1
            and self.player.first == "CTBPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLFuture(Page):
    def vars_for_template(self):
        title = "Evaluate the Future Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            self.player.set_1
            and self.player.first == "HLFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLPast(Page):
    def vars_for_template(self):
        title = "Evaluate the Past Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            self.player.set_1
            and self.player.first == "HLPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLFuturePast(Page):
    def vars_for_template(self):
        title = "Evaluate the Future Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "HLFuture"
            and self.player.first == "HLPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLFutureCTB(Page):
    def vars_for_template(self):
        title = "Evaluate the Future Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "HLFuture"
            and self.player.first == "CTBFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLPastFuture(Page):
    def vars_for_template(self):
        title = "Evaluate the Past Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "HLPast"
            and self.player.first == "HLFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class HLPastCTB(Page):
    def vars_for_template(self):
        title = "Evaluate the Past Economy"
        instructions_image_link = "https://i.imgur.com/GD3wzM5.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "HLPast"
            and self.player.first == "CTBPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class CTBPastHL(Page):
    def vars_for_template(self):
        title = "Choose the Best Past Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "CTBPast"
            and self.player.first == "HLPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class CTBPastFuture(Page):
    def vars_for_template(self):
        title = "Choose the Best Past Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "CTBPast"
            and self.player.first == "CTBFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class CTBFuturePast(Page):
    def vars_for_template(self):
        title = "Choose the Best Future Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "CTBFuture"
            and self.player.first == "CTBPast"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class CTBFutureHL(Page):
    def vars_for_template(self):
        title = "Choose the Best Future Economy"
        instructions_image_link = "https://i.imgur.com/uEs8ViI.png"
        return {
            "instructions_image_link": instructions_image_link,
            "title": title,
        }

    def error_message(self, values):
        pass

    def is_displayed(self):
        return (
            not self.player.set_1
            and self.player.second == "CTBFuture"
            and self.player.first == "HLFuture"
            and ((json.loads(self.player.consent_answer) == 1))
        )


class Consent(Page):
    form_model = "player"
    form_fields = ["consent_answer"]

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)
        self.player.denominator = 15
        if self.player.first[:2] == "HL":
            self.player.denominator += len(PLOTS1) // 2
        else:
            self.player.denominator += len(BLOCKS1)

        if self.player.second[:2] == "HL":
            self.player.denominator += len(PLOTS2) // 2
        else:
            self.player.denominator += len(BLOCKS2)
        return 1


class PhoneDevice(Page):
    def is_displayed(self):
        return self.player.round_number == 1 and self.player.device_type == 3


class DeviceType(Page):
    form_model = "player"
    form_fields = ["device_type"]

    def is_displayed(self):
        return self.player.round_number == 1


class Dice(Page):
    form_model = "player"
    form_fields = ["dice_answer"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def vars_for_template(self):
        if self.player.first[:2] == "HL":
            progress_num = ((len(PLOTS1) // 2) + 2) * 100
        else:
            progress_num = (len(BLOCKS1) + 2) * 100

        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class Disease(Page):
    form_model = "player"
    form_fields = ["disease_answer"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def before_next_page(self):
        self.player.set_1 = False
        self.player.current_plot_step = 0
        self.player.current_block_step = 0

    def vars_for_template(self):
        if self.player.first[:2] == "HL":
            progress_num = ((len(PLOTS1) // 2) + 5) * 100
        else:
            progress_num = (len(BLOCKS1) + 5) * 100
        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class Lottery(Page):
    form_model = "player"
    form_fields = ["lottery_answer"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def vars_for_template(self):
        if self.player.first[:2] == "HL":
            progress_num = ((len(PLOTS1) // 2) + 3) * 100
        else:
            progress_num = (len(BLOCKS1) + 3) * 100

        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        return {
            "progress": (self.player.denominator - 1) / self.player.denominator * 100
        }


class Education(Page):
    form_model = "player"
    form_fields = ["education"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        return {
            "progress": (self.player.denominator - 3) / self.player.denominator * 100,
        }


class BenefitToday(Page):
    form_model = "player"
    form_fields = ["benefit_today"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def vars_for_template(self):
        progress_num = (self.player.denominator - 5) * 100
        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class TakeRisks(Page):
    form_model = "player"
    form_fields = ["take_risks"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def vars_for_template(self):
        progress_num = (self.player.denominator - 7) * 100
        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class Impulsive(Page):
    form_model = "player"
    form_fields = ["impulsive"]

    def is_displayed(self):
        return self.player.round_number == 1 and (
            json.loads(self.player.consent_answer) == 1
        )

    def vars_for_template(self):
        progress_num = (self.player.denominator - 6) * 100
        progress = progress_num / self.player.denominator
        return {
            "progress": progress,
        }


class Check1(Page):
    form_model = "player"
    form_fields = ["check_1"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        if self.player.first[:2] == "HL":
            progress_num = ((len(PLOTS1) // 2) + 1) * 100
        else:
            progress_num = (len(BLOCKS1) + 1) * 100

        progress = progress_num / self.player.denominator

        if self.player.first[:3] == "CTB":
            instructions = "On the previous pages, were you choosing growth rates for two years of past economic growth, or future economic growth? "
        else:
            instructions = "On the previous pages, were you rating the condition of past economic growth or future economic growth? "

        return {
            "instructions": instructions,
            "progress": progress,
        }


class Check2(Page):
    form_model = "player"
    form_fields = ["check_2"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        if self.player.second[:3] == "CTB":
            instructions = "On the previous pages, were you choosing growth rates for two years of past economic growth, or future economic growth? "
        else:
            instructions = "On the previous pages, were you rating the condition of past economic growth or future economic growth? "

        return {
            "instructions": instructions,
            "progress": (self.player.denominator - 8) / self.player.denominator * 100,
        }


class GenderAge(Page):
    form_model = "player"
    form_fields = ["gender", "age"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        return {
            "progress": (self.player.denominator - 4) / self.player.denominator * 100,
        }


class EthnicityRace(Page):
    form_model = "player"
    form_fields = ["ethnicity", "race"]

    def is_displayed(self):
        return json.loads(self.player.consent_answer) == 1

    def vars_for_template(self):
        values = [
            "White",
            "Black or African American",
            "Asian",
            "American Indian or Alaska Native",
            "Native Hawaiian or Pacific Islander",
            "Some other race",
        ]
        return {
            "values": values,
            "progress": (self.player.denominator - 2) / self.player.denominator * 100,
        }


def generate_page_sequence():
    return (
        [DeviceType]
        + [PhoneDevice]
        + [Consent]
        + [HLPast]
        + [HLFuture]
        + [CTBPast]
        + [CTBFuture]
        + [HLPage] * (len(PLOTS1) // 2)
        + [BlockPage] * len(BLOCKS1)
        + [Check1]
        + [Dice]
        + [Lottery]
        + [Disease]
        + [HLFuturePast]
        + [HLFutureCTB]
        + [HLPastFuture]
        + [HLPastCTB]
        + [CTBFutureHL]
        + [CTBFuturePast]
        + [CTBPastHL]
        + [CTBPastFuture]
        + [HLPage] * (len(PLOTS2) // 2)
        + [BlockPage] * len(BLOCKS2)
        + [Check2]
        + [TakeRisks]
        + [Impulsive]
        + [BenefitToday]
        + [GenderAge]
        + [Education]
        + [EthnicityRace]
        + [ZipCode]
        + [Results]
        + [NonConsent]
    )


page_sequence = generate_page_sequence()