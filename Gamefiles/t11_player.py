import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning player")
        self.surf = pygame.image.load('tuna.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)


    def movement(self, keys):
        """
        Handles up, down, left, right movement events from the user

        :param keys: key presses from pygame event listener

        :return: None
        """
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -3)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 3)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(3, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-3, 0)


