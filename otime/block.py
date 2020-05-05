from typing import List

class Block:
    """Describes a single block consisting of multiple choices
    """
    def __init__(self,
                 values: List[float],
                 initial_payout_delay: int,
                 initial_to_last_payout_delay: int,
                 number_of_choices: int,
                 decrease_rate: int,
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
        if type(values) is not list:
            raise ValueError("values must be a list, e.g. [1.05, 1.03]")
        if (type(initial_payout_delay) is not int
                or type(initial_payout_delay) is not int
                or type(number_of_choices) is not int):
            raise ValueError("parameters initial_payout_delay, initial_to_last_payout_delay, "
                             "and number_of_choices must be integers")
        if number_of_choices < 0:
            raise ValueError("number of choices must be >= 0")

        self.block_index = block_index
        self.values = values
        self.initial_payout_delay = initial_payout_delay
        self.initial_to_last_payout_delay = initial_to_last_payout_delay
        self.number_of_choices = number_of_choices
        self.show_least_initial_value_first = show_least_initial_value_first
        self.decrease_rate = decrease_rate

    def _instructions(self) -> str:
        if self.player.choices:
            return "Econ Instructions"
        else:
            return "Politics Instructions"

    def _title(self) -> str:
        if self.player.choices:
            return "Payment Preferences"
        else:
            return "Economic Growth"
    
    def _secondary_instructions
        if self.player.choices:
            return "Secondary Econ Instructions"
        else:
            return "Secondary Politics Instructions"


    def _text_delay_start(self) -> str:
        """Returns a human readable text describing the start of the block (e.g. in 1 year) from today.
        :return: Human readable start of block from today
        """
        if self.player.choices:
            return self._days_to_text(self.initial_payout_delay)
        else:
            return self._years_to_text(self.initial_payout_delay)

    def _text_total_end(self) -> str:
        """Returns a human readable text describing the end of the block (e.g. in 2 years) from today.

        :return: Human readable end of block from today
        """
        if self.player.choices:
            return self._days_to_text(self.initial_payout_delay + self.initial_to_last_payout_delay)
        else:
            return self._years_to_text(self.initial_payout_delay + self.initial_to_last_payout_delay)

    @staticmethod
    def _years_to_text(value: int) -> str:
        if value == 0: 
            return "this year"
        if value == 1:
            return "next year"
        else:
            return str(value) + " years from now"

    @staticmethod
    def _days_to_text(value: int) -> str:
        """Interprets the given value as number of days in the future and returns a human readable presentation

        :param value: Number of days in the future
        :return: Human readable presentation
        """
        if value == 0:
            return "today"
        if value % 7 == 0:
            if value == 7:
                return "in 1 week"
            return "in {0:.0f} weeks".format(value / 7)
        if value == 1:
            return "in 1 day"
        return "in {0:.0f} days".format(value)
