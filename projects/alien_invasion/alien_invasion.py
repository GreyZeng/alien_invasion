import sys
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次执行while循环的时候都绘制一个空屏幕，并擦去旧屏幕
            pygame.display.flip()
            # 用于控制帧率，每次循环的时候都进行计时
            # 当这个循环通过速度超过定义的帧率时，Pygame会计算需要暂停多长时间，以便游戏速度保持一致
            # tick方法接受一个参数：游戏的帧率，这里使用的值是 60
            # Pygame将尽可能确保这个循环每秒恰好运行60次
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
