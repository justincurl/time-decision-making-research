from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import datetime


class NonConsent(Page):
    def is_displayed(self):
        return json.loads(self.participant.vars["consent_answer"]) == 0

class Consent(Page):
    form_model = "player"
    form_fields = ["consent_answer"]

    def before_next_page(self):
        self.participant.vars["consent_answer"] = self.player.consent_answer
        return super().before_next_page()


class PhoneDevice(Page):
    def is_displayed(self):
        return (self.player.device_type == 3) or (self.player.device_type == 4) or (self.player.device_type == 5)

class DeviceType2(Page):
    form_model = "player"
    form_fields = ["is_mobile"]

class DeviceType(Page):
    form_model = "player"
    form_fields = ["device_type", "is_mobile_original_method"]

    def vars_for_template(self):
        return dict(
            phone=self.player.is_mobile
        )


def generate_page_sequence():
    return (
        [DeviceType2]
        + [DeviceType]
        + [PhoneDevice]
        + [Consent]
        + [NonConsent]
    )

page_sequence = generate_page_sequence()
