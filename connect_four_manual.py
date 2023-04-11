import pygame

from pygame_gui.windows import UIMessageWindow

class ConnectFourManual(UIMessageWindow):
    def __init__(self, manager, button):
        super().__init__(rect=pygame.Rect((10, 10), (600, 600)), manager=manager, window_title='Connect Four Manual', object_id='#connect_four_manual', 
            html_message='<font color=normal_text>'
                         'The goal of the game is to connect four tokens of the same type vertically, horizontally, or diagonally.<br><br>'
                         'To drop a token, click the Select button beneath a column. The token will be dropped to the lowest available space in that column.<br><br>'
                         'The image below shows the board state after the first player dropped a token in the first column.<br><br>'
                         '<img src="data/images/connect_four_started.png"><br>'
                         'The game will end in a draw when the board is full and neither player has connected four tokens.<br><br>'
                         'The image below has an example of a winning board. In this case, the player using the X token won, connecting four tokens diagonally.<br><br>'
                         '<img src="data/images/connect_four_win.png">'
                         '</font>')
        # Disable the button associated with this manual to prevent opening multiple instances
        self.button = button
        self.button.disable()

    def kill(self):
        # When the window is closed, re-enable the button
        self.button.enable()
        super().kill()