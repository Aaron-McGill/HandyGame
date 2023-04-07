import os
import time
import pygame
import pygame_gui
from tic_tac_toe import TicTacToe
from connect_four import ConnectFour
from game_client import Client
from connect_four_manual import ConnectFourManual
from tic_tac_toe_manual import TicTacToeManual

# Need to initialize pygame before doing anything else
pygame.init()

# Create display surface
width = 800
height = 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HandyGame")

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((width, height), 'data/themes/theme.json')

# Start menu UI elements
header_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (150, 25), (500, 100)),
                                          text='Welcome to HandyGame!',
                                          manager=manager, visible=0)
tic_tac_toe_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (50, 125), (250, 50)),
                                                  text='Play Tic-Tac-Toe',
                                                  manager=manager, visible=0)
connect_four_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 225), (250, 50)),
                                          text='Play Connect Four',
                                          manager=manager, visible=0)

connect_four_manual_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 325), (250, 50)),
                                          text='View Connect Four Manual',
                                          manager=manager, visible=0)

tic_tac_toe_manual_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 425), (250, 50)),
                                          text='View Tic-Tac-Toe Manual',
                                          manager=manager, visible=0)

exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (50, 525), (250, 50)),
                                           text='Exit Game',
                                           manager=manager, visible=0)

# Name prompt elements
name_prompt = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (175, 100), (500, 100)),
                                          text='Please enter your name:',
                                          manager=manager)

name_text_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
    (275, 200), (300, 50)),
                                          manager=manager)

submit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (325, 300), (200, 50)),
                                           text='Submit',
                                           manager=manager)

# Used for locking FPS
clock = pygame.time.Clock()

# Set up REST client for interacting with server
# If a value is not provided for the host, just fall
# back to server hosted in cloud
host = os.environ.get('SERVER_HOST', 'https://handygame.onrender.com')
game_client = Client(host)

# Create the object for playing tic tac toe and connect four
tic_tac_toe_game = TicTacToe(manager, screen, game_client)
connect_four_game = ConnectFour(manager, screen, game_client)

global player_name

def hide_start_menu():
    tic_tac_toe_button.hide()
    connect_four_button.hide()
    connect_four_manual_button.hide()
    tic_tac_toe_manual_button.hide()
    exit_button.hide()
    header_text.hide()

def show_start_menu():
    tic_tac_toe_button.show()
    connect_four_button.show()
    connect_four_manual_button.show()
    tic_tac_toe_manual_button.show()
    exit_button.show()
    header_text.show()

playing = True
while playing:
    time_delta = clock.tick(30) / 1000.0

    if tic_tac_toe_game.waiting_to_join_game:
        if game_client.is_game_ready(tic_tac_toe_game.game_id):
            tic_tac_toe_game.waiting_to_join_game = False
            tic_tac_toe_game.initialize_game_board()
        else:
            time.sleep(0.5)
    
    if tic_tac_toe_game.waiting_for_opponent_move:
        if game_client.is_my_turn(tic_tac_toe_game.game_id, tic_tac_toe_game.player_id):
            tic_tac_toe_game.waiting_for_opponent_move = False
            response = game_client.get_game(tic_tac_toe_game.game_id)
            tic_tac_toe_game.update_interface_from_board(response.json()['board'])
        else:
            time.sleep(0.5)
    
    if connect_four_game.waiting_to_join_game:
        if game_client.is_game_ready(connect_four_game.game_id):
            connect_four_game.waiting_to_join_game = False
            connect_four_game.initialize_game_board()
        else:
            time.sleep(0.5)
    
    if connect_four_game.waiting_for_opponent_move:
        if game_client.is_my_turn(connect_four_game.game_id, connect_four_game.player_id):
            connect_four_game.waiting_for_opponent_move = False
            response = game_client.get_game(connect_four_game.game_id)
            connect_four_game.update_interface_from_board(response.json()['board'])
        else:
            time.sleep(0.5)

    # Support quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            # If we're waiting on someone to join our game session and then exit the app,
            # delete the game session we created.
            if connect_four_game.waiting_to_join_game and connect_four_game.created_session:
                game_client.delete_game(connect_four_game.game_id)
            if tic_tac_toe_game.waiting_to_join_game and tic_tac_toe_game.created_session:
                game_client.delete_game(tic_tac_toe_game.game_id)

        # Handle getting user name from initial screen
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == submit_button and name_text_box.get_text().strip() != "":
                player_name = name_text_box.get_text().strip()
                name_prompt.kill()
                name_text_box.kill()
                submit_button.kill()
                header_text.set_text(player_name + ', welcome to HandyGame!')
                show_start_menu()

        if tic_tac_toe_game.playing == False:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tic_tac_toe_button:
                    hide_start_menu()

                    tic_tac_toe_game.start_game(player_name)
                if event.ui_element == exit_button:
                    playing = False
                
        else:
            tic_tac_toe_game.process_event(event)
            if tic_tac_toe_game.playing == False:
                show_start_menu()
            
        if connect_four_game.playing == False:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == connect_four_button:
                    hide_start_menu()

                    connect_four_game.start_game(player_name)
                if event.ui_element == exit_button:
                    playing = False
        else:
            connect_four_game.process_event(event)
            if connect_four_game.playing == False:
                show_start_menu()
        
        # Display Connect Four manual
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == connect_four_manual_button:
                ConnectFourManual(manager, connect_four_manual_button)
        
        # Display Tic-Tac-Toe manual
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == tic_tac_toe_manual_button:
                TicTacToeManual(manager, tic_tac_toe_manual_button)

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
