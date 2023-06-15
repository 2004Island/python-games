import pygame
from random import randint
from sys import exit

pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption('snek')
clock = pygame.time.Clock()
game_active = True
tutorial = True
game_loop = False

appleconsumestat = False
velocity = 16
x = 0
y = -1 * velocity

score = 0
snakecoords = [[400, i*16 + 240] for i in range(0, 3)]
snakelen = len(snakecoords)
pixel_font = pygame.font.Font('snake/Pixeltype.ttf', 50)
applecoord = [randint(8, 41) * 16, randint(8, 22) * 16]
applesfx = pygame.mixer.Sound('snake/hCAIx6Bj.wav')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if tutorial:
        keys = pygame.key.get_pressed()

        window.fill((10, 40, 20))
        message = pixel_font.render('Welcome to Python Snake!', False, (255, 255, 255))
        message_rect = message.get_rect(center = (400, 200))
        messagetwo = pixel_font.render('use the keys [w],[a],[s],[d] to control the snake', False, (255, 255, 255))
        messagetwo_rect = messagetwo.get_rect(center = (400, 250))
        messagethree = pixel_font.render('press [space] to begin and [q] to quit', False, (255, 255, 255))
        messagethree_rect = messagethree.get_rect(center = (400, 300))
        window.blit(message, message_rect)
        window.blit(messagetwo, messagetwo_rect)
        window.blit(messagethree, messagethree_rect)

        if keys[pygame.K_SPACE]:
            game_loop = True
        
        if keys[pygame.K_q]:
            pygame.quit()
            exit()
    
    if game_loop:
        if game_active:
            snakelen = len(snakecoords)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and x != velocity:  # right
                x, y = -1 * velocity, 0

            if keys[pygame.K_d] and x != -1 * velocity:  # left
                x, y = velocity, 0

            if keys[pygame.K_w] and y != velocity:  # up
                x, y = 0, -1 * velocity

            if keys[pygame.K_s] and y != -1 * velocity:  # down
                x, y = 0, velocity
            
            if keys[pygame.K_q]:
                pygame.quit()
                exit()

            if appleconsumestat:
                applecoord = [randint(8, 41) * 16, randint(8, 22) * 16]
                appleconsumestat = False
            else:
                pass

            for i in range(snakelen-1, 0, -1):
                snakecoords[i][0] = snakecoords[i-1][0]
                snakecoords[i][1] = snakecoords[i-1][1]

            snakecoords[0][0] += x
            snakecoords[0][1] += y

            if snakecoords[0][1] - y > 0 and snakecoords[0][1] + y < (480-16):
                pass
            else:
                game_active = False

            if snakecoords[0][0] - x > 0 and snakecoords[0][0] + x < (800-16):
                pass
            else:
                game_active = False

            for i in snakecoords:
                if snakecoords.count(i) > 1:
                    game_active = False
                else:
                    pass
                if i == applecoord and [snakecoords[-1][0] - x, snakecoords[-1][1] - y] not in snakecoords:
                    snakecoords.append([snakecoords[-1][0] - x, snakecoords[-1][1] - y])
                    appleconsumestat = True
                    applesfx.play()
                    score += 1
                elif i == applecoord and [snakecoords[-1][0] + x, snakecoords[-1][1] + y] not in snakecoords:
                    snakecoords.append([snakecoords[-1][0] + x, snakecoords[-1][1] + y])
                    appleconsumestat = True
                    applesfx.play()
                    score += 1

            window.fill((20, 20, 50))
            scoremsg = pixel_font.render(f'Score: {score}', False, (255, 255, 255))
            score_rect = scoremsg.get_rect(center = (400, 50))
            [pygame.draw.rect(window, (200, 0, 100), pygame.Rect(applecoord[0], applecoord[1], 16, 16))]
            [pygame.draw.rect(window, (0, 200, 100), pygame.Rect(snakecoords[i][0], snakecoords[i][1], 16, 16)) for i in range(0, snakelen)]
            window.blit(scoremsg, score_rect)

        else:
            window.fill((50, 20, 20))
            score_rect = scoremsg.get_rect(center = (400, 150))
            message = pixel_font.render('The snake has died', False, (255, 255, 255))
            message_rect = message.get_rect(center = (400, 200))
            messagetwo = pixel_font.render('press space to be born again', False, (255, 255, 255))
            messagetwo_rect = messagetwo.get_rect(center = (400, 250))
            window.blit(message, message_rect)
            window.blit(messagetwo, messagetwo_rect)
            window.blit(scoremsg, score_rect)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                snakecoords = [[400, i*16 + 240] for i in range(0, 3)]
                x = 0
                y = -1 * velocity
                score = 0
                game_active = True
            
            if keys[pygame.K_q]:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(16)
