"""File contains player class"""

from src.back.constants import *
import pygame


class Player:
    def __init__(self):
        """initialize player"""

        self.speed = SPEED_OF_CHARACTER
        self.side = 'right'

        self.hit_box = pygame.Rect((SPAWN_POSITION[0], SPAWN_POSITION[1]), (SIZE_OF_CHARACTER, SIZE_OF_CHARACTER))
        self.moveBox = (
            SIZE_OF_DISPLAY[0] // 2 - SIZE_OF_MOVE_BOX[0] // 2, SIZE_OF_DISPLAY[1] // 2 - SIZE_OF_MOVE_BOX[1] //
            2, SIZE_OF_DISPLAY[0] // 2 + SIZE_OF_MOVE_BOX[0] // 2,
            SIZE_OF_DISPLAY[1] // 2 + SIZE_OF_MOVE_BOX[1] // 2)

        self.image = pygame.Surface(
            (SIZE_OF_CHARACTER, SIZE_OF_CHARACTER), flags=pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image_of_character = pygame.image.load(PATH_TO_CHARACTER_PNG)
        self.image_of_character = pygame.transform.scale(
            self.image_of_character, (SIZE_OF_CHARACTER, SIZE_OF_CHARACTER))

        self.image.blit(self.image_of_character, (0, 0))

    def GetPosition(self):
        """that function gives position of player on the screen"""

        return [self.hit_box.x + SIZE_OF_CHARACTER // 2, self.hit_box.y + SIZE_OF_CHARACTER]

    def move(self, mappa):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if mappa.CanStandThere(
                    (
                            self.hit_box.x,
                            self.hit_box.y + SIZE_OF_CHARACTER - self.speed - 8)):
                if mappa.CanStandThere((self.hit_box.x + SIZE_OF_CHARACTER,
                                        self.hit_box.y + SIZE_OF_CHARACTER - self.speed - 8)):
                    self.hit_box.y -= self.speed
        if key[pygame.K_a]:
            if self.side == 'right':
                self.side = 'left'
                self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            if mappa.CanStandThere(
                    (self.hit_box.x - self.speed, self.hit_box.y + SIZE_OF_CHARACTER)):
                self.hit_box.x -= self.speed
        if key[pygame.K_s]:
            if mappa.CanStandThere(
                    (self.hit_box.x, self.hit_box.y + SIZE_OF_CHARACTER + self.speed)):
                if mappa.CanStandThere((self.hit_box.x + SIZE_OF_CHARACTER,
                                        self.hit_box.y + SIZE_OF_CHARACTER + self.speed)):
                    self.hit_box.y += self.speed
        if key[pygame.K_d]:
            if self.side == 'left':
                self.side = 'right'
                self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
            if mappa.CanStandThere(
                    (self.hit_box.x + SIZE_OF_CHARACTER + self.speed,
                     self.hit_box.y + SIZE_OF_CHARACTER)):
                self.hit_box.x += self.speed
        if self.hit_box.x <= self.moveBox[0]:
            self.hit_box.x += self.speed
            mappa.MoveMap([self.speed, 0])
        elif self.hit_box.x >= self.moveBox[2] - SIZE_OF_CHARACTER:
            self.hit_box.x -= self.speed
            mappa.MoveMap([-self.speed, 0])
        if self.hit_box.y <= self.moveBox[1]:
            self.hit_box.y += self.speed
            mappa.MoveMap([0, self.speed])
        elif self.hit_box.y >= self.moveBox[3] - SIZE_OF_CHARACTER:
            self.hit_box.y -= self.speed
            mappa.MoveMap([0, -self.speed])

    def render(self, screen):
        """draw player on the screen"""

        screen.blit(self.image, (self.hit_box.x, self.hit_box.y))
