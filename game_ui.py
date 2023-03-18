import pygame
import pygame_gui
from tic_tac_toe import TicTacToe

# Need to initialize pygame before doing anything else
pygame.init()

# Create display surface
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HandyGame")

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((width, height), 'data/themes/theme.json')

header_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((150, 25), (500, 100)), text='Welcome to HandyGame!', manager=manager)
tic_tac_toe_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 150), (200, 50)),
                                             text='Play Tic-Tac-Toe',
                                             manager=manager)
exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 250), (200, 50)),
                                             text='Exit Game',
                                             manager=manager)

# Used for locking FPS
clock = pygame.time.Clock()

# Create the object for playing tic tac toe
tic_tac_toe_game = TicTacToe(manager, screen)

playing = True
while playing:
    time_delta = clock.tick(60)/1000.0

    # Support quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if tic_tac_toe_game.playing == False:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == tic_tac_toe_button:
                    tic_tac_toe_button.hide()
                    exit_button.hide()
                    header_text.hide()
                    
                    tic_tac_toe_game.start_game()
                if event.ui_element == exit_button:
                    playing = False
        else:
            tic_tac_toe_game.process_event(event)
            if tic_tac_toe_game.playing == False:
                tic_tac_toe_button.show()
                exit_button.show()
                header_text.show()

        manager.process_events(event)
    
    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()