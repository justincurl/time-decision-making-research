import random
import json
from .models import Constants
import datetime
from ._builtin import Page, WaitPage
from otree.api import safe_json


class Start(Page):
    pass

class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]

    def is_displayed(self):
        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )


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

        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )


class NonConsent(Page):
    def is_displayed(self):
        return json.loads(self.participant.vars["consent_answer"]) == 0


class Consent(Page):
    form_model = "player"
    form_fields = ["consent_answer"]

    def is_displayed(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.player.start_time = json.dumps(current_time)
        return self.player.round_number == 1

    def before_next_page(self):
        self.participant.vars["consent_answer"] = self.player.consent_answer
        return super().before_next_page()


class PhoneDevice(Page):
    def is_displayed(self):
        
        return self.player.round_number == 1 and self.player.round_number == 1 and self.player.device_type == 3


class DeviceType(Page):
    form_model = "player"
    form_fields = ["device_type"]

    def is_displayed(self):
        return self.player.round_number == 1


class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

    def is_displayed(self):
        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        ) 

    def vars_for_template(self):
        return {
            "progress": 1
        }


class Education(Page):
    form_model = "player"
    form_fields = ["education"]

    def is_displayed(self):
        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        return {
            "progress": 1
        }


class GenderAge(Page):
    form_model = "player"
    form_fields = ["gender", "age"]

    def is_displayed(self):
        
        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def vars_for_template(self):
        return {
            "progress": 1
        }


class EthnicityRace(Page):
    form_model = "player"
    form_fields = ["ethnicity", "race"]

    def is_displayed(self):

        return (
            (self.player.round_number == Constants.num_rounds) and 
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

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
            "progress": 1,
        }

class SliderSimple(Page):
    form_model = 'player'
    form_fields = ['slider_one', 'check_slider_one', 'slider_two', 'check_slider_two']

    def vars_for_template(self):
        return dict(
            earlier_max=self.player.earlier_max,
            later_max=self.player.later_max,
            earlier_time=self.player.earlier_time,
            later_time=self.player.later_time
        )

    def is_displayed(self):
        return (
            (self.player.round_number != Constants.num_rounds) and 
            (self.player.round_number != 1) and
            (json.loads(self.participant.vars["consent_answer"]) == 1)
        )

    def error_message(self, value):
        if value["slider_one"] == None or value['slider_two'] == None:
            return 'Please use the slider to make a decision.'
    
    def before_next_page(self):
        self.player.slider_one = self.player.earlier_max - self.player.slider_one
        return super().before_next_page()


def generate_page_sequence():
    return (
        [DeviceType]
        + [PhoneDevice]
        + [Consent]
        + [SliderSimple]
        + [GenderAge]
        + [Education]
        + [EthnicityRace]
        + [ZipCode]
        + [Results]
        + [NonConsent]
    )


page_sequence = generate_page_sequence()