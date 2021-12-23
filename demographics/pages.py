from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime

class FutureLineLength(Page):
    form_model = 'player'
    form_fields = ['slider_one_year','slider_five_year', 'slider_one_year_ever_clicked', 'slider_five_year_ever_clicked', "is_mobile_original_method", "is_mobile"]

    def is_displayed(self):
        return self.player.line_length_condition == 2


class PastLineLength(Page):
    form_model = 'player'
    form_fields = ['slider_one_year','slider_five_year', 'slider_one_year_ever_clicked', 'slider_five_year_ever_clicked', "is_mobile_original_method", "is_mobile"]

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

    def get_form_fields(player):
        return [race['name'] for race in Constants.races_ethn]


class ZipCode(Page):
    form_model = "player"
    form_fields = ["zipcode"]

class VSRespondents(Page):
    form_model = "player"
    form_fields = ["vs_respondents"]

    def is_displayed(self):
        return self.session.config["vs_on"]

class ResultsVS(Page):

    def is_displayed(self):
        return self.session.config["vs_on"]

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
    form_fields = ['slider_overlap_one_year', 'slider_overlap_five_year', 'slider_overlap_one_year_ever_clicked', 'slider_overlap_five_year_ever_clicked']

    def is_displayed(self):
        return self.player.overlap_condition == 1

    def vars_for_template(self):
        start_values = ["less overlap"] + ["" for i in range(5)] + ["more overlap"]
        return dict(
            start_values=start_values,
            end_values=[i for i in range(7)],
            idxs=[i for i in range(7)]
        )

class FutureSelvesOverlap(Page):
    form_model = 'player'
    form_fields = ['slider_overlap_one_year', 'slider_overlap_five_year', 'slider_overlap_one_year_ever_clicked', 'slider_overlap_five_year_ever_clicked']

    def is_displayed(self):
        return self.player.overlap_condition == 2
    
    def vars_for_template(self):
        start_values = ["less overlap"] + ["" for i in range(5)] + ["more overlap"]
        return dict(
            start_values=start_values,
            end_values=["<img src = {% static 'Demographics/overlap_images/future_1.png' %} width='149' height='84'/>", "", "", "<img src = {% static 'Demographics/overlap_images/future_2.png' %} width='149' height='84'/>", "", "", "<img src = {% static 'Demographics/overlap_images/future_3.png' %} width='149' height='84'/>"],
            idxs=[i for i in range(7)]
        )

class InterfaceChoice(Page):
    form_model = 'player'
    form_fields = ['interface_choice']

    def is_displayed(self):
        return int(self.participant.vars["condition"]) == 2 or int(self.participant.vars["condition"]) == 4 or int(self.participant.vars["condition"]) == 6 or int(self.participant.vars["condition"]) == 8

class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]
    
class Results(Page):

    def is_displayed(self):
        return self.session.config["vs_on"]==0




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
        + [FutureSelvesOverlap]
        + [InterfaceChoice]
        + [Feedback]
        + [Results]
        + [ResultsVS]
    )

page_sequence = generate_page_sequence()
