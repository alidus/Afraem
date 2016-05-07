import math, pygame
import threading


class ColoursPack:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)


colours = ColoursPack()


class AList:
    def __init__(self, x=0, y=0, width=100, height=300, element_id='a_list', background=colours.white,
                 text_colour=colours.black, centered_elements=False, text_size=20, bold=False, italic=False, shading=100, thikness=0,
                 edge_colour=colours.black):
        self.list_box = pygame.Rect(x, y, width, height)
        self.element_id = element_id
        self.background = background
        self.shading = shading
        self.thikness = thikness
        self.edge_colour = edge_colour
        self.text_size = text_size
        self.centered = centered_elements
        self.text_colour = text_colour
        self.list_surface = pygame.Surface((width, height)).convert()
        self.list_surface.set_alpha(255)
        self.bold_italic = (bold, italic)
        if isinstance(self.background, tuple):
            self.list_surface.fill(self.background)
        else:
            pygame.transform.scale(self.background, self.button_box)
            self.list_surface.blit(self.background, (0, 0))
        self.list_of_items = []

    def add(self, element):
        number_of_element = len(self.list_of_items)
        if not self.centered:
            element_label = AText(element, self.list_box.x + self.thikness, number_of_element*self.text_size, self.text_size,
                                  element_id=self.element_id+';'+str(number_of_element), colour=self.text_colour,
                                  bold=self.bold_italic[0], italic=self.bold_italic[1])
        else:
            element_label = AText(element, self.list_box.x + self.list_box.width/2,
                                  number_of_element * self.text_size + self.text_size/2, self.text_size,
                                  element_id=self.element_id + ';' + str(number_of_element), colour=self.text_colour,
                                  bold=self.bold_italic[0], italic=self.bold_italic[1], centered=True)
        self.list_of_items.append(element_label)

    def draw(self, surface):
        surface.blit(self.list_surface, self.list_box)
        if self.thikness > 0:
            pygame.draw.line(surface, self.edge_colour, (self.list_box.x, self.list_box.y),
                             (self.list_box.x + self.list_box.width, self.list_box.y), self.thikness)
            pygame.draw.line(surface, self.edge_colour, (self.list_box.x + self.list_box.width, self.list_box.y),
                             (self.list_box.x + self.list_box.width, self.list_box.y + self.list_box.height),
                             self.thikness)
            pygame.draw.line(surface, self.edge_colour, (self.list_box.x, self.list_box.y),
                             (self.list_box.x, self.list_box.y + self.list_box.height),
                             self.thikness)
            pygame.draw.line(surface, self.edge_colour, (self.list_box.x, self.list_box.y + self.list_box.height),
                             (self.list_box.x + self.list_box.width, self.list_box.y + self.list_box.height),
                             self.thikness)
        for element in self.list_of_items:
            element.draw(surface)
        if self.thikness > 0:
            for element in self.list_of_items:
                element_bot_y = self.list_box.y + self.text_size*(1 + self.list_of_items.index(element))
                pygame.draw.line(surface, self.edge_colour, (self.list_box.x, element_bot_y),
                                 (self.list_box.x + self.list_box.width, element_bot_y), self.thikness)

class AButton:
    def __init__(self, x=0, y=0, width=100, height=20, element_id='a_button', background=colours.white,
                 text_colour=colours.black, text='', text_size=20, bold=False, italic=False, shading=100):
        self.button_box = pygame.Rect(x, y, width, height)
        self.element_id = element_id
        self.background = background
        self.shading = shading
        self.text_colour = text_colour
        self.button_surface = pygame.Surface((width, height)).convert()
        self.button_surface.set_alpha(255)
        if isinstance(self.background, tuple):
            self.button_surface.fill(self.background)
        else:
            pygame.transform.scale(self.background, self.button_box)
            self.button_surface.blit(self.background, (0, 0))
        self.button_text = AText(text, centered=True, x=self.button_box.centerx, y=self.button_box.centery,
                                 size=text_size, bold=bold, italic=italic)

    def draw(self, surface):
        surface.blit(self.button_surface, self.button_box)
        self.button_text.draw(surface)

    def click_normalize(self):
        self.button_surface.set_alpha(255 + self.shading)

    def click(self):
        self.button_surface.set_alpha(255 - self.shading)
        delayed_normalise = threading.Timer(0.1, self.click_normalize)
        delayed_normalise.start()


class AText:
    def __init__(self, text='', x=0, y=0, size=20, element_id='a_text', font_name='arial', centered=False, colour=colours.black,
                 background=None, antialias=0, bold=False, italic=False):
        self.font = pygame.font.SysFont(font_name, size, bold=bold, italic=italic)
        self.text_surface = self.font.render(text, antialias, colour, background)
        self.text_rectangle = self.text_surface.get_rect()
        self.element_id = element_id
        if centered:
            self.text_rectangle.centerx = x
            self.text_rectangle.centery = y
        else:
            self.text_rectangle.x = x
            self.text_rectangle.y = y

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_rectangle)

