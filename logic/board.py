import numpy as np
from logic.cell_state import State

class Board:
    """Represents the game board."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.states_grid = np.full((height, width), State.HIDDEN, dtype=object)
        self.game_over = False

    def reveal_cell(self, x: int, y: int) -> None:
        """Reveals a cell on the board. Chages the state of the cell and updates the board accordingly.
        Args:
            x (int): The x-coordinate of the cell to reveal.
            y (int): The y-coordinate of the cell to reveal.
        """
        #TODO: Implement the logic to reveal a cell and update the board state accordingly.
        # This should include checking for mines, updating the revealed state, and handling game over conditions.
        pass

    @property
    def revealed_cells(self) -> list[tuple[int, int]]:
        """Returns a list of revealed cells."""
        matched_indices = np.argwhere(self.states_grid == State.OPENED)
        return [(x, y) for y, x in matched_indices]
    
    @property
    def hidden_cells(self) -> list[tuple[int, int]]:
        """Returns a list of hidden cells."""
        matched_indices = np.argwhere(self.states_grid == State.HIDDEN)
        return [(x, y) for y, x in matched_indices]
    
