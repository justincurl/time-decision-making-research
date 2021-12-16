from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        # define page as round_number
        page = self.subsession.round_number
        if self.player.line_length_condition == 2:
            yield pages.FutureLineLength, dict(slider_one_year=1, slider_five_year=2)
        if self.player.line_length_condition == 1:
            yield pages.PastLineLength, dict(slider_one_year=1, slider_five_year=2)
        yield pages.GenderAge, dict(gender=1, age=27)
        yield pages.Education, dict(education=1)
        yield pages.IncomeLevel, dict(income_level=1)
        yield pages.EthnicityRace, dict(ethnicity=True, white=1, black=1, asian=1, native=1, islander=1,other=1)
        yield pages.ZipCode, dict(zipcode=12345)
        if self.session.config["vs_on"]:
            yield pages.VSRespondents, dict(vs_respondents=1)
        yield pages.WorkSituation, dict(work_situation=1)
        yield pages.BenefitToday, dict(benefit_answer=1)
        yield pages.PoliticalOrientation1, dict(political_orientation=1)
        yield pages.PoliticalOrientation2, dict(republican_option=1)
        if self.player.overlap_condition == 1:
            yield pages.PastSelvesOverlap, dict(slider_overlap_one_year=1, slider_overlap_five_year=2)
        if self.player.overlap_condition == 2:
            yield pages.FutureSelvesOverlap, dict(slider_overlap_one_year=1, slider_overlap_five_year=2)
        if int(self.participant.vars["condition"]) == 2 or int(self.participant.vars["condition"]) == 4 or int(self.participant.vars["condition"]) == 6 or int(self.participant.vars["condition"]) == 8:
            yield pages.InterfaceChoice, dict(interface_choice=1)
        yield pages.Feedback, dict(feedback="trial")