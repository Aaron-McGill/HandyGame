import pygame
import pygame_gui

from tic_tac_toe_manual import TicTacToeManual

button1_position = (250, 150)
button2_position = (350, 150)
button3_position = (450, 150)
button4_position = (250, 250)
button5_position = (350, 250)
button6_position = (450, 250)
button7_position = (250, 350)
button8_position = (350, 350)
button9_position = (450, 350)

button_positions = [
    button1_position,
    button2_position,
    button3_position,
    button4_position,
    button5_position,
    button6_position,
    button7_position,
    button8_position,
    button9_position
]

square_size = (100, 100)

x_image = pygame.image.load("data/images/x_symbol.png")
x_image = pygame.transform.scale(x_image, square_size)
o_image = pygame.image.load("data/images/o_symbol.png")
o_image = pygame.transform.scale(o_image, square_size)

opponents_turn_message = "Waiting for opponent to make a move..."

class TicTacToe():
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
        self.board = [" " for i in range(9)]
        self.images = []
        self.player_name = player_name

        self.loading_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (175, 100), (500, 100)),
                                          text='Looking for a game to join...',
                                          manager=self.manager)

        # Contact the game server to join a session
        game_session_info = self.game_client.join_game('tic-tac-toe', self.player_name)
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
        self.your_turn_message = "{}, it's your turn. Click a square to place an {}!".format(self.player_name, self.symbol)
        if self.created_session:
            self.draw_board(self.your_turn_message, True)
        else:
            self.draw_board(opponents_turn_message, False)
            self.waiting_for_opponent_move = True
    
    def draw_board(self, label_text, enable_buttons):
        self.label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 25), (500, 100)), text=label_text, manager=self.manager)
        self.g1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button1_position, square_size), text = '', manager=self.manager)
        self.g2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button2_position, square_size), text = '', manager=self.manager)
        self.g3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button3_position, square_size), text = '', manager=self.manager)
        self.g4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button4_position, square_size), text = '', manager=self.manager)
        self.g5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button5_position, square_size), text = '', manager=self.manager)
        self.g6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button6_position, square_size), text = '', manager=self.manager)
        self.g7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button7_position, square_size), text = '', manager=self.manager)
        self.g8 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button8_position, square_size), text = '', manager=self.manager)
        self.g9 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button9_position, square_size), text = '', manager=self.manager)
        self.buttons = [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9]
        if not enable_buttons:
            for button in self.buttons:
                button.disable()
        self.manual_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 500), (150, 50)), text = 'View Manual', manager=self.manager)
    
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
        else:
            self.process_game_event(event)

    def process_game_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            for i, button in enumerate(self.buttons):
                if event.ui_element == button:
                    self.board[i] = self.symbol
                    button_position = button_positions[i]
                    self.game_client.make_move(self.game_id, self.board)
                    self.update_board(button, button_position)
            if event.ui_element == self.manual_button:
                TicTacToeManual(self.manager, self.manual_button)
    
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
    
    def clear_board(self):
        for button in self.buttons:
            if button.visible == 1:
                button.kill()

        for image in self.images:
            image.kill()
        
        self.label.kill()
        self.exit_button.kill()
    
    def handle_game_end(self, new_header):
        for button in self.buttons:
            if button.is_enabled:
                button.disable()
        self.manual_button.kill()
        
        self.label.set_text(new_header)
        self.game_completed = True
        self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 500), (200, 50)),
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
            for button in self.buttons:
                if button.visible == 1:
                    button.disable()
            self.label.set_text(opponents_turn_message)
            self.waiting_for_opponent_move = True
     
    def update_interface_from_board(self, updated_board):
        self.waiting_for_opponent_move = False
        self.board = updated_board
        for i, square in enumerate(updated_board):
            if square != " ":
                button = self.buttons[i]
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
            for button in self.buttons:
                if button.visible == 1:
                    button.enable()
            self.label.set_text(self.your_turn_message)

