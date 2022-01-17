import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Moment Book!')
app_fps = pygame.time.Clock()
font = pygame.font.Font('font.ttf',30)

class Button():
    def __init__(self,text,width,height,pos):
        self.pressed = False
        self.Top_rect = pygame.Rect(pos,(width,height))
        self.Top_color = (245,245,245)

        self.text_surf = font.render(text,True,(0,0,0))
        self.text_rect = self.text_surf.get_rect(center = self.Top_rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.Top_color,self.Top_rect,border_radius=12)
        screen.blit(self.text_surf,self.text_rect)

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Top_rect.collidepoint(mouse_pos):
            self.Top_color = '#ffff99'
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.Top_color = '#e6e600'
                self.pressed = False 

    def reset_button_color(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.Top_rect.collidepoint(mouse_pos) == False:
            self.Top_color = (255,255,255)
            

bg_surf = pygame.image.load('bg.jpg')
create = Button('Create!',280,50,(50,145))
view = Button('View',280,50,(50,245))
edit = Button('Edit',280,50,(50,345))
delete = Button('Delete',280,50,(50,438))

def display_buttons(*BUTTON):
    for button in BUTTON:
        button.draw()
        button.check_hover()
        button.reset_button_color()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surf,(0,0))
    display_buttons(create,view,edit,delete)
    

    pygame.display.update()
    app_fps.tick(60)