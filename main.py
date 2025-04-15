# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from clown import Clown
import random

pygame.init()

WIDTH=640
HEIGHT=640
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

lives = 3
score =0

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the clown")


custom_font = pygame.font.Font("CAMPUS PERSONAL USE.ttf", 40)
custom_text = custom_font.render("CATCH THE CLOWN", True, BLUE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.left = 10
custom_text_rect.top = 20

custom_font2 = pygame.font.Font("CollegiateFLF.ttf", 25)
custom_text2 = custom_font2.render(f"LIVES : {lives}", True, BLUE)
custom_text2_rect = custom_text2.get_rect()
custom_text2_rect.right = HEIGHT - 20
custom_text2_rect.top = 15

custom_text_score = custom_font2.render(f"SCORE :{score}", True, RED)
score_rect = custom_text_score.get_rect()
score_rect.top = custom_text2_rect.bottom + 10
score_rect.left = custom_text2_rect.left

gameover_text = custom_font2.render(f"GAME OVER", True, BLUE)
gameover_rect = gameover_text.get_rect()
gameover_rect.center =(WIDTH//2, HEIGHT//2)

clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.x = random.randint(0, 50)
clown_rect.y=random.randint(0, HEIGHT)

clown = Clown(clown_rect)

sound1 = pygame.mixer.Sound("sound.wav")
sound1.set_volume(0.2)

music = pygame.mixer.music.load("experimental-cinematic-hip-hop-315904.mp3")

pygame.mixer.music.play(-1, 0.0)
running=True
while running:
    events = pygame.event.get()

    for event in events:
        print(event)
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if clown.inSurface(pos):
                clown.velocity.x*=-1
                clown.applyForce(clown.velocity.normalize()*0.1)
                score+=20
                sound1.play()
            else:
                lives-=1
    #intialisation of the game
    pygame.draw.rect(display_surface,CYAN,  (0, 0, WIDTH//2, HEIGHT), 0)
    pygame.draw.rect(display_surface, YELLOW, (WIDTH//2, 0, WIDTH, HEIGHT), 0)
    display_surface.blit(custom_text, custom_text_rect)

    #score and lives text
    custom_text2 = custom_font2.render(f"LIVES : {lives}", True, BLUE)
    custom_text_score = custom_font2.render(f"SCORE :{score}", True, RED)
    display_surface.blit(custom_text2, custom_text2_rect)
    display_surface.blit(custom_text_score, score_rect)

    if lives==0:
        display_surface.blit(gameover_text, gameover_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused=True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    score=0
                    lives=2
                    clown.location.x=random.randint(0, 50)
                    clown.location.y = random.randint(0,100)
                    clown.velocity = pygame.math.Vector2(0.2, 0.2)
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused=False
                if event.type==pygame.QUIT:
                    is_paused=False
                    running=False

    #update of the model
    clown.update()
    clown.checkEdges(WIDTH, HEIGHT)
    clown_rect = clown.display()
    display_surface.blit(clown_image,clown_rect)

    pygame.display.update()

pygame.quit()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
