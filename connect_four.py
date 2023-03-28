import pygame
import pygame_gui

button1_position = (200, 75)
button2_position = (300, 75)
button3_position = (400, 75)
button4_position = (500, 75)
button5_position = (200, 175)
button6_position = (300, 175)
button7_position = (400, 175)
button8_position = (500, 175)
button9_position = (200, 275)
button10_position = (300, 275)
button11_position = (400, 275)
button12_position = (500, 275)
button13_position = (200, 375)
button14_position = (300, 375)
button15_position = (400, 375)
button16_position = (500, 375)

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
        self.player_message_x = "{}'s turn. Select a column to drop an X!".format(self.player_name_x)
        self.player_message_o = "{}'s turn. Select a column to drop an O!".format(self.player_name_o)
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
        self.label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 10), (500, 100)), text=self.player_message_x, manager=self.manager)
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
        self.place_holder_buttons = [
            self.g1,
            self.g2,
            self.g3,
            self.g4,
            self.g5,
            self.g6,
            self.g7,
            self.g8,
            self.g9,
            self.g10,
            self.g11,
            self.g12,
            self.g13,
            self.g14,
            self.g15,
            self.g16
        ]
        for button in self.place_holder_buttons:
            button.disable()
        self.column1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 475), (100, 50)), text = 'Select', manager=self.manager)
        self.column2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 475), (100, 50)), text = 'Select', manager=self.manager)
        self.column3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 475), (100, 50)), text = 'Select', manager=self.manager)
        self.column4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 475), (100, 50)), text = 'Select', manager=self.manager)
        self.column_buttons = [
            self.column1_button,
            self.column2_button,
            self.column3_button,
            self.column4_button
        ]
    
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
            if event.ui_element == self.column1_button:
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
                    self.column1_button.disable()
            if event.ui_element == self.column2_button:
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
                    self.column2_button.disable()
            if event.ui_element == self.column3_button:
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
                    self.column3_button.disable()
            if event.ui_element == self.column4_button:
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
                    self.column3_button.disable()
            
    
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
        if " " not in self.board:
            return True
        else:
            return False
    
    def clear_board(self):
        for button in self.place_holder_buttons:
            if button.visible == 1:
                button.kill()

        for image in self.images:
            image.kill()
        
        self.label.kill()
        self.exit_button.kill()
    
    def handle_game_end(self, new_header):
        for button in self.column_buttons:
            button.kill()
        
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
