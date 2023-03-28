import pygame
import pygame_gui

button1_position = (250, 150)
button2_position = (350, 150)
button3_position = (450, 150)
button4_position = (550, 150)
button5_position = (250, 250)
button6_position = (350, 250)
button7_position = (450, 250)
button8_position = (550, 250)
button9_position = (250, 350)
button10_position = (350, 350)
button11_position = (450, 350)
button12_position = (550, 350)
button13_position = (250, 450)
button14_position = (350, 450)
button15_position = (450, 450)
button16_position = (550, 450)

square_size = (100, 100)

x_image = pygame.image.load("data/images/x_symbol.png")
x_image = pygame.transform.scale(x_image, square_size)
o_image = pygame.image.load("data/images/o_symbol.png")
o_image = pygame.transform.scale(o_image, square_size)

class ConnectFour():
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

    def start_game(self):
        self.playing = True
        self.game_completed = False
        self.board = [" " for i in range(16)]
        self.current_symbol = "X"
        self.images = []
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
        self.g10 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button10_position, square_size), text = '', manager=self.manager)
        self.g11 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button11_position, square_size), text = '', manager=self.manager)
        self.g12 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button12_position, square_size), text = '', manager=self.manager)
        self.g13 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button13_position, square_size), text = '', manager=self.manager)
        self.g14 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button14_position, square_size), text = '', manager=self.manager)
        self.g15 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button15_position, square_size), text = '', manager=self.manager)
        self.g16 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button16_position, square_size), text = '', manager=self.manager)
    
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
            if event.ui_element in [self.g1 or self.g5 or self.g9 or self.g13]:
                if self.board[12] == " ":
                    self.board[12] = self.current_symbol
                    self.update_board(self.g13, button13_position)
                elif self.board[8] == " ":
                    self.board[8] = self.current_symbol
                    self.update_board(self.g9, button9_position)
                elif self.board[4] == " ":
                    self.board[4] = self.current_symbol
                    self.update_board(self.g5, button5_position)
                elif self.board[0] == " ":
                    self.board[0] = self.current_symbol
                    self.update_board(self.g1, button1_position)
            if event.ui_element in [self.g2 or self.g6 or self.g10 or self.g14]:
                if self.board[13] == " ":
                    self.board[13] = self.current_symbol
                    self.update_board(self.g14, button14_position)
                elif self.board[9] == " ":
                    self.board[9] = self.current_symbol
                    self.update_board(self.g10, button10_position)
                elif self.board[5] == " ":
                    self.board[5] = self.current_symbol
                    self.update_board(self.g6, button6_position)
                elif self.board[1] == " ":
                    self.board[1] = self.current_symbol
                    self.update_board(self.g2, button2_position)
            if event.ui_element in [self.g3 or self.g7 or self.g11 or self.g15]:
                if self.board[14] == " ":
                    self.board[14] = self.current_symbol
                    self.update_board(self.g15, button15_position)
                elif self.board[10] == " ":
                    self.board[10] = self.current_symbol
                    self.update_board(self.g11, button11_position)
                elif self.board[6] == " ":
                    self.board[6] = self.current_symbol
                    self.update_board(self.g7, button7_position)
                elif self.board[2] == " ":
                    self.board[2] = self.current_symbol
                    self.update_board(self.g3, button3_position)
            if event.ui_element in [self.g4 or self.g8 or self.g12 or self.g16]:
                if self.board[15] == " ":
                    self.board[15] = self.current_symbol
                    self.update_board(self.g16, button16_position)
                elif self.board[11] == " ":
                    self.board[11] = self.current_symbol
                    self.update_board(self.g12, button12_position)
                elif self.board[7] == " ":
                    self.board[7] = self.current_symbol
                    self.update_board(self.g8, button8_position)
                elif self.board[3] == " ":
                    self.board[3] = self.current_symbol
                    self.update_board(self.g4, button4_position)
            
    
    def is_victory(self, icon):
        if  (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon and self.board[3] == icon) or \
            (self.board[4] == icon and self.board[5] == icon and self.board[6] == icon and self.board[7] == icon) or \
            (self.board[8] == icon and self.board[9] == icon and self.board[10] == icon and self.board[11] == icon) or \
            (self.board[12] == icon and self.board[13] == icon and self.board[14] == icon and self.board[15] == icon) or \
            (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon and self.board[12] == icon) or \
            (self.board[1] == icon and self.board[5] == icon and self.board[9] == icon and self.board[13] == icon) or \
            (self.board[2] == icon and self.board[6] == icon and self.board[10] == icon and self.board[14] == icon) or \
            (self.board[3] == icon and self.board[7] == icon and self.board[11] == icon and self.board[15] == icon) or \
            (self.board[0] == icon and self.board[5] == icon and self.board[10] == icon and self.board[15] == icon) or \
            (self.board[3] == icon and self.board[6] == icon and self.board[9] == icon and self.board[12] == icon):
            return True
        else:
            return False

    def is_draw(self):
        print("Draw?")
        for idx, square in enumerate(self.board):
            print(str(idx) + ":" + square)
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
        if self.g10.visible == 1:
            self.g10.kill()
        if self.g11.visible == 1:
            self.g11.kill()
        if self.g12.visible == 1:
            self.g12.kill()
        if self.g13.visible == 1:
            self.g13.kill()
        if self.g14.visible == 1:
            self.g14.kill()
        if self.g15.visible == 1:
            self.g15.kill()
        if self.g16.visible == 1:
            self.g16.kill()

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
        if self.g10.is_enabled:
            self.g10.disable()
        if self.g11.is_enabled:
            self.g11.disable()
        if self.g12.is_enabled:
            self.g12.disable()
        if self.g13.is_enabled:
            self.g13.disable()
        if self.g14.is_enabled:
            self.g14.disable()
        if self.g15.is_enabled:
            self.g15.disable()
        if self.g16.is_enabled:
            self.g16.disable()
        
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
