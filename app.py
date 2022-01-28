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

        player_surface = pygame.Surface((50,50))
        player_surface.fill('Red')
        player_rect = player_surface.get_rect(center=(10,10))

        return race_surface, player_surface, player_rect
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def game_loop(screen: object, clock: object, race_surface: object, player_surface:object, player_rect:object)->None:
    try:
        while True:
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info(f"Finishing {PGMNAME}")
                    pygame.quit() # Opposite of .init()
 
                    # Ensure pygame ends 
                    exit()

            # blit - Blcok Image Transfer i.e put a regular surface on top of display surface
            screen.blit(race_surface,(0,0))
            screen.blit(player_surface, player_rect)

            # Writeupdates to display surface
            pygame.display.update()

            # Control speed , set maximum frame rate - while loop must not run more than 60 times per second
            clock.tick(60)
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def main()->None:
    logger.info(f"Starting {PGMNAME}")

    screen, clock = setup_pygame()

    race_surface, player_surface, player_rect = setup_game()

    game_loop(screen, clock, race_surface, player_surface, player_rect)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.info(f"{err}")