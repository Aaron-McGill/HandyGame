import pygame

from pygame_gui.windows import UIMessageWindow

class ConnectFourManual(UIMessageWindow):
    def __init__(self, manager, button):
        super().__init__(rect=pygame.Rect((10, 10), (600, 600)), manager=manager, window_title='Connect Four Manual', object_id='#connect_four_manual', 
            html_message='<font color=normal_text>'
                         'During your turn, a message will appear at the top of the screen prompting you to select a column to drop a token.<br><br>'
                         'To drop a token, click the Select button beneath the column where you want to drop your token.<br><br>'
                         'When a column is full, the Select button beneath that column will be disabled. When it is your opponent\'s turn, all Select buttons will be disabled.<br><br>'
                         'The game will end when either you or your opponent connects four tokens, either horizontally, vertically, or diagonally.<br><br>'
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