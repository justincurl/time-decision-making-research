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
    [8.6, 5.7, 2.8, 1.4],
    [6.6, 4.4, 2.2, 1.1],
    [8.7, 5.8, 2.9, 1.4],
    [6.9, 4.6, 2.3, 1.2],
    [9, 6, 3, 1.5],
    [8.9, 5.9, 3, 1.5]
]


all_right_values = [
    [4.3, 4.3, 4.3, 4.3],
    [4.4, 4.4, 4.4, 4.4],
    [4, 4, 4, 4],
    [5.8, 5.8, 5.8, 5.8],
    [5.6, 5.6, 5.6, 5.6],
    [4.3, 4.3, 4.3, 4.3],
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

NUM_PLOTS = 18

plot_links = [
    "https://i.imgur.com/qpaRNrX.png",
    "https://i.imgur.com/TuSpZo0.png",
    "https://i.imgur.com/7LZvwmr.png",
    "https://i.imgur.com/NpkqJHE.png",
    "https://i.imgur.com/YEtQoF2.png",
    "https://i.imgur.com/T9X2bBp.png",
    "https://i.imgur.com/dvfgeqj.png",
    "https://i.imgur.com/Q3IiPZR.png",
    "https://i.imgur.com/jAQ6CJb.png",
    "https://i.imgur.com/25ni7G4.png",
    "https://i.imgur.com/L8DiVvQ.png",
    "https://i.imgur.com/ASGntyM.png",
    "https://i.imgur.com/i1Sxc32.png",
    "https://i.imgur.com/Xkj8GZK.png",
    "https://i.imgur.com/SKaSxxG.png",
    "https://i.imgur.com/YqhDmdB.png",
    "https://i.imgur.com/1sdQawn.png",
    "https://i.imgur.com/mWqxdRK.png"
]

PLOTS = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
