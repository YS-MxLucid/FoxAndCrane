import os
import pygame

pygame.init()
pygame.display.set_caption('Fox & Crane')
screen_main = pygame.display.set_mode((700, 500))
screen_text = pygame.Surface((150, 100))
myfont = pygame.font.Font("HanSans.ttf.ttc", 15)
label = myfont.render("这是一段文本", True, (210, 210, 215))
text_Surf = screen_text.copy()
text_Surf.blit(label, (0, 20))
screen_main.blit(text_Surf, (50, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
exit()
