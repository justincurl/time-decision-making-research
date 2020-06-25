"""
This file includes all available configuration options for the otime app.

Modify this file to set all your preferences - also modify `templates/otime/Results.html` to your liking
which will be displayed after all questions of all blocks have been answered.

It's not recommended to edit any of the other files.

Be sure to also check the README.md file!
"""
import random
from .block import Block
from .plot import Plot

#: The total budget available for each choice
TOTAL_BUDGET = 5

# Number of Blocks
NUM_BLOCKS = 6

#: Set to True if you want blocks to be randomized in order
RANDOMIZE_BLOCKS = True

RANDOMIZE_PLOTS = True

#: The configuration for all blocks to be displayed to the user
#: Note:
#: - The given delays are treated as WEEKS where an initial delay of 0 means today.
#: - The order of interest_rates given is the order in which they will be display, i.e.
#:      to change the order of display just change the order of values here
""" Edit the number of choices and values to put in the blocks here """


all_left_values = [
    [8, 5.3, 2.6, 1.3],
    [6.9, 4.6, 2.3, 1.2],
    [7.2, 4.8, 2.4, 1.2],
    [7.4, 4.9, 2.4, 1.2],
    [7.2, 4.8, 2.4, 1.2],
    [7.2, 4.8, 2.4, 1.2],
]


all_right_values = [
    [3.4, 3.4, 3.4, 3.4],
    [3.7, 3.7, 3.7, 3.7],
    [3, 3, 3, 3],
    [5.4, 5.4, 5.4, 5.4],
    [5.4, 5.4, 5.4, 5.4],
    [3.8, 3.8, 3.8, 3.8],
]

block_order = [i for i in range(NUM_BLOCKS)]

BLOCKS = [
    Block(
        left_values=all_left_values[0],
        right_values=all_right_values[0],
        top_later_term=2,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index=int(block_order[0]),
    ),
    Block(
        left_values=all_left_values[1],
        right_values=all_right_values[1],
        top_later_term=3,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index=int(block_order[1]),
    ),
    Block(
        left_values=all_left_values[2],
        right_values=all_right_values[2],
        top_later_term=4,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index=int(block_order[2]),
    ),
    Block(
        left_values=all_left_values[3],
        right_values=all_right_values[3],
        top_later_term=3,
        bottom_earlier_term=2,
        number_of_choices=6,
        block_index=int(block_order[3]),
    ),
    Block(
        left_values=all_left_values[4],
        right_values=all_right_values[4],
        top_later_term=4,
        bottom_earlier_term=2,
        number_of_choices=6,
        block_index=int(block_order[4]),
    ),
    Block(
        left_values=all_left_values[5],
        right_values=all_right_values[5],
        top_later_term=4,
        bottom_earlier_term=3,
        number_of_choices=6,
        block_index=int(block_order[5]),
    ),
]

NUM_PLOTS = 24

plot_links = [
    "https://i.imgur.com/wI95aRk.png",
    "https://i.imgur.com/qBLDL9q.png",
    "https://i.imgur.com/afR6gMb.png",
    "https://i.imgur.com/Tz22E9V.png",
    "https://i.imgur.com/5rL2vnx.png",
    "https://i.imgur.com/Rzx5ejS.png",
    "https://i.imgur.com/rXEmgQy.png",
    "https://i.imgur.com/3TItooK.png",
    "https://i.imgur.com/eAygo5V.png",
    "https://i.imgur.com/9LNZ5GM.png",
    "https://i.imgur.com/ywcOXAu.png",
    "https://i.imgur.com/nF7Scjj.png",
    "https://i.imgur.com/j8Jd3r9.png",
    "https://i.imgur.com/Ac0SpHS.png",
    "https://i.imgur.com/tLBY1G3.png",
    "https://i.imgur.com/B17WGCS.png",
    "https://i.imgur.com/2HVuOhO.png",
    "https://i.imgur.com/Wqs15Kb.png",
    "https://i.imgur.com/FVGCKWd.png",
    "https://i.imgur.com/QzdomVt.png",
    "https://i.imgur.com/t2Y8hFx.png",
    "https://i.imgur.com/9q9Wgpt.png",
    "https://i.imgur.com/CY2bxmX.png",
    "https://i.imgur.com/W8nsFX0.png",
]

PLOTS = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
