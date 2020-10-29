import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

# 加载字体
# ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath',
# 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel',
# 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi',
# 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui',
# 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic',
# 'malgungothicsemilight', 'microsofthimalaya',
# 'microsoftjhengheimicrosoftjhengheiui',
# 'microsoftjhengheimicrosoftjhengheiuibold',
# 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue',
# 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile',
# 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold',
# 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti',
# 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti',
# 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'extra', 'arvo', 'droidserif', 'indieflower', 'lobster', 'opensans', 'poiretone', 'raleway', 'robotocondensed', 'robotoslab', 'icomoon', '方正粗黑宋简体', 'dejavusansmono', 'dejavusansmonooblique', 'numberonly', 'teamviewer15', 'teamviewer14', 'sjqy']
font = pygame.font.get_fonts()
print(font)
red = pygame.Color(255, 0, 0)
# 加粗 斜体
# 方式一：使用系统默认的字体来进行加载
# font = pygame.font.SysFont('方正粗黑宋简体', 40, False, False)
# 方式二：自己准备一个字体ttf，放到咱们的项目里面
font = pygame.font.Font('./static/simkai.ttf', 40)
# 文字对象
text = font.render('得分', True, red)

# 加载音乐
bg_music = pygame.mixer.music.load('./static/game_bg_music.mp3')
# 设置音量大小（0-1），值越小，音量越小
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (20, 20))
    pygame.display.flip()
