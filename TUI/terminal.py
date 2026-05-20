from  blessed import Terminal

class TUI:

    def __init__(self):
        self.term = Terminal()
        self.running = True

    def draw_screen(self):
        """Draws the game screen."""
        print(self.term.clear())
        print(self.term.move(0, 0) + "Welcome to Yet Another Saper Simulator!")
        print(self.term.move(1, 0) + "Press 'q' to quit.")
        #TODO: Implement the logic to draw the game board and other UI elements.

    def run(self):
        """Runs the main loop of the TUI."""
        with self.term.fullscreen(), self.term.hidden_cursor(), self.term.cbreak():

            while self.running:
                self.draw_screen()
                key = self.term.inkey(timeout=0.1)
                if key == 'q':
                    self.running = False