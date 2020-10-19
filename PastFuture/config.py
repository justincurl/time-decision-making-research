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
    [1.5, 2.25, 3.0, 6.0, 12.0],
    [1.45, 2.175, 2.9, 5.8, 11.6],
    [1.75, 2.625, 3.5, 7.0, 14.0],
    [1.8, 2.7, 3.6, 7.2, 14.4],
    [1.55, 2.325, 3.1, 6.2, 12.4],
    [1.65, 2.475, 3.3, 6.6, 13.2],
]


all_right_values = [
    [3.0, 3.0, 3.0, 3.0, 3.0],
    [2.9, 2.9, 2.9, 2.9, 2.9],
    [3.5, 3.5, 3.5, 3.5, 3.5],
    [3.6, 3.6, 3.6, 3.6, 3.6],
    [3.1, 3.1, 3.1, 3.1, 3.1],
    [3.3, 3.3, 3.3, 3.3, 3.3],
]

block1_order = [i for i in range(NUM_BLOCKS)]
block2_order = [i for i in range(NUM_BLOCKS)]

BLOCKS1 = [
    Block(
        left_values=all_left_values[0],
        right_values=all_right_values[0],
        top_earlier_term=1,
        bottom_later_term=2,
        number_of_choices=6,
        block_index=int(block1_order[0]),
    ),
    Block(
        left_values=all_left_values[1],
        right_values=all_right_values[1],
        top_earlier_term=1,
        bottom_later_term=3,
        number_of_choices=6,
        block_index=int(block1_order[1]),
    ),
    Block(
        left_values=all_left_values[2],
        right_values=all_right_values[2],
        top_earlier_term=1,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block1_order[2]),
    ),
    Block(
        left_values=all_left_values[3],
        right_values=all_right_values[3],
        top_earlier_term=2,
        bottom_later_term=3,
        number_of_choices=6,
        block_index=int(block1_order[3]),
    ),
    Block(
        left_values=all_left_values[4],
        right_values=all_right_values[4],
        top_earlier_term=2,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block1_order[4]),
    ),
    Block(
        left_values=all_left_values[5],
        right_values=all_right_values[5],
        top_earlier_term=3,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block1_order[5]),
    ),
]

BLOCKS2 = [
    Block(
        left_values=all_left_values[0],
        right_values=all_right_values[0],
        top_earlier_term=1,
        bottom_later_term=2,
        number_of_choices=6,
        block_index=int(block2_order[0]),
    ),
    Block(
        left_values=all_left_values[1],
        right_values=all_right_values[1],
        top_earlier_term=1,
        bottom_later_term=3,
        number_of_choices=6,
        block_index=int(block2_order[1]),
    ),
    Block(
        left_values=all_left_values[2],
        right_values=all_right_values[2],
        top_earlier_term=1,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block2_order[2]),
    ),
    Block(
        left_values=all_left_values[3],
        right_values=all_right_values[3],
        top_earlier_term=2,
        bottom_later_term=3,
        number_of_choices=6,
        block_index=int(block2_order[3]),
    ),
    Block(
        left_values=all_left_values[4],
        right_values=all_right_values[4],
        top_earlier_term=2,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block2_order[4]),
    ),
    Block(
        left_values=all_left_values[5],
        right_values=all_right_values[5],
        top_earlier_term=3,
        bottom_later_term=4,
        number_of_choices=6,
        block_index=int(block2_order[5]),
    ),
]

NUM_PLOTS = 18

plot_links = [
    "https://i.imgur.com/sH9YQiQ.png",
    "https://i.imgur.com/8qaYO7I.png",
    "https://i.imgur.com/rDgwEYP.png",
    "https://i.imgur.com/9ufxb8h.png",
    "https://i.imgur.com/aI805Ti.png",
    "https://i.imgur.com/ut9ksk4.png",
    "https://i.imgur.com/eFEVW00.png",
    "https://i.imgur.com/osFSpsG.png",
    "https://i.imgur.com/1BOqhIe.png",
    "https://i.imgur.com/chWQ17R.png",
    "https://i.imgur.com/WKHOMT7.png",
    "https://i.imgur.com/N2CmC5E.png",
    "https://i.imgur.com/E8n0Lbo.png",
    "https://i.imgur.com/6SPZcfz.png",
    "https://i.imgur.com/P0EKWit.png",
    "https://i.imgur.com/uz0E0hJ.png",
    "https://i.imgur.com/0t7BhoX.png",
    "https://i.imgur.com/N0NA4Gs.png",
]

PLOTS1 = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
PLOTS2 = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]