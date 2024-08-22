from inspect import getframeinfo, stack


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


class Person:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0

    def move_left(self):
        self.xpos += 1


def person_unit_tester():
    # Initialize an object to test
    p = Person()
    # Feed it initial values, if needed
    p.xpos = 10
    # Test the initial values
    unittest(p.xpos == 10)
    # Call a method
    p.move_left()
    # Test the new state of the object to see if it changed as you expect
    unittest(p.xpos == 11)


person_unit_tester()


# Importing necessary libraries for testing
import pygame
from pygame.locals import *
from tkinter.messagebox import showinfo

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 1000
screen_height = 640

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The best maze game")


# Function to resize image
def resize_image(image_path, size):
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, size)
    return image


# Define classes for game elements
class Player:
    def __init__(self, image_path, initial_position):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 150, 10), self.rect)


class FinishLine:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)


class Game:
    def __init__(self):
        self.bg = resize_image("images/maze.jpg", (1000, 640))
        self.player = Player("images/tacocat.png", (0, 0))
        self.walls = [
            Wall(20, 50, 450, 50),
            Wall(170, 160, 450, 50),
            Wall(100, 400, 450, 50),
            Wall(400, 500, 450, 50),
            Wall(550, 280, 450, 50)
        ]
        self.finish_line = FinishLine(screen_width - 50, screen_height - 50)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.player.move(-5, 0)
        if keys[K_RIGHT]:
            self.player.move(5, 0)
        if keys[K_UP]:
            self.player.move(0, -5)
        if keys[K_DOWN]:
            self.player.move(0, 5)
        return True

    def check_collisions(self):
        for wall in self.walls:
            if self.player.rect.colliderect(wall.rect):
                self.player.rect.move_ip(-self.player.rect.x, -self.player.rect.y)
        if self.player.rect.colliderect(self.finish_line.rect):
            return True
        return False

    def update_screen(self):
        screen.fill((255, 255, 255))
        screen.blit(self.bg, (0, 0))
        self.player.draw(screen)
        for wall in self.walls:
            wall.draw(screen)
        self.finish_line.draw(screen)
        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if self.check_collisions():
                running = False
                showinfo("Winner", "Congratulations! You reached the finish line!")
            self.update_screen()

        pygame.quit()


# Create and run the game
game = Game()
game.run()
