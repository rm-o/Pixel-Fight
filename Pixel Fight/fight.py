import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Pixel Fight")
clock = pygame.time.Clock()

surface = pygame.image.load('assets/background/background.jpg')
start_img = pygame.image.load("buttons/start_btn.png")
exit_img = pygame.image.load("buttons/exit_btn.png")

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True 

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 

        screen.blit(self.image,(self.rect.x, self.rect.y))
        
        return action

start_button = Button(350, 540, start_img, 0.5)
exit_button = Button(600, 540, exit_img, 0.5)

run = True
while run:

    scaled_bg = pygame.transform.scale(surface,(1100, 600))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:    
            pygame.quit()
            exit()

    screen.blit(scaled_bg,(0, 0))

    if start_button.draw():
        print("Start")
    if exit_button.draw():
        run = False
      
    pygame.display.update()
    clock.tick(60)