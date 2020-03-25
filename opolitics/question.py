from typing import List

from .block import Block


class Question:
    """Represents a single question of a `Block`

    A Question represents a set of different choices where the values
    are linearly calculated taking into account the corresponding p value
    and of course the total available budget.
    """

    def __init__(self, block: Block, index: int):
        """Create a new Question
        """
        self.block = block
        self.index = index
        self.num_choices = block.number_of_choices
        self.value = self.block.values[self.index]

    def question_number(self) -> int:
        """Get the number of this question in the block
        
        :return: Question number
        """
        return self.index + 1

    def start_values(self) -> List[str]:
        """ Take the initial number, and determine how much to decrease the amount by
            The expected number of values in this version is going to be 6. Decrease rate is 0.8 in this example.
            These numbers will be decreasing
        
        :return: list of values
        """
        absolute_decrease =  self.value - self.value*self.block.decrease_rate
        values = []
        for i in range(6):
            values.append(str(self.value - absolute_decrease*i) + '%')
        return values

    def end_values(self) -> List[str]:
        values =[]
        for i in range(6):
            values.append(str(i) + '%')
        return values
    
    def choice_index(self) -> range:
        """Range from 1 to the `num_choices` (including)
        """
        return range(1, self.num_choices + 1)
