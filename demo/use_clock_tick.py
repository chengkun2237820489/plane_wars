import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

# 加载图片
image1 = pygame.image.load('./static/hero1.png')
image2 = pygame.image.load('./static/hero2.png')

clock = pygame.time.Clock()

counter = 0
while True:
    counter += 1
    print(111)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 每秒执行次数
    clock.tick(1)
    # 绘制白色屏幕
    screen.fill(pygame.Color(255, 255, 255))
    # 绘制图片
    if counter % 5 == 0:
        screen.blit(image1, (20, 20))
    else:
        screen.blit(image2, (20, 20))
    pygame.display.flip()
