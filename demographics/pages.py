from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class FutureLineLength(Page):
    form_model = 'player'
    form_fields = ['slider_one_year','slider_five_year']

    def is_displayed(self):
        return self.player.line_length_condition == 2


class PastLineLength(Page):
    form_model = 'player'
    form_fields = ['slider_one_year','slider_five_year']

    def is_displayed(self):
        return self.player.line_length_condition == 1

class GenderAge(Page):
    form_model = "player"
    form_fields = ["gender", "age"]

class Education(Page):
    form_model = "player"
    form_fields = ["education"]

class IncomeLevel(Page):
    form_model = "player"
    form_fields = ["income_level"]

class EthnicityRace(Page):
    form_model = "player"
    form_fields = ["ethnicity", "race"]

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
        }

class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

class VSRespondents(Page):
    form_model = "player"
    form_fields = ["vs_respondents"]

    def is_displayed(self):
        #  set to true during VS survey
        return False

class WorkSituation(Page):
    form_model = "player"
    form_fields = ["work_situation"]

class BenefitToday(Page):
    form_model = "player"
    form_fields = ["benefit_answer"]

    def vars_for_template(self):
        start_values = ["completely unwilling to do so"] + ["" for i in range(9)] + ["very willing to do so"]
        return dict(
            start_values=start_values,
            end_values=[i for i in range(11)],
            idxs=[i for i in range(11)]
        )

class PoliticalOrientation1(Page):
    form_model = "player"
    form_fields = ["political_orientation"]

class PoliticalOrientation2(Page):
    form_model = "player"
    form_fields = ["political_orientation", "independent_option", "republican_option", "democrat_option"]

class PastSelvesOverlap(Page):
    form_model = 'player'
    form_fields = ['slider_overlap_one_year', 'slider_overlap_five_year']

    def is_displayed(self):
        return self.player.overlap_condition == 1

class FutureSelvesOverlap(Page):
    form_model = 'player'
    form_fields = ['slider_overlap_one_year', 'slider_overlap_five_year']

    def is_displayed(self):
        return self.player.overlap_condition == 2

class InterfaceChoice(Page):
    form_model = 'player'
    form_fields = ['interface_choice']

    def is_displayed(self):
        return int(self.participant.vars["condition"]) == 2 or int(self.participant.vars["condition"]) == 4 or int(self.participant.vars["condition"]) == 6 or int(self.participant.vars["condition"]) == 8

class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]
    
class Results(Page):
    pass




def generate_page_sequence():
    return (
        [FutureLineLength]
        + [PastLineLength]
        + [GenderAge]
        + [Education]
        + [IncomeLevel]
        + [EthnicityRace]
        + [ZipCode]
        + [VSRespondents]
        + [WorkSituation]
        + [BenefitToday]
        + [PoliticalOrientation1]
        + [PoliticalOrientation2]
        + [PastSelvesOverlap]
        + [InterfaceChoice]
        + [Feedback]
        + [Results]
    )

page_sequence = generate_page_sequence()
