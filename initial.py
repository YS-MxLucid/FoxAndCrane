import pygame

pygame.init()
pygame.display.set_caption('Fox & Crane')
screen_main = pygame.display.set_mode((750, 500))
screen_text = pygame.Surface((150, 500))
screen_img = pygame.Surface((550, 500))
myfont = pygame.font.Font("HanSans.ttf.ttc", 15)
label1 = myfont.render("这是一段文本", True, (210, 210, 215))
label2 = myfont.render("这是另一段文本", True, (210, 210, 215))
img1 = pygame.image.load('test.png')
img1 = pygame.transform.scale(img1, (550, 309))
text_Surf = screen_text.copy()
text_Surf.blit(label1, (0, 20))
text_Surf.blit(label2, (0, 40))
img_Surf = screen_img.copy()
img_Surf.blit(img1, (0, 20))
screen_main.blit(text_Surf, (20, 20))
screen_main.blit(img_Surf, (170, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                continue
    pygame.display.update()
exit()
