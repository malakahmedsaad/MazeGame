import pygame, random


class NPC(pygame.sprite.Sprite):
    move_distance = 10
    directions = ["north", "east", "south", "west"]

    def __init__(self, screen_size):
        """
        Represents the Good NPC in the game.

        :param screen_size: size of the window, for ensuring the NPC stays on screen
        """
        print("Spawning NPC")
        self.screen_size = screen_size
        super().__init__()
        self.surf = pygame.image.load('images/tacocat.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//4, self.screen_size[1]//4)
        self.path = random.choice(self.directions)
        self.position = [0,0]

    def get_direction(self):
        """
        Keeps the NPC on the screen.

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top <= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"
        elif random.random() > .95:
            self.path = random.choice(self.directions)

    def movement(self):
        """
        Moves the NPC around.

        :return: None
        """
        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance

        self.get_direction()