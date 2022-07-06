import sys
import pygame
from Controller import Controller
from Button import Button


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

FPS = pygame.time.Clock()

display_width = 1400
display_height = 650
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('InsanePokemons')

controller = Controller(FPS, display)

class Window:
    def __init__(self, text, text_font, text_color, x, y, window_bg, surf):
        self.text = text
        self.buttons = []
        self.text_font = text_font
        self.text_color = text_color
        self.x = x
        self.y = y
        self.window_bg = window_bg
        self.surf = surf

    def append_button(self, button):
        self.buttons.append(button)

    def start(self):
        while True:
            MOUSE_POS = pygame.mouse.get_pos()

            self.surf.blit(self.window_bg, (0, 0))

            TEXT = get_font(self.text_font).render(f'{self.text}', True, self.text_color)
            TEXT_RECT = TEXT.get_rect(center=(self.x, self.y))
            self.surf.blit(TEXT, TEXT_RECT)

            for i in range(len(self.buttons)):
                self.buttons[i].changeColor(MOUSE_POS)
                self.buttons[i].update(self.surf)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].checkForInput(MOUSE_POS):
                            self.buttons[i].click()
            pygame.display.update()

class Menu(Window):
    def __init__(self):
        self.text = "MAIN MENU"
        self.text_font = 100
        self.text_color = "#b68f40"
        self.x = 700
        self.y = 100
        self.window_bg = pygame.image.load("images/backg.jpg")
        self.surf = display
        self.buttons = []

class Options(Window):
    def __init__(self):
        self.text = "Отожмись 10 раз или я заберу твою душу"
        self.text_font = 35
        self.text_color = "white"
        self.x = 700
        self.y = 260
        self.window_bg = pygame.image.load("images/Optionsbg.jpg")
        self.surf = display
        self.buttons = []

MENU = Menu()
OPTIONS = Options()

PLAY_BUTTON = Button(image=pygame.image.load("images/play_rect.png"), pos=(700, 250),
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = controller.run_game)
OPTIONS_BUTTON = Button(image=pygame.image.load("images/options_rect.png"), pos=(700, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = OPTIONS.start)
QUIT_BUTTON = Button(image=pygame.image.load("images/quit_rect.png"), pos=(700, 550),
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White", run_window = pygame.quit)
BACK_BUTTON = Button(image=None, pos=(700, 460),
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", run_window = MENU.start)

MENU.append_button(PLAY_BUTTON)
MENU.append_button(OPTIONS_BUTTON)
MENU.append_button(QUIT_BUTTON)
OPTIONS.append_button(BACK_BUTTON)