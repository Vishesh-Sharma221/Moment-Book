from importlib_metadata import textwrap
import pygame 

pygame.init()
screen = pygame.display.set_mode((600,600))
app_fps = pygame.time.Clock()
bg = pygame.image.load('Moment-Book/GUI/assets/login_bg.jpg')
font = pygame.font.Font(None,32)
active_color = pygame.Color('dodgerblue2')
inactive_color = pygame.Color('white')
back_button = pygame.image.load('Moment-Book/GUI/assets/back_button.png')

class InputBox():
    def __init__(self,max_len,x,y,width,height,text = ''):
        self.color = inactive_color
        self.len = max_len
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text 
        self.text_surf = font.render(text,True,self.color)
        self.active = False

    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active 
            else:
                self.active = False
        self.color = active_color if self.active else inactive_color
    
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE or len(self.text)>self.len:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                
                self.text_surf = font.render(self.text,True,self.color)

    def draw(self,screen):
        screen.blit(self.text_surf, (self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(screen,self.color,self.rect,2,border_radius=2)

    def update(self):
        width = max(200, self.text_surf.get_width()+10)
        self.rect.w = width 
        
back_rect = pygame.Rect(30,30,45,45)

def login():
    inputbox = InputBox(15,180,305,140,32)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    running = False  
            inputbox.event_handler(event)
        
        screen.blit(bg,(-167,0))
        screen.blit(back_button,(back_rect.topleft,back_rect.bottomleft))
        

        inputbox.draw(screen)
        inputbox.update()

        pygame.display.update()
        app_fps.tick(60)

