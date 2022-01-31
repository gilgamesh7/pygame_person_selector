import pygame

import sys
import logging

# Instantiate logging
PGMNAME = "selector"
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger(PGMNAME)

def setup_pygame():
    try:
        pygame.init()

        # create display surface - width,height
        screen = pygame.display.set_mode((1200,600))
        # Set window title
        pygame.display.set_caption(PGMNAME)
        # create clock for controlling fps
        clock = pygame.time.Clock()

        return screen, clock

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def setup_game()->None:
    try:
        # Create race surface with width, height
        race_surface = pygame.Surface((1200,600))
        race_surface.fill('Green')

        # Set up race surface / background
        player_surface = pygame.Surface((50,50))
        player_surface.fill('Red')
        player_rect = player_surface.get_rect(center=(10,10))

        # Set up timer
        movement_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(movement_timer, 2000)

        # Caption
        game_font = pygame.font.SysFont('timesnewroman',  50)
        race_finish_surface = game_font.render('FINISH', False, (64, 64, 64))
        race_finish_surface = pygame.transform.rotozoom(race_finish_surface, 270, 3)


        return race_surface, race_finish_surface, movement_timer, player_surface, player_rect
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def game_loop(screen: object, clock: object, movement_timer:object, race_surface: object, race_finish_surface: object, player_surface:object, player_rect:object)->None:
    try:
        player_x_pos = 0
        while True:
            print(player_x_pos)
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info(f"Finishing {PGMNAME}")
                    pygame.quit() # Opposite of .init()
 
                    # Ensure pygame ends 
                    exit()

            # if event.type == movement_timer:
            if player_rect.x < 950 :
                player_x_pos += 1
                player_rect.x += player_x_pos

            # blit - Blcok Image Transfer i.e put a regular surface on top of display surface
            screen.blit(race_surface,(0,0))
            screen.blit(race_finish_surface,(1000,50))
            screen.blit(player_surface, player_rect)

            # Writeupdates to display surface
            pygame.display.update()

            # Control speed , set maximum frame rate - while loop must not run more than 60 times per second
            clock.tick(10)
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def main()->None:
    logger.info(f"Starting {PGMNAME}")

    screen, clock = setup_pygame()

    race_surface, race_finish_surface, movement_timer, player_surface, player_rect = setup_game()

    game_loop(screen, clock, movement_timer, race_surface, race_finish_surface, player_surface, player_rect)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.info(f"{err}")