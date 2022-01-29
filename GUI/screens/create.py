import pygame 
from login import InputBox

pygame.init()
screen = pygame.display.set_mode((600,600))
app_fps = pygame.time.Clock()
bg = pygame.image.load('Moment-Book/GUI/assets/create_bg.jpg')
font = pygame.font.Font(None,32)

def create():
    inputbox_1 = InputBox(39,110,97,140,32)
    inputbox_2 = InputBox(100,60,220,140,342)
    inputbox = [inputbox_1,inputbox_2]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 
            for box in inputbox:
                box.event_handler(event)

        screen.blit(bg,(0,0))
        for box in inputbox:
            box.draw(screen)
            box.update()

        pygame.display.update()
        app_fps.tick(60)

create()