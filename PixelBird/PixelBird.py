import pygame
import sys


class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        self.birdStatus = [pygame.image.load("img/1.png"),
                           pygame.image.load("img/2.png"),
                           pygame.image.load("img/dead.png")]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False

    def bird_update(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= int(self.jumpSpeed)
        else:
            self.gravity += 0.2
            self.birdY += int(self.gravity)
        self.birdRect[1] = int(self.birdY)
        print(self.birdRect[1])


class Pipeline(object):
    def __init__(self):
        self.wallX = 400
        self.pineUp = pygame.image.load("img/top.png")
        self.pineDown = pygame.image.load("img/bottom.png")

    def update_pipeline(self):
        self.wallX -= 5
        if self.wallX < -80:
            global score
            score += 1
            self.wallX = 400


def create_map():
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # 显示管道
    screen.blit(Pipeline.pineUp, (Pipeline.wallX, -300))
    screen.blit(Pipeline.pineDown, (Pipeline.wallX, 500))
    Pipeline.update_pipeline()

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1

    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))
    Bird.bird_update()

    # 显示分数
    screen.blit(font.render('Score:' + str(score), -1, (255, 255, 255)), (100, 50))
    pygame.display.update()


def check_dead():
    up_rect = pygame.Rect(Pipeline.wallX, -300,
                          Pipeline.pineUp.get_width() - 10,
                          Pipeline.pineUp.get_height())

    down_rect = pygame.Rect(Pipeline.wallX, 500,
                            Pipeline.pineDown.get_width() - 10,
                            Pipeline.pineDown.get_height())
    # 检测小鸟与上下方管子是否碰撞
    if up_rect.colliderect(Bird.birdRect) or down_rect.colliderect(Bird.birdRect):
        Bird.dead = True

    # 检测小鸟是否飞出上下边界
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def get_result():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)
    ft1_surf = font.render(final_text1, 1, (242, 3, 36))
    ft2_surf = font.render(final_text2, 1, (253, 177, 6))

    screen.blit(ft1_surf, [int(screen.get_width() / 2 - ft1_surf.get_width() / 2), 100])
    screen.blit(ft2_surf, [int(screen.get_width() / 2 - ft2_surf.get_width() / 2), 200])
    pygame.display.flip()


if __name__ == '__main__':
    """主程序"""
    pygame.init()
    size = width, height = 400, 650
    screen = pygame.display.set_mode(size)

    color = (0, 0, 0)  # 设置填充颜色
    charlotte = pygame.image.load("img/bg.png")  # 记载图片
    charlotte_rect = charlotte.get_rect()

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 50)

    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    score = 0
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpSpeed = 10

        background = pygame.image.load("img/bg.png")
        if check_dead():
            get_result()
            break
        else:
            create_map()
    pygame.quit()
