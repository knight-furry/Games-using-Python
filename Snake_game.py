import pygame
import random
import os
# pygame.mixer.init()
# pygame.mixer.music.load("demp.mp3")
# pygame.mixer.music.play()
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

pygame.display.set_caption("Snake_With_Datta")
gameWindow = pygame.display.set_mode((800, 400))
pygame.display.update()
font = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_window(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    game_exit = False
    while not game_exit:
        gameWindow.fill(white)
        text_screen("Welcome to snakes", red, 250, 150)
        text_screen("Press spacebar to play..", red, 230, 200)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(30)

def gameloop():
    game_exit = False
    game_over = False
    snake_x = random.randint(20, 780)
    snake_y = random.randint(20, 380)
    food_x = random.randint(20, 780)
    food_y = random.randint(20, 380)
    score = 0
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    fps = 30
    clock = pygame.time.Clock()
    snake_list = []
    snake_length = 1
    if not os.path.exists("scorecard.txt"):
        with open("scorecard.txt", "w") as f:
            f.write("0")
    with open("scorecard.txt", "r") as f:
        hiscore = f.read()

    while not game_exit:
        if game_over:
            with open("scorecard.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game over, press enter to continue...!", red, 160, 170)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                # print("Score:", score)
                food_x = random.randint(20, 780)
                food_y = random.randint(20, 380)
                snake_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score:"+str(score)+"  Highscore:"+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            plot_window(gameWindow, black, snake_list, snake_size)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > 800 or snake_y < 0 or snake_y > 400:
                game_over = True
                # print("Game over...!")

        # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()