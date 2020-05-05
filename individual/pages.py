from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class SimpleSurvey(Page):
    form_model = 'player'
    form_fields = ['name', 'age', 'political_affiliation']

page_sequence = [SimpleSurvey]