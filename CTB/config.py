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
RANDOMIZE_BLOCKS = False

RANDOMIZE_PLOTS = True

#: The configuration for all blocks to be displayed to the user
#: Note:
#: - The given delays are treated as WEEKS where an initial delay of 0 means today.
#: - The order of interest_rates given is the order in which they will be display, i.e.
#:      to change the order of display just change the order of values here
""" Edit the number of choices and values to put in the blocks here """

all_left_values = [[5.5, 4, 2.8, 1.1], [5.2, 3.5, 2.7, 1.8], [5.6, 3.8, 2.6, 1.6], [5.2, 3.5, 2.7, 1.8], 
        [5.6, 3.8, 2.6, 1.6], [5.6, 3.8, 2.6, 1.6]]

all_right_values = [[4.2, 4.2, 4.2, 4.2], [4.2, 4.2, 4.2, 4.2], [4.2, 4.2, 4.2, 4.2], [5.5, 5.5, 5.5, 5.5], 
        [5.5, 5.5, 5.5, 5.5], [5.3, 5.3, 5.3, 5.3]]

block_order = [i for i in range(NUM_BLOCKS)]

BLOCKS = [
    Block(
        left_values=all_left_values[0],
        right_values=all_right_values[0],
        top_later_term=2,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index= int(block_order[0])
    ), 
    Block(
        left_values=all_left_values[1],
        right_values=all_right_values[1],
        top_later_term=3,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index= int(block_order[1])
    ),
    Block(
        left_values=all_left_values[2],
        right_values=all_right_values[2],
        top_later_term=4,
        bottom_earlier_term=1,
        number_of_choices=6,
        block_index= int(block_order[2])
    ),
    Block(
        left_values=all_left_values[3],
        right_values=all_right_values[3],
        top_later_term=3,
        bottom_earlier_term=2,
        number_of_choices=6,
        block_index= int(block_order[3])
    ),
    Block(
        left_values=all_left_values[4],
        right_values=all_right_values[4],
        top_later_term=4,
        bottom_earlier_term=2,
        number_of_choices=6,
        block_index= int(block_order[4])
    ),
    Block(
        left_values=all_left_values[5],
        right_values=all_right_values[5],
        top_later_term=4,
        bottom_earlier_term=3,
        number_of_choices=6,
        block_index= int(block_order[5])
    )
]

NUM_PLOTS = 5

plot_links = ["https://i.imgur.com/7nVED9H.png", "https://i.imgur.com/PtfIsEV.png", "https://i.imgur.com/aAS88mA.png", "https://i.imgur.com/bCqMEek.png", "https://i.imgur.com/Xflg73S.png"]

PLOTS = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
