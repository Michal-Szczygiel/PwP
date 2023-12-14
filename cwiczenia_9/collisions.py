import pygame
import numpy as np

WIDTH = 800
HEIGHT = 600
BALL_SPEED = 10


class Ball:
    def __init__(self, radius):
        alpha = np.random.uniform(0, np.pi)

        self.position = np.random.uniform(200, 400, 2)      # ndarray
        self.direction = np.array([
            np.cos(alpha),
            np.sin(alpha)
        ])                                                  # ndarray
        self.color = np.random.randint(150, 255, 3)         # ndarray
        self.radius = radius

    def move(self):
        self.position = self.position + self.direction * BALL_SPEED

    def collision_check(self):
        if self.position[0] < 0 or self.position[0] > WIDTH:
            self.direction = self.direction * np.array([-1, 1])

        if self.position[1] < 0 or self.position[1] > HEIGHT:
            self.direction = self.direction * np.array([1, -1])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


def run():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    runing = True
    balls = [Ball(15) for _ in range(16)]

    pygame.display.set_caption("COLLISIONS")

    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False


        screen.fill((30, 40, 45))
        
        for ball in balls:
            ball.move()
            ball.collision_check()
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run()
