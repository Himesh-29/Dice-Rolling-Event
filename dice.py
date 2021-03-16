import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("Events of Dice")

#Screen Settings
screen_width=600
screen_height=240
screen = pygame.display.set_mode((screen_width, screen_height))

#Image Settings
image1 = pygame.image.load('Images\One.png').convert_alpha()
image2 = pygame.image.load('Images\Two.png').convert_alpha()
image3 = pygame.image.load('Images\Three.png').convert_alpha()
image4 = pygame.image.load('Images\Four.png').convert_alpha()
image5 = pygame.image.load('Images\Five.png').convert_alpha()
image6 = pygame.image.load('Images\Six.png').convert_alpha()

image_rect=image1.get_rect()
image_rect.center=(screen_width//2,150)

#Font Settings
font=pygame.font.SysFont('comicsansms', 16)
text1 = font.render('Press Spacebar to display a particular face of dice (hold it to see it properly)',True,(0,0,255))
text2 = font.render('Press Q to quit the game',True,(0,0,255))
text_roll_1 = font.render('You rolled 1',True,(0,0,255))
text_roll_2 = font.render('You rolled 2',True,(0,0,255))
text_roll_3 = font.render('You rolled 3',True,(0,0,255))
text_roll_4 = font.render('You rolled 4',True,(0,0,255))
text_roll_5 = font.render('You rolled 5',True,(0,0,255))
text_roll_6 = font.render('You rolled 6',True,(0,0,255))

text1_rect=text1.get_rect()
text1_rect.center=(screen_width//2,30)
text2_rect=text2.get_rect()
text2_rect.center=(screen_width//2,50)

text_roll_1_rect=text_roll_1.get_rect()
text_roll_1_rect.center=(screen_width//2,90)
text_roll_2_rect=text_roll_2.get_rect()
text_roll_2_rect.center=(screen_width//2,90)
text_roll_3_rect=text_roll_3.get_rect()
text_roll_3_rect.center=(screen_width//2,90)
text_roll_4_rect=text_roll_4.get_rect()
text_roll_4_rect.center=(screen_width//2,90)
text_roll_5_rect=text_roll_5.get_rect()
text_roll_5_rect.center=(screen_width//2,90)
text_roll_6_rect=text_roll_6.get_rect()
text_roll_6_rect.center=(screen_width//2,90)


def throw_dice():
    while True:
        screen.fill((255,255,0))
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)
        random_number = random.randint(1, 6)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if random_number == 1:
                        screen.blit(image1,image_rect)
                        screen.blit(text_roll_1,text_roll_1_rect)
                    elif random_number == 2:
                        screen.blit(image2,image_rect)
                        screen.blit(text_roll_2,text_roll_2_rect)
                    elif random_number == 3:
                        screen.blit(image3,image_rect)
                        screen.blit(text_roll_3,text_roll_3_rect)
                    elif random_number == 4:
                        screen.blit(image4,image_rect)
                        screen.blit(text_roll_4,text_roll_4_rect)
                    elif random_number == 5:
                        screen.blit(image5,image_rect)
                        screen.blit(text_roll_5,text_roll_5_rect)
                    elif random_number == 6:
                        screen.blit(image6,image_rect)
                        screen.blit(text_roll_6,text_roll_6_rect)
                if event.key == pygame.K_q:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            pygame.display.flip()

throw_dice()