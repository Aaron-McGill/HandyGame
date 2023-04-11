import pygame
import pygame_gui

from connect_four_manual import ConnectFourManual

button1_position = (200, 100)
button2_position = (300, 100)
button3_position = (400, 100)
button4_position = (500, 100)
button5_position = (200, 200)
button6_position = (300, 200)
button7_position = (400, 200)
button8_position = (500, 200)
button9_position = (200, 300)
button10_position = (300, 300)
button11_position = (400, 300)
button12_position = (500, 300)
button13_position = (200, 400)
button14_position = (300, 400)
button15_position = (400, 400)
button16_position = (500, 400)

button_positions = [
    button1_position,
    button2_position,
    button3_position,
    button4_position,
    button5_position,
    button6_position,
    button7_position,
    button8_position,
    button9_position,
    button10_position,
    button11_position,
    button12_position,
    button13_position,
    button14_position,
    button15_position,
    button16_position,
]

square_size = (100, 100)

x_image = pygame.image.load("data/images/x_symbol.png")
x_image = pygame.transform.scale(x_image, square_size)
o_image = pygame.image.load("data/images/o_symbol.png")
o_image = pygame.transform.scale(o_image, square_size)

opponents_turn_message = "Waiting for opponent to make a move..."

class ConnectFour():
    def __init__(self, manager, screen, game_client):
        self.manager = manager
        self.screen = screen
        self.playing = False
        self.game_completed = False
        self.game_client = game_client
        self.waiting_to_join_game = False
        self.waiting_for_opponent_move = False

    def start_game(self, player_name):
        self.playing = True
        self.game_completed = False
        self.board = [" " for i in range(16)]
        self.images = []
        self.player_name = player_name
        self.column1_full = False
        self.column2_full = False
        self.column3_full = False
        self.column4_full = False

        self.loading_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (175, 100), (500, 100)),
                                          text='Looking for a game to join...',
                                          manager=self.manager)
        game_session_info = self.game_client.join_game('connectFour', self.player_name)
        self.game_id = game_session_info['game_id']
        self.created_session = game_session_info['created']
        self.waiting_to_join_game = game_session_info['waiting']
        self.player_id = game_session_info["player_id"]

        if self.waiting_to_join_game == False:
            self.initialize_game_board()                                  
    
    def initialize_game_board(self):
        self.loading_label.kill()

        if self.created_session:
            self.symbol = "X"
            self.opponent_symbol = "O"
        else:
            self.symbol = "O"
            self.opponent_symbol = "X"
        self.your_turn_message = "{}, it's your turn. Select a column to drop an {}!".format(self.player_name, self.symbol)
        if self.created_session:
            self.draw_board(self.your_turn_message, True)
        else:
            self.draw_board(opponents_turn_message, False)
            self.waiting_for_opponent_move = True

    def draw_board(self, label_text, enable_buttons):
        self.label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 10), (500, 100)), text=label_text, manager=self.manager)
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
        self.column1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 500), (100, 50)), text = 'Select', manager=self.manager)
        self.column2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 500), (100, 50)), text = 'Select', manager=self.manager)
        self.column3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 500), (100, 50)), text = 'Select', manager=self.manager)
        self.column4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 500), (100, 50)), text = 'Select', manager=self.manager)
        self.column_buttons = [
            self.column1_button,
            self.column2_button,
            self.column3_button,
            self.column4_button
        ]
        if not enable_buttons:
            for button in self.column_buttons:
                button.disable()
        self.manual_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 575), (150, 50)), text = 'View Manual', manager=self.manager)
    
    def process_event(self, event):
        if self.game_completed:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.exit_button:
                    self.clear_board()
                    # If we created the session, we're responsible
                    # for cleaning it up as well.
                    if self.created_session == True:
                        self.game_client.delete_game(self.game_id)
                    self.playing = False
                    self.playing = False
        else:
            self.process_game_event(event)

    def process_game_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.column1_button:
                if self.board[12] == " ":
                    self.handle_board_change_for_index(12)
                elif self.board[8] == " ":
                    self.handle_board_change_for_index(8)
                elif self.board[4] == " ":
                    self.handle_board_change_for_index(4)
                elif self.board[0] == " ":
                    self.handle_board_change_for_index(0)
                    self.column1_button.disable()
                    self.column1_full = True
            if event.ui_element == self.column2_button:
                if self.board[13] == " ":
                    self.handle_board_change_for_index(13)
                elif self.board[9] == " ":
                    self.handle_board_change_for_index(9)
                elif self.board[5] == " ":
                    self.handle_board_change_for_index(5)
                elif self.board[1] == " ":
                    self.handle_board_change_for_index(1)
                    self.column2_button.disable()
                    self.column2_full = True
            if event.ui_element == self.column3_button:
                if self.board[14] == " ":
                    self.handle_board_change_for_index(14)
                elif self.board[10] == " ":
                    self.handle_board_change_for_index(10)
                elif self.board[6] == " ":
                    self.handle_board_change_for_index(6)
                elif self.board[2] == " ":
                    self.handle_board_change_for_index(2)
                    self.column3_button.disable()
                    self.column3_full = True
            if event.ui_element == self.column4_button:
                if self.board[15] == " ":
                    self.handle_board_change_for_index(15)
                elif self.board[11] == " ":
                    self.handle_board_change_for_index(11)
                elif self.board[7] == " ":
                    self.handle_board_change_for_index(7)
                elif self.board[3] == " ":
                    self.handle_board_change_for_index(3)
                    self.column4_button.disable()
                    self.column4_full = True
            if event.ui_element == self.manual_button:
                ConnectFourManual(self.manager, self.manual_button)

    def handle_board_change_for_index(self, index):
        self.board[index] = self.symbol
        self.game_client.make_move(self.game_id, self.board)
        button_position = button_positions[index]
        button = self.place_holder_buttons[index]
        self.update_board(button, button_position)
            
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
        self.manual_button.kill()
        
        self.label.set_text(new_header)
        self.game_completed = True
        self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 550), (200, 50)),
                                             text='Return to Main Menu',
                                             manager=self.manager)

    def update_board(self, clicked_button, button_position):
        clicked_button.kill()
        if self.symbol == "X":
            self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=x_image, manager=self.manager))
        else:
            self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=o_image, manager=self.manager))

        if self.is_victory(self.symbol):
            self.handle_game_end("Congratulations {}, you win!".format(self.player_name))
        elif self.is_draw():
            self.handle_game_end("It's a draw!")
        else:
            if self.column1_button.visible == 1 and not self.column1_full:
                self.column1_button.disable()
            if self.column2_button.visible == 1 and not self.column2_full:
                self.column2_button.disable()
            if self.column3_button.visible == 1 and not self.column3_full:
                self.column3_button.disable()
            if self.column4_button.visible == 1 and not self.column4_full:
                self.column4_button.disable()
            self.label.set_text(opponents_turn_message)
            self.waiting_for_opponent_move = True
    
    def update_interface_from_board(self, updated_board):
        self.waiting_for_opponent_move = False
        self.board = updated_board

        # Check if the select buttons need to be disabled because the user filled up a column
        if not self.column1_full and self.board[12] != " " and self.board[8] != " " and self.board[4] != " " and self.board[0] != " ":
            self.column1_full = True
        if not self.column2_full and self.board[13] != " " and self.board[9] != " " and self.board[5] != " " and self.board[1] != " ":
            self.column2_full = True
        if not self.column3_full and self.board[14] != " " and self.board[10] != " " and self.board[6] != " " and self.board[2] != " ":
            self.column3_full = True
        if not self.column4_full and self.board[15] != " " and self.board[11] != " " and self.board[7] != " " and self.board[3] != " ":
            self.column4_full = True

        for i, square in enumerate(updated_board):
            if square != " ":
                button = self.place_holder_buttons[i]
                # The button's still there even though there's a symbol at that
                # position on the board. Remove the button and add an image at
                # its location.
                if button.visible == 1:
                    button_position = button_positions[i]
                    button.kill()
                    if square == "X":
                        self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=x_image, manager=self.manager))
                    else:
                        self.images.append(pygame_gui.elements.UIImage(relative_rect=pygame.Rect(button_position, square_size), image_surface=o_image, manager=self.manager))
        if self.is_victory(self.opponent_symbol):
            self.handle_game_end("You lose!")
        elif self.is_draw():
            self.handle_game_end("It's a draw!")
        else:
            if self.column1_button.visible == 1 and not self.column1_full:
                self.column1_button.enable()
            if self.column2_button.visible == 1 and not self.column2_full:
                self.column2_button.enable()
            if self.column3_button.visible == 1 and not self.column3_full:
                self.column3_button.enable()
            if self.column4_button.visible == 1 and not self.column4_full:
                self.column4_button.enable()
            self.label.set_text(self.your_turn_message)
