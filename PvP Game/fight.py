import pygame
from sys import exit

player_w = 150
player_h = 150

# class Player1(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         player1 = pygame.image.load('characters/Running1/1.png').convert_alpha()
#         self.image1 = pygame.transform.scale(player1, (player_w, player_h))
#         self.player1_rect = self.image1.get_rect(midleft = (200, 300))

#     def player1_movement(self):
#         key = pygame.key.get_pressed()
#         if key[pygame.K_a]:
#             self.player1_rect.x -= 5
#         elif key[pygame.K_d]:
#             self.player1_rect.x += 5
#         elif key[pygame.K_w]:
#             self.player1_rect.y -= 5
#         elif key[pygame.K_s]:
#             self.player1_rect.y += 5

#     def update(self):
#         self.player1_movement()

# class Player2(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         player2 = pygame.image.load('characters/Running2/1.png').convert_alpha()
#         self.image2 = pygame.transform.scale(player2, (player_w, player_h))
#         self.image2_flip = pygame.transform.flip(self.image2, True, False)
#         self.player2_rect = self.image2_flip.get_rect(midright = (900, 300))

#     def player2_movement(self):
#         key = pygame.key.get_pressed()
#         if key[pygame.K_UP]:
#             self.player2_rect.y -= 5
#         elif key[pygame.K_DOWN]:
#             self.player2_rect.y += 5
#         elif key[pygame.K_LEFT]:
#             self.player2_rect.x -= 5
#         elif key[pygame.K_RIGHT]:
#             self.player2_rect.x += 5

#     def update(self):
#         self.player2_movement()

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
    
pygame.init()
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Pixel Fight")
clock = pygame.time.Clock()

# player = pygame.sprite.GroupSingle()
# player.add(Player1())
# player.add(Player2())

surface = pygame.image.load('assets/background/background.jpg')
start_img = pygame.image.load("buttons/start_btn.png")
exit_img = pygame.image.load("buttons/exit_btn.png")

# Players
player1 = pygame.image.load('characters/Running1/1.png').convert_alpha()
# player1_run2 = pygame.image.load('characters/Running1/2.png').convert_alpha()
# player1_run = [player1_run1, player1_run2]
# player1_index = 0
# player1_image = player1_run[player1_index]
image1 = pygame.transform.scale(player1, (player_w, player_h))
player1_rect = image1.get_rect(midleft = (200, 300))

player2 = pygame.image.load('characters/Running2/1.png').convert_alpha()
# player2_run2 = pygame.image.load('characters/Running2/2.png').convert_alpha()
# player2_run = [player2_run1, player2_run2]
# player2_index = 0
# player2_image = player2_run[player2_index]
image2 = pygame.transform.scale(player2, (player_w, player_h))
image2_flip = pygame.transform.flip(image2, True, False)
player2_rect = image2_flip.get_rect(midright = (900, 300))

# HeartBar
heart = [pygame.image.load('hearts/heart3.png').convert_alpha(),
         pygame.image.load('hearts/heart2.png').convert_alpha(),
         pygame.image.load('hearts/heart1.png').convert_alpha()]

start_button = Button(350, 540, start_img, 0.5)
exit_button = Button(600, 540, exit_img, 0.5)

run = True
while run:

    scaled_bg = pygame.transform.scale(surface,(1100, 600))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:    
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player1_rect.x -= 5
    elif key[pygame.K_d]:
        player1_rect.x += 5
    elif key[pygame.K_w]:
        player1_rect.y -= 5
    elif key[pygame.K_s]:
        player1_rect.y += 5

    if key[pygame.K_UP]:
        player2_rect.y -= 5
    elif key[pygame.K_DOWN]:
        player2_rect.y += 5
    elif key[pygame.K_LEFT]:
        player2_rect.x -= 5
    elif key[pygame.K_RIGHT]:
        player2_rect.x += 5
        
    screen.blit(scaled_bg,(0, 0))
    if start_button.draw():
        print("Start")
    if exit_button.draw():
        run = False
    
    # pygame.draw.rect(screen, 'Red', player1_rect)
    # pygame.draw.rect(screen, 'Red', player2_rect)
    screen.blit(image1, player1_rect)
    screen.blit(image2_flip, player2_rect)

    screen.blit(heart[0], (30, 40))
    screen.blit(heart[0], (890, 40))
    
    pygame.display.update()
    clock.tick(60)