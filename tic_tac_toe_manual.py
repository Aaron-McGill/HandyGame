import pygame

from pygame_gui.windows import UIMessageWindow

class TicTacToeManual(UIMessageWindow):
    def __init__(self, manager, button):
        super().__init__(rect=pygame.Rect((10, 10), (600, 600)), manager=manager, window_title='Tic-Tac-Toe Manual', object_id='#tic_tac_toe_manual', 
            html_message='<font color=normal_text>'
                         'The goal of the game is to get three tokens of the same type in a row, either horizontally, vertically, or diagonally.<br><br>'
                         'To place a token, click on a square on the board.<br><br>'
                         'The game will end in a draw when the board is full and neither player has connected three tokens.<br><br>'
                         'The image below has an example of a winning board. In this case, the player using the X token won, connecting three tokens diagonally.<br><br>'
                         '<img src="data/images/tic_tac_toe_win.png">'
                         '</font>')
        # Disable the button associated with this manual to prevent opening multiple instances
        self.button = button
        self.button.disable()
    
    def kill(self):
        # When the window is closed, re-enable the button
        self.button.enable()
        super().kill()