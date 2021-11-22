from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

    # def is_displayed(self):
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     ) 

    def vars_for_template(self):
        return {
            "progress": 1
        }


class Education(Page):
    form_model = "player"
    form_fields = ["education"]

    # def is_displayed(self):
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

    def vars_for_template(self):
        return {
            "progress": 1
        }


class GenderAge(Page):
    form_model = "player"
    form_fields = ["gender", "age"]

    # def is_displayed(self):
        
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

    def vars_for_template(self):
        return {
            "progress": 1
        }

class IncomeLevel(Page):
    form_model = "player"
    form_fields = ["income_level"]

    # def is_displayed(self):
        
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

    def vars_for_template(self):
        return {
            "progress": 1
        }

class PoliticalOrientation(Page):
    form_model = "player"
    form_fields = ["political_orientation", "independent_option", "republican_option", "democrat_option"]

    # def is_displayed(self):
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

    def vars_for_template(self):
        return {
            "progress": 1
        }

class BenefitToday(Page):
    form_model = "player"
    form_fields = ["benefit_today"]

    # def is_displayed(self):
    #     return self.player.round_number == 1 and (
    #         json.loads(self.player.consent_answer) == 1
    #     )

class EthnicityRace(Page):
    form_model = "player"
    form_fields = ["ethnicity", "race"]

    # def is_displayed(self):

    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

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

    # def is_displayed(self):
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )

class SelvesOverlap(Page):
    form_model = 'player'
    form_fields = ['slider_overlap', 'check_slider_overlap']
    
    def error_message(self, value):
        if value["check_slider_overlap"] == None:
            return 'Please use the slider to make a decision.'

class Results(Page):
    def __datetime(self, date_str):
        return datetime.strptime(date_str, "%H:%M:%S")

    # def is_displayed(self):
    #     return (
    #         json.loads(self.participant.vars["consent_answer"]) == 1
    #     )


def generate_page_sequence():
    return ([GenderAge]
        + [Education]
        + [IncomeLevel]
        + [EthnicityRace]
        + [ZipCode]
        + [BenefitToday]
        + [PoliticalOrientation]
        + [Results]
    )

page_sequence = generate_page_sequence()
