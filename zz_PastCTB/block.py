from typing import List

class Block:
    """Describes a single block consisting of multiple choices
    """
    def __init__(self,
                 left_values: List[float],
                 right_values: List[float],
                 t_earlier: str,
                 t_later: str,
                 number_of_choices: int,
                 block_index: int,
                 show_least_initial_value_first: bool = False):
        """Create a new block consisting of multiple choices. All delays are treated as WEEKS.
        :param values: List with fraction of initial value to use per block
        :param initial_payout_delay: Number of days until initial payout
        :param initial_to_last_payout_delay: Number of days between initial and last payout (delay)
        :param number_of_choices: Number of choices
        :param show_least_initial_value_first: Set to `True` in order to show the least amount of initial
        payout money as the first option
        """
        if type(left_values) is not list or type(right_values) is not list:
            raise ValueError("values must be a list, e.g. [1.05, 1.03]")
        if type(number_of_choices) is not int:
            raise ValueError("number_of_choices must be integers")
        if number_of_choices < 0:
            raise ValueError("number of choices must be >= 0")

        self.block_index = block_index
        self.left_values = left_values
        self.right_values = right_values
        self.t_later = t_later
        self.t_earlier = t_earlier
        self.number_of_choices = number_of_choices
        self.show_least_initial_value_first = show_least_initial_value_first     

    def questions(self) -> List['Question']:
        """Get the list of Questions described by this block
        :return: List of Questions
        """
        from .question import Question
        return [Question(self, self.block_index, i) for i in range(len(self.left_values))]

    def text_delay_start(self) -> str:
        """Returns a human readable text describing the start of the block (e.g. in 1 year) from today.
        :return: Human readable start of block from today
        """
        return self.t_later

    def text_total_end(self) -> str:
        """Returns a human readable text describing the end of the block (e.g. in 2 years) from today.

        :return: Human readable end of block from today
        """
        return self.t_earlier
