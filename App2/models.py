from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
)
import random, itertools

author = 'Justin Curl'

doc = """
Initial consent app that can be prepended onto other apps
"""


class Constants(BaseConstants):
    name_in_url = 'App2'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self) -> None:
        r_direct_options = [
            (1, "Before"),
            (2, "After"),
        ]

        r_plot_options = [
            (1, "Past"),
            (2, "Future"),
        ]

        rand_direct_choice = random.choice(r_direct_options)
        ordering = itertools.cycle(rand_direct_choice)
        start_at_random_direct = itertools.islice(ordering, rand_direct_choice[0], None)

        rand_plot_choice = random.choice(r_plot_options)
        ordering = itertools.cycle(rand_plot_choice)
        start_at_random_plot = itertools.islice(ordering, rand_plot_choice[0], None)

        for player in self.get_players():
            if self.round_number == 1:
                player_direct_order = next(start_at_random_direct)
                player.direct_condition = player_direct_order[0]

                player_plot_order = next(start_at_random_plot)
                player.plot_condition = player_plot_order[0]
            else:
                player.plot_condition = player.in_round(self.round_number - 1).plot_condition
                player.direct_condition = player.in_round(self.round_number - 1).direct_condition



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    direct_condition = models.IntegerField()
    plot_condition = models.IntegerField()
    slider_direct_growth = models.StringField()
    direct_growth = models.IntegerField(choices=[[1, "4% this year and no growth next year"], [2, "4% next year and no growth this year"]], widget=widgets.RadioSelect,)
