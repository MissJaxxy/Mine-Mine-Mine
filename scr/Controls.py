import pygame
import sys

def KeyPressed(player: object) -> None:
    """Checks the event loop for KEY press, and sets player position offsets."""
    offset = int((pygame.display.get_surface().get_width() / 500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    player.y_offset = -offset
            if event.key == pygame.K_RIGHT:
                    player.x_offset = offset
            if event.key == pygame.K_DOWN:
                    player.y_offset = offset
            if event.key == pygame.K_LEFT:
                    player.x_offset = -(offset + 1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                    player.y_offset = 0
            if event.key == pygame.K_RIGHT:
                    player.x_offset = 0
            if event.key == pygame.K_DOWN:
                    player.y_offset = 0
            if event.key == pygame.K_LEFT:
                    player.x_offset = 0
   