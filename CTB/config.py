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

NUM_PLOTS = 18
# small_plot_links = [
#     "https://i.imgur.com/bclJT7b.png",
#     "https://i.imgur.com/mfZ4X2j.png",
#     "https://i.imgur.com/zfYOn1A.png",
#     "https://i.imgur.com/wyFkWUQ.png",
#     "https://i.imgur.com/RXXZRdB.png",
#     "https://i.imgur.com/CRj3Tcc.png",
#     "https://i.imgur.com/BnMUSKV.png",
#     "https://i.imgur.com/MvFDoc7.png",
#     "https://i.imgur.com/6iHDf6b.png",
#     "https://i.imgur.com/6hGujUK.png",
#     "https://i.imgur.com/8ixS5hv.png",
#     "https://i.imgur.com/KXPVBCR.png",
#     "https://i.imgur.com/EKBwKih.png",
#     "https://i.imgur.com/Ubtp5em.png",
#     "https://i.imgur.com/hSfaWOw.png",
#     "https://i.imgur.com/HnniYEh.png",
#     "https://i.imgur.com/pSJXSUO.png",
#     "https://i.imgur.com/hPcouQo.png"
# ]
plot_links = [
    "https://i.imgur.com/tv80mGo.png",
    "https://i.imgur.com/QP549W9.png",
    "https://i.imgur.com/ff7lu55.png",
    "https://i.imgur.com/eEBRZFo.png",
    "https://i.imgur.com/qOcXBox.png",
    "https://i.imgur.com/FCvX5dt.png",
    "https://i.imgur.com/y34mfxd.png",
    "https://i.imgur.com/aZl77Sz.png",
    "https://i.imgur.com/slbHvpo.png",
    "https://i.imgur.com/iNVr5g8.png",
    "https://i.imgur.com/maIW58T.png",
    "https://i.imgur.com/AXwjhC9.png",
    "https://i.imgur.com/Git8BSM.png",
    "https://i.imgur.com/qResnR3.png",
    "https://i.imgur.com/uP4eNmx.png",
    "https://i.imgur.com/qMlDI48.png",
    "https://i.imgur.com/yJKtg0Y.png",
    "https://i.imgur.com/m4DjdUF.png"
]

# SMALL_PLOTS = [Plot(image_link=small_plot_links[i]) for i in range(NUM_PLOTS)]
PLOTS = [Plot(image_link=plot_links[i]) for i in range(NUM_PLOTS)]
