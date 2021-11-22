from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime


class PastLineLength(Page):
    form_model = 'player'
    form_fields = ['slider_one_year', 'check_slider_one_year', 'slider_five_year', 'check_slider_five_year']
    
    def error_message(self, value):
        if value["check_slider_one_year"] == None or value["check_slider_five_year"] == None:
            return 'Please use the slider to make a decision.'

class DirectGrowth(Page):
    form_model = 'player'
    form_fields = ['slider_direct_growth', 'check_slider_direct_growth', 'direct_growth']
    
    def error_message(self, value):
        if value["check_slider_direct_growth"] == None:
            return 'Please use the slider to make a decision.'




def generate_page_sequence():
    return (
        [DirectGrowth] +
        [PastLineLength] 
    )

page_sequence = generate_page_sequence()
