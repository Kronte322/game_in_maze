import pygame
import pygame_gui
import src.front.ui
from src.back.constants import *


class Ui:
    def __init__(self):
        """initialize in-game user interface"""

        self.manager = pygame_gui.UIManager(SIZE_OF_DISPLAY)
        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PLACE_OF_SETTINGS_BUTTON, SIZE_OF_SETTINGS_BUTTON),
            text='Menu',
            manager=self.manager)

        self.show_answer_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PLACE_OF_SHOW_ANSWER_BUTTON, SIZE_OF_SHOW_ANSWER_BUTTON),
            text='Show Answer',
            manager=self.manager)

    def ProcessEvents(self, event, mappa):
        """this function processing events for UI"""

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            src.front.ui.InGameMenu()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.settings_button:
                src.front.ui.InGameMenu()
            if event.ui_element == self.show_answer_button:
                mappa.ShowAnswer()

        self.manager.process_events(event)

    def Blit(self, time_delta, screen):
        """function for blit UI on screen"""

        self.manager.draw_ui(screen)
        self.manager.update(time_delta)
