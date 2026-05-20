from enum import Enum

class State(Enum):
    """Represents the state of a cell in the game."""
    HIDDEN = 0
    OPENED = 1
    FLAGGED = 2