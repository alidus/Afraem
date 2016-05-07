import agui, pygame
pygame.init()
window_res = (800, 600)
DisplaySurface = pygame.display.set_mode(window_res)
ProgramExit = False
clock = pygame.time.Clock()
FPS = 60


class ColoursPack:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.grey = (200, 200, 200)

colours = ColoursPack()


def clear_screen(surface):
    surface.fill(colours.black)

button1 = agui.AButton(text='Hello', bold=True, width=100, height=50, text_size=30, x=50, y=50)
list1 = agui.AList(200, 0, element_id='list_1', thikness=2, centered_elements=True)
for element in range(10):
    list1.add('element №'+str(element))

while not ProgramExit:
    # clear_screen(DisplaySurface)
    DisplaySurface.fill(colours.grey)
    events = pygame.event.get()
    button1.draw(DisplaySurface)
    list1.draw(DisplaySurface)
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            ProgramExit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            button1.click()
    pygame.display.update()
    clock.tick(FPS)
