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
    [1.5, 2.5, 4, 6.4, 10.7],
    [1, 2, 3.5, 6.1, 12.3],
    [1.5, 2.6, 4.1, 6.5, 11.2],
    [1, 2, 3, 4.5, 9],
    [1.5, 2.9, 4.4, 6.7, 12.9],
    [1.5, 2.5, 4.5, 8.1, 13.5],
]


all_right_values = [
    [4, 4, 4, 4, 4],
    [3.5, 3.5, 3.5, 3.5, 3.5],
    [4.1, 4.1, 4.1, 4.1, 4.1],
    [3, 3, 3, 3, 3],
    [4.4, 4.4, 4.4, 4.4, 4.4],
    [4.5, 4.5, 4.5, 4.5, 4.5],
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

NUM_PLOTS = 16

plot_links = [
    "https://i.imgur.com/JcaBGNi.png",
    "https://i.imgur.com/ej3I1aa.png",
    "https://i.imgur.com/ZZItnq7.png",
    "https://i.imgur.com/if5oLFh.png",
    "https://i.imgur.com/vdbplSb.png",
    "https://i.imgur.com/t4sdSV6.png",
    "https://i.imgur.com/cCClmIn.png",
    "https://i.imgur.com/KgzsIH7.png",
    "https://i.imgur.com/kIlFFs8.png",
    "https://i.imgur.com/UndrAVo.png",
    "https://i.imgur.com/2BTKhi0.png",
    "https://i.imgur.com/vXTvq8a.png",
    "https://i.imgur.com/7YfqKtd.png",
    "https://i.imgur.com/4AAqISx.png",
    "https://i.imgur.com/TW3JYOC.png",
    "https://i.imgur.com/ma5nWH0.png",
]

PLOTS1 = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
PLOTS2 = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]