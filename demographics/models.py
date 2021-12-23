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
    races = [
        dict(name='white', label="White"),
        dict(name='black', label="Black or African America"),
        dict(name='asian', label="Asian"),
        dict(name='native', label="American Indian or Alaska Native"),
        dict(name='islander', label="Native Hawaiian or Pacific Islander"),
        dict(name='other', label="Some other race"),
    ]
    races_ethn = [
        dict(name='white', label="White"),
        dict(name='black', label="Black or African America"),
        dict(name='asian', label="Asian"),
        dict(name='native', label="American Indian or Alaska Native"),
        dict(name='islander', label="Native Hawaiian or Pacific Islander"),
        dict(name='other', label="Some other race"),
        dict(name='ethnicity'),
    ]


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        r_line_length_options = [
            (1, "Past"),
            (2, "Future"),
        ]

        r_selves_overlap_options = [
            (1, "Past"),
            (2, "Future"),
        ]

        for player in self.get_players():
            if self.round_number == 1:
                player.line_length_condition = random.choice(r_line_length_options)[0]
                player.overlap_condition = random.choice(r_selves_overlap_options)[0]
            else:
                player.line_length_condition = player.in_round(self.round_number - 1).line_length_condition
                player.overlap_condition = player.in_round(self.round_number - 1).overlap_condition
            player.code = str(random.randrange(10 ** 11, 10 ** 12))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    white = models.BooleanField(blank=True)
    black = models.BooleanField(blank=True)
    asian = models.BooleanField(blank=True)
    native = models.BooleanField(blank=True)
    islander = models.BooleanField(blank=True)
    other = models.BooleanField(blank=True)

    line_length_condition = models.IntegerField()

    overlap_condition = models.IntegerField()

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
            [17, "$500,000 or more"],
            [-1, "Prefer not to say"],
        ],
        blank=True,
    )

    work_situation = models.IntegerField(
        choices=[
            [1,"Working full-time"],
            [2,"Working part-time"],
            [3,"Temporarily unemployed (including furloughed)"],
            [4,"Unemployed"],
            [5,"Retired"],
            [6,"Homemaker or stay-at-home parent"],
            [7,"Student"],
            [8,"Disabled and unable to work"],

        ],
        blank=True,
        widget=widgets.RadioSelect,
    )

    benefit_answer = models.IntegerField(blank=True)

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

    interface_choice = models.IntegerField(
        choices=[
            [1, "Choosing one of the response buttons"],
            [2, "Moving the green blocks across periods"],
            [3, "Both methods were equally as intuitive"]
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

    slider_one_year = models.StringField(blank=True)
    slider_five_year = models.StringField(blank=True)

    slider_overlap_one_year = models.StringField(blank=True)
    slider_overlap_five_year = models.StringField(blank=True)

    slider_one_year_ever_clicked = models.IntegerField(blank=True)
    slider_five_year_ever_clicked = models.IntegerField(blank=True)
    slider_overlap_one_year_ever_clicked = models.IntegerField(blank=True)
    slider_overlap_five_year_ever_clicked = models.IntegerField(blank=True)

    is_mobile = models.BooleanField()
    is_mobile_original_method = models.StringField()


    zipcode = models.IntegerField(blank=True, min=0, max=99999)

    vs_respondents = models.IntegerField(
        blank=True,
        choices=[
            [1, "Yes"],
            [2, "No"],
        ],
        widget=widgets.RadioSelect,
    )
