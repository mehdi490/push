
import pygame
from Striker import Striker
from Ball import Ball
from Setup import WIDTH, WHITE, HEIGHT, GREEN, screen, BLACK, clock, FPS

def main():
    running = True
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

    listOfGeeks = [geek1, geek2]

    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0
        
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()
        
        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()

        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        
        if point:   # Someone has scored a point and the
          # ball is out of bounds. So, we reset it's position
            ball.reset()
        
        geek1.display()
        geek2.display()
        ball.display()

        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH-100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)     
        
if __name__ == "__main__":
    main()
    pygame.quit()    






