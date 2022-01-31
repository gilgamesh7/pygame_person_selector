import pygame

import sys
import logging

from typing import List
import random
import itertools

# Instantiate logging
PGMNAME = "selector"
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger(PGMNAME)

def setup_pygame():
    try:
        pygame.init()

        # create display surface - width,height
        screen = pygame.display.set_mode((1200,700))
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
        race_surface = pygame.Surface((1200,700))
        race_surface.fill('Green')

        # Set up race surface / background
        player_surfaces_list = []
        player_rectangles_list = []
        player_colours_list = ['Red', 'Black', 'Orange', 'Purple','Yellow','Magenta','Gray','Cyan','White','Violet','Olive','Brown']
        player_names = ['Bernard','Tony','Naresh','Norman','Pawan','Rajesh','Roopal','Srikar','Stephen','Sudha','Vishaal','Raman']

        player_y_pos = 15
        for colour in player_colours_list :
            player_surface = pygame.Surface((50,50))
            player_surface.fill(colour)
            player_rectangle = player_surface.get_rect(center=(10,player_y_pos))

            player_surfaces_list.append(player_surface)
            player_rectangles_list.append(player_rectangle)

            player_y_pos += 60


        # Set up timer
        movement_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(movement_timer, 2000)

        # Caption
        game_font = pygame.font.SysFont('timesnewroman',  20)
        race_finish_surface = game_font.render('FINISH', False, (0, 0, 0))
        race_finish_surface = pygame.transform.rotozoom(race_finish_surface, 270, 2)

        winner_font = pygame.font.SysFont('timesnewroman',  20)
        winner_surface = winner_font.render('W', False, (64, 64, 64))
        winner_rectangle = winner_surface.get_rect()

        return race_surface, race_finish_surface, movement_timer, player_surfaces_list, player_rectangles_list, winner_surface , winner_rectangle

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def game_loop(screen: object, clock: object, movement_timer:object, race_surface: object, race_finish_surface: object, player_surfaces_list:List[object], player_rectangles_list:List[object], winner_surface:object, winner_rectangle:object)->None:
    try:
        race_underway = True
        while True:
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info(f"Finishing {PGMNAME}")
                    pygame.quit() # Opposite of .init()
 
                    # Ensure pygame ends 
                    exit()

            # blit - Block Image Transfer i.e put a regular surface on top of display surface
            screen.blit(race_surface,(0,0))
            screen.blit(race_finish_surface,(1000,300))
            pygame.draw.line(screen, (0,0,0),(1000,0),(1000,800))

            current_speed = [random.randrange(1,10,1) for _ in range(len(player_surfaces_list))] if race_underway else list(itertools.repeat(0, len(player_surfaces_list)))

            for i in range(0,len(player_surfaces_list)):
                if player_rectangles_list[i].x < 950 :
                    player_rectangles_list[i].x += current_speed[i]
                else :
                    # winner_name_rectangle.x = player_rectangles_list[i].x
                    # winner_name_rectangle.y = player_rectangles_list[i].y
                    winner_rectangle.center = player_rectangles_list[i].center
                    race_underway = False
                
                screen.blit(player_surfaces_list[i], player_rectangles_list[i])
                if (not race_underway):
                    screen.blit(winner_surface, winner_rectangle)

            # Write updates to display surface
            pygame.display.update()

            # Control speed , set maximum frame rate - while loop must not run more than 60 times per second
            clock.tick(40)
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def main()->None:
    logger.info(f"Starting {PGMNAME}")

    screen, clock = setup_pygame()

    race_surface, race_finish_surface, movement_timer, player_surfaces_list, player_rectangles_list , winner_surface , winner_rectangle= setup_game()

    game_loop(screen, clock, movement_timer, race_surface, race_finish_surface, player_surfaces_list, player_rectangles_list, winner_surface , winner_rectangle)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.info(f"{err}")