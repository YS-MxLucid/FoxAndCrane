import os
import pygame

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fox & Crane')
myfont = pygame.font.Font("HanSans.ttf.ttc", 15)
label = myfont.render("这是一段文本\n这是另一段文本", True, (122, 122, 150))
screen.blit(label, (50, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
exit()
