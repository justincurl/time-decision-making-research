from typing import List
from .block import Block


class Plot:
    """Represents a single plot of Healy and Lenz

    """

    def __init__(self, image_link):
        """Create a new Question
        """
        self.num_choices = 4
        self.image_link = image_link

    def start_values(self) -> List[str]:
        """ Take the initial number, and determine how much to decrease the amount by
            The expected number of values in this version is going to be 6. Decrease rate is 0.8 in this example.
            These numbers will be decreasing 
        
        :return: list of values
        """
        return ["Very bad", "Fairly bad", "Fairly good", "Very good"]

    def choice_index(self) -> range:
        """Range from 1 to the `num_choices` (including)
        """
        return range(1, self.num_choices + 1)
