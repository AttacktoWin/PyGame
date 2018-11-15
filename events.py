import pygame

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == KEYDOWN and (
                event.key == K_ESCAPE
            )
        ): sys.exit()