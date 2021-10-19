from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

    def is_displayed(self):
        return (
            json.loads(self.participant.vars["consent_answer"]) == 1
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
            json.loads(self.participant.vars["consent_answer"]) == 1
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
            json.loads(self.participant.vars["consent_answer"]) == 1
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
            json.loads(self.participant.vars["consent_answer"]) == 1
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

class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]

    def is_displayed(self):
        return (
            json.loads(self.participant.vars["consent_answer"]) == 1
        )


class Results(Page):
    def __datetime(self, date_str):
        return datetime.strptime(date_str, "%H:%M:%S")

    def is_displayed(self):
        return (
            json.loads(self.participant.vars["consent_answer"]) == 1
        )


def generate_page_sequence():
    return ([GenderAge]
        + [Education]
        + [EthnicityRace]
        + [ZipCode]
        + [Results]
    )

page_sequence = generate_page_sequence()
