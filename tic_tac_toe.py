import pygame
import pygame_gui

button1_position = (250, 150)
button2_position = (350, 150)
button3_position = (450, 150)
button4_position = (250, 250)
button5_position = (350, 250)
button6_position = (450, 250)
button7_position = (250, 350)
button8_position = (350, 350)
button9_position = (450, 350)

square_size = (100, 100)

x_image = pygame.image.load("data/images/x_symbol.png")
x_image = pygame.transform.scale(x_image, square_size)
o_image = pygame.image.load("data/images/o_symbol.png")
o_image = pygame.transform.scale(o_image, square_size)

class TicTacToe():
    def __init__(self, manager, screen):
        self.manager = manager
        self.screen = screen
        # TODO: Make it so that these names can be passed in.
        self.player_name_x = "Player 1"
        self.player_name_o = "Player 2"
        self.player_message_x = "{}'s turn. Click a square to place an X!".format(self.player_name_x)
        self.player_message_o = "{}'s turn. Click a square to place an O!".format(self.player_name_o)
        self.playing = False
        self.game_completed = False
        self.images = []

    def start_game(self):
        self.playing = True
        self.game_completed = False
        self.board = [" " for i in range(9)]
        self.current_symbol = "X"
        self.draw_board()
    
    def draw_board(self):
        self.label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 25), (500, 100)), text=self.player_message_x, manager=self.manager)
        self.g1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button1_position, square_size), text = '', manager=self.manager)
        self.g2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_position, square_size), text = '', manager=self.manager)
        self.g3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button3_position, square_size), text = '', manager=self.manager)
        self.g4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button4_position, square_size), text = '', manager=self.manager)
        self.g5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button5_position, square_size), text = '', manager=self.manager)
        self.g6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button6_position, square_size), text = '', manager=self.manager)
        self.g7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button7_position, square_size), text = '', manager=self.manager)
        self.g8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button8_position, square_size), text = '', manager=self.manager)
        self.g9 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button9_position, square_size), text = '', manager=self.manager)
    
    def process_event(self, event):
        if self.game_completed:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.exit_button:
                    self.clear_board()
                    self.playing = False
        else:
            self.process_game_event(event)

    def process_game_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.g1:
                self.board[0] = self.current_symbol
                self.update_board(self.g1, button1_position)
            if event.ui_element == self.g2:
                self.board[1] = self.current_symbol
                self.update_board(self.g2, button2_position)
            if event.ui_element == self.g3:
                self.board[2] = self.current_symbol
                self.update_board(self.g3, button3_position)
            if event.ui_element == self.g4:
                self.board[3] = self.current_symbol
                self.update_board(self.g4, button4_position)
            if event.ui_element == self.g5:
                self.board[4] = self.current_symbol
                self.update_board(self.g5, button5_position)
            if event.ui_element == self.g6:
                self.board[5] = self.current_symbol
                self.update_board(self.g6, button6_position)
            if event.ui_element == self.g7:
                self.board[6] = self.current_symbol
                self.update_board(self.g7, button7_position)
            if event.ui_element == self.g8:
                self.board[7] = self.current_symbol
                self.update_board(self.g8, button8_position)
            if event.ui_element == self.g9:
                self.board[8] = self.current_symbol
                self.update_board(self.g9, button9_position)
    
    def is_victory(self, icon):
        if (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon) or \
           (self.board[3] == icon and self.board[4] == icon and self.board[5] == icon) or \
           (self.board[6] == icon and self.board[7] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[3] == icon and self.board[6] == icon) or \
           (self.board[1] == icon and self.board[4] == icon and self.board[7] == icon) or \
           (self.board[2] == icon and self.board[5] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon) or \
           (self.board[2] == icon and self.board[4] == icon and self.board[6] == icon):
            return True
        else:
            return False

    def is_draw(self):
        if " " not in self.board:
            return True
        else:
            return False
    
     # TODO: Is there a cleaner way to remove the board?
    def clear_board(self):
        if self.g1.visible == 1:
            self.g1.kill()
        if self.g2.visible == 1:
            self.g2.kill()
        if self.g3.visible == 1:
            self.g3.kill()
        if self.g4.visible == 1:
            self.g4.kill()
        if self.g5.visible == 1:
            self.g5.kill()
        if self.g6.visible == 1:
            self.g6.kill()
        if self.g7.visible == 1:
            self.g7.kill()
        if self.g8.visible == 1:
            self.g8.kill()
        if self.g9.visible == 1:
            self.g9.kill()

        for image in self.images:
            image.kill()
        
        self.label.kill()
        self.exit_button.kill()
    
    def handle_game_end(self, new_header):
        if self.g1.is_enabled:
            self.g1.disable()
        if self.g2.is_enabled:
            self.g2.disable()
        if self.g3.is_enabled:
            self.g3.disable()
        if self.g4.is_enabled:
            self.g4.disable()
        if self.g5.is_enabled:
            self.g5.disable()
        if self.g6.is_enabled:
            self.g6.disable()
        if self.g7.is_enabled:
            self.g7.disable()
        if self.g8.is_enabled:
            self.g8.disable()
        if self.g9.is_enabled:
            self.g9.disable()
        
        self.label.set_text(new_header)
        self.game_completed = True
        self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 500), (200, 50)),
                                             text='Return to Main Menu',
                                             manager=self.manager)

    def update_board(self, clicked_button, button_position):
        clicked_button.kill()
        if self.current_symbol == "X":
            self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=x_image, manager=self.manager))
        else:
            self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=o_image, manager=self.manager))

        if self.is_victory(self.current_symbol):
            if self.current_symbol == "X":
                self.handle_game_end("{} (X) is the winner!".format(self.player_name_x))
            else:
                self.handle_game_end("{} (O) is the winner!".format(self.player_name_o))
        elif self.is_draw():
            self.handle_game_end("It's a draw!")
        else:
            if self.current_symbol == "X":
                self.current_symbol = "O"
                self.label.set_text(self.player_message_o)
            else:
                self.current_symbol = "X"
                self.label.set_text(self.player_message_x)

