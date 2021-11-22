from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Justin Curl'

doc = """
short demographics questionnaire that can be appended to end of other apps
"""


class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        for player in self.get_players():
            player.code = str(random.randrange(10 ** 11, 10 ** 12))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    race = models.StringField()

    code = models.StringField()

    political_orientation = models.IntegerField(
        blank=True,
        choices=[
            [1, "Republican"],
            [2, "Democrat"],
            [3, "Independent"],
            [4, "Other"],
        ],
        widget=widgets.RadioSelect,
    )
    republican_option = models.IntegerField(
        blank=True,
        choices=[
            [1, "Strong"],
            [2, "Not very strong"],
        ],
        widget=widgets.RadioSelect,
    )
    democrat_option = models.IntegerField(
        blank=True,
        choices=[
            [1, "Strong"],
            [2, "Not very strong"],
        ],
        widget=widgets.RadioSelect,
    )
    independent_option = models.IntegerField(
        blank=True,
        choices=[
            [1, "Republican Party"],
            [2, "Democratic Party"],
            [3, "Neither Party"]
        ],
        widget=widgets.RadioSelect,
    )

    income_level = models.IntegerField(
        choices=[
            [1, "Less than $10,000"],
            [2, "$10,000 - $19,999"],
            [3, "$20,000 - $29,999"],
            [4, "$30,000 - $39,999"],
            [5, "$40,000 - $49,999"],
            [6, "$50,000 - $59,999"],
            [7, "$60,000 - $69,999"],
            [8, "$70,000 - $79,999"],
            [9, "$80,000 - $89,999"],
            [10, "$90,000 - $99,999"],
            [11, "$10,000 - $119,999"],
            [12, "$120,000 - $149,999"],
            [13, "$150,000 - $199,999"],
            [14, "$200,000 - $249,999"],
            [15, "$250,000 - $349,999"],
            [16, "$350,000 - $499,999"],
            [17, "$500,000 or moree"],
            [-1, "Prefer not to say"],
        ],
        blank=True,
        widget=widgets.RadioSelect,
    )

    benefit_today = models.IntegerField(
        choices=[
            [0, "0"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    education = models.IntegerField(
    choices=[
        [1, "I do not have a high school degree or GED "],
        [2, "Regular high school degree "],
        [3, "GED or alternative credential "],
        [4, "Some college credit, no degree"],
        [5, "Associate’s degree (for example: AA, AS) "],
        [6, "Bachelor’s degree (for example: BA, BS) "],
        [7, "Graduate or professional degree "],
    ],
    blank=True,
    widget=widgets.RadioSelect,
)

    gender = models.IntegerField(
        blank=True,
        choices=[
            [1, "Male"],
            [2, "Female"],
        ],
        widget=widgets.RadioSelect,
    )

    ethnicity = models.BooleanField(
        blank=True, choices=[[True, "Yes"], [False, "No"]], widget=widgets.RadioSelect
    )

    age = models.IntegerField(blank=True, min=18, max=110)

    feedback = models.LongStringField(blank=True)

    check_slider_overlap = models.IntegerField()
    slider_overlap = models.StringField()

    zipcode = models.IntegerField(blank=True, min=0, max=99999)
