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

        # set up music
        bg_music = pygame.mixer.Sound('audio/miscWithFinsiher.mp3')
        bg_music.set_volume(0.2)
        bg_music.play(loops = -1)

        return screen, clock

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def setup_game()->None:
    try:
        # Create race surface with width, height
        race_surface = pygame.Surface((1200,700))
        race_surface.fill('White')

        # Set up race surface / background
        player_surfaces_list = []
        player_rectangles_list = []
        
        player_colours_list = ['green', 'purple', 'grey', 'red','white','yellow', 'blue','cyan','orange', 'olive','brown','magenta']
        #player_names_list = ['Tony','Naresh','Pawan','Rajesh','Roopal', 'Bernard']
        player_names_list = ['Bernard','Tony','Naresh','Norman','Pawan','Rajesh','Roopal','Srikar','Stephen','Sudha','Vishaal','Raman']

        # assign colours to players
        players_table_surfaces_list = []
        players_table_rectangles_list = []
        players_name_surfaces_list = []

        player_name_font = pygame.font.SysFont('timesnewroman',  20)

        random.shuffle(player_names_list)

        table_y_position = 10
        for index,colour in enumerate(player_colours_list) :
            # Tried to put color block before name, so for now reduced the color block size to make the text readable
            table_surface = pygame.Surface((20,20))
            table_surface.fill(colour)
            table_rectangle = table_surface.get_rect(center=(1100,table_y_position))
            

            name_surface = player_name_font.render(player_names_list[index], False, (100, 100, 100))


            players_table_surfaces_list.append(table_surface)
            players_table_rectangles_list.append(table_rectangle)
            players_name_surfaces_list.append(name_surface)

            table_y_position += 30

        # generate racers
        player_y_pos = 60
        for colour in player_colours_list :
            player_surface = pygame.Surface((75,38))
            carImage = pygame.image.load("images/"+colour+"-car.png").convert()
            player_surface.blit(carImage,(0,0))
            #player_surface.fill(colour)
            player_rectangle = player_surface.get_rect(center=(10,player_y_pos))

            player_surfaces_list.append(player_surface)
            player_rectangles_list.append(player_rectangle)

            player_y_pos += 50


        # Set up timer
        movement_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(movement_timer, 2000)

        # Caption
        race_font = pygame.font.SysFont('timesnewroman',  20)
        race_finish_surface = race_font.render('FINISH', False, (0, 0, 0))
        race_finish_surface = pygame.transform.rotozoom(race_finish_surface, 270, 2)

        # Winner indicator
        winner_font = pygame.font.SysFont('timesnewroman',  20)
        winner_surface = winner_font.render('W', False, (64, 64, 64))
        winner_rectangle = winner_surface.get_rect()

        return race_surface, race_finish_surface, movement_timer, player_surfaces_list, player_rectangles_list, winner_surface , winner_rectangle , players_table_surfaces_list , players_table_rectangles_list, players_name_surfaces_list

    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{err} on line {exc_tb.tb_lineno}")
        raise err

def game_loop(screen: object, clock: object, movement_timer:object, race_surface: object, race_finish_surface: object, player_surfaces_list:List[object], player_rectangles_list:List[object], winner_surface:object, winner_rectangle:object, players_table_surfaces_list:List[object] , players_table_rectangles_list:List[object], players_name_surfaces_list:List[object])->None:
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
            roadImage = pygame.image.load("images/road-asphalt-highway-street-marking-horizontal-vector-21645745.jpeg").convert()
            #screen.blit(race_surface,(0,0))
            screen.blit(race_surface,(0,0))
            screen.blit(roadImage,(0,0))
            screen.blit(race_finish_surface,(1000,300))
            pygame.draw.line(screen, (0,0,0),(1000,0),(1000,800))

            current_speed = [random.randrange(1,10,1) for _ in range(len(player_surfaces_list))] if race_underway else list(itertools.repeat(0, len(player_surfaces_list)))

            for i in range (len(players_table_surfaces_list)):
                screen.blit(players_table_surfaces_list[i], players_table_rectangles_list[i])
                screen.blit(players_name_surfaces_list[i],(players_table_rectangles_list[i].x, players_table_rectangles_list[i].y))

            for i in range(0,len(player_surfaces_list)):
                if player_rectangles_list[i].x < 925 :
                    player_rectangles_list[i].x += current_speed[i]
                else :
                    winner_rectangle.center = player_rectangles_list[i].center
                    race_underway = False
                
                screen.blit(player_surfaces_list[i], player_rectangles_list[i])
                if (not race_underway):
                    screen.blit(winner_surface, winner_rectangle)

            # Write updates to display surface
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

    race_surface, race_finish_surface, movement_timer, player_surfaces_list, player_rectangles_list , winner_surface , winner_rectangle, players_table_surfaces_list , players_table_rectangles_list, players_name_surfaces_list = setup_game()

    game_loop(screen, clock, movement_timer, race_surface, race_finish_surface, player_surfaces_list, player_rectangles_list, winner_surface , winner_rectangle, players_table_surfaces_list , players_table_rectangles_list, players_name_surfaces_list)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        logger.info(f"{err}")