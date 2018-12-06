import sys, math, random, pygame

pygame.init()
pygame.font.init()
size = width, height = 1000, 640

# # FPS COUNTER
# def show_fps(window, clock):
#     f = pygame.font.Font(None, 10)
#     fps_overlay = f.render(str(math.floor(clock.get_fps())), True, (255, 255, 255))
#     window.blit(fps_overlay, (0,0))

# clock = pygame.time.Clock()
# FPS = 1000

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

class Ship:
    def __init__(self, sprite, speed):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect = self.rect.move(25, 500)
        self.doLogic = True
        self.speed = speed
        self.maxSpeed = 1.5
        self.health = 10
        self.healthBox = pygame.image.load('assets/health.png')
        self.fireRate = 100
        self.shot = False
        self.shots = []
        self.shotTimer = 0

    def loop(self):
        keys = pygame.key.get_pressed()
        if self.doLogic:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.speed[0] += 0.75
            if keys[pygame.K_a] or keys[pygame.K_LEFT]: self.speed[0] -= 0.75
            if keys[pygame.K_s] or keys[pygame.K_DOWN]: self.speed[1] += 0.75
            if keys[pygame.K_w] or keys[pygame.K_UP]: self.speed[1] -= 0.75

            if keys[pygame.K_SPACE]: self.fire()
        
            self.rect = self.rect.move(self.speed)
            if self.speed[0] < 0:
                self.speed[0] += 0.5
            if self.speed[1] < 0:
                self.speed[1] += 0.5
            if self.speed[0] > 0:
                self.speed[0] -= 0.5
            if self.speed[1] > 0:
                self.speed[1] -= 0.5

            if self.rect.left < 0: self.rect = self.rect.move(-self.rect.left, 0)
            if self.rect.right > width: self.rect = self.rect.move(width - self.rect.right, 0)
            if self.rect.top < 0: self.rect =  self.rect.move(0, -self.rect.top)
            if self.rect.bottom > height: self.rect = self.rect.move(0, height - self.rect.bottom)

            if self.speed[0] > self.maxSpeed: self.speed[0] = self.maxSpeed
            if self.speed[1] > self.maxSpeed: self.speed[1] = self.maxSpeed
            if self.speed[0] < -self.maxSpeed: self.speed[0] = -self.maxSpeed
            if self.speed[1] < -self.maxSpeed: self.speed[1] = -self.maxSpeed


            if self.shot:
                self.shotTimer += 1
                if self.shotTimer > self.fireRate:
                    self.shotTimer = 0
                    self.shot = False

        for proj in self.shots:
            if self.doLogic: proj.logic()
            proj.display()

        for hp in range(self.health):
            screen.blit(self.healthBox, pygame.Rect(30 + (hp * 22), 40, 15, 20))

        screen.blit(self.sprite, self.rect)

        if self.health < 1:
            playing = False
            gameOver = True


    def fire(self):
        if not self.shot:
            self.shots.append(Shot(self.rect.x + (self.rect.width/2) - 5, self.rect.y - 5, (0, -2), pygame.image.load('assets/shot.png'), "player"))
        self.shot = True


class debugEnemy:
    def __init__(self):
        self.rect = pygame.Rect(120, 5, 50, 50)
        self.sprite = pygame.image.load('assets/enemyShip.png')
        self.speed = [0, 0]
        self.maxSpeed = 1.25
        self.health = 10
        self.fireRate = 100
        self.shot = False
        self.shots = []
        self.shotTimer = 0

    def loop(self):
        if self.rect.x + self.rect.width < ship.rect.x:
            self.speed[0] += 0.5
        if self.rect.x > ship.rect.x + ship.rect.width:
            self.speed[0] -= 0.5

        if self.rect.y > 5:
            self.speed[1] -= 0.5
        if self.rect.y < 5:
            self.speed[1] += 0.5

        self.rect = self.rect.move(self.speed)
        if self.speed[0] < 0:
            self.speed[0] += 0.25
        if self.speed[1] < 0:
            self.speed[1] += 0.25
        if self.speed[0] > 0:
            self.speed[0] -= 0.25
        if self.speed[1] > 0:
            self.speed[1] -= 0.25

        if self.rect.left < 0: self.rect = self.rect.move(-self.rect.left, 0)
        if self.rect.right > width: self.rect = self.rect.move(width - self.rect.right, 0)
        if self.rect.top < 0: self.rect =  self.rect.move(0, -self.rect.top)
        if self.rect.bottom > height: self.rect = self.rect.move(0, height - self.rect.bottom)

        if self.speed[0] > self.maxSpeed: self.speed[0] = self.maxSpeed
        if self.speed[1] > self.maxSpeed: self.speed[1] = self.maxSpeed
        if self.speed[0] < -self.maxSpeed: self.speed[0] = -self.maxSpeed
        if self.speed[1] < -self.maxSpeed: self.speed[1] = -self.maxSpeed

        if self.speed[0] == 0:
            if math.floor(random.random() * 2) == 0: self.speed[0] = -0.75
            else: self.speed[0] = 0.75
        if self.speed[1] == 0:
            if math.floor(random.random() * 2) == 0: self.speed[1] = -0.75
            else: self.speed[1] = 0.75

        if self.shot:
            self.shotTimer += 1
            if self.shotTimer > self.fireRate:
                self.shotTimer = 0
                self.shot = False

        self.fire()

        if self.health < 1:
            world.enemies.remove(self)

    def display(self):
        screen.blit(self.sprite, self.rect)

    def fire(self):
        if not self.shot:
            world.shots.append(Shot(self.rect.x + (self.rect.width/2) - 5, self.rect.y - 5, (0, 2), pygame.image.load('assets/enemyShot.png'), "enemy"))
        self.shot = True    

class Shot:
    def __init__(self, x, y, speed, sprite, target):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = speed
        self.sprite = sprite
        self.target = target

    def logic(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])

        if self.target == "player":
            if self.rect.x < 0 or self.rect.x > width:
                ship.shots.remove(self)
            if self.rect.y < 0 or self.rect.y > height:
                ship.shots.remove(self)

            for enemy in world.enemies:
                if self.rect.colliderect(enemy.rect):
                    enemy.health -= 1
                    ship.shots.remove(self)
        else:
            if self.rect.x < 0 or self.rect.x > width:
                world.shots.remove(self)
            if self.rect.y < 0 or self.rect.y > height:
                world.shots.remove(self)

            if self.rect.colliderect(ship.rect):
                ship.health -= 1
                world.shots.remove(self)

    def display(self):
        screen.blit(self.sprite, self.rect)

class World:
    def __init__(self, debug, level):
        self.debug = debug
        self.debugTimer = 1
        self.doLogic = True
        self.pauseDelay = False
        self.shots = []
        self.enemies = []
        self.level = level
        self.map = [
            (15, 50, 255), #color
            [
                [
                    pygame.image.load('assets/rock1.png'),
                    [200, -500]
                ],
                [
                    pygame.image.load('assets/rock2.png'),
                    [750, -800]
                ]
            ], #assets
            0, #timer
            6000 #maxTimer (length of map)
        ]

        for asset in self.map[1]:
            asset.append(asset[0].get_rect())
            asset[2] = asset[2].move(asset[1][0], asset[1][1])

        if self.debug: self.enemies.append(debugEnemy())

    def loop(self):

        for asset in self.map[1]:
            if self.doLogic: asset[2] = asset[2].move(0, 1)
            if asset[2].bottom > 0 and asset[2].top < height:
                screen.blit(asset[0], asset[2])
            

        for proj in self.shots:
            if self.doLogic: proj.logic()
            proj.display()

        for enemy in self.enemies:
            if self.doLogic: enemy.loop()
            enemy.display()

        if self.debug and self.debugTimer%1000 == 0:
            self.shots.append(Shot(0, 0, (1, 1), pygame.image.load('assets/enemyShot.png'), 'world'))

        if self.doLogic: self.updateTime()

    def updateTime(self):
        if self.debug:
            self.debugTimer += 1

        self.map[2] += 1

class Scene:
    def __init__(self, steps):
        self.steps = steps
        self.frames = 0
    def loop(self):
        for step in self.steps:
            if self.frames > step[2]: continue
            else: step[0].rect = step[0].rect.move((step[1][0] / step[2]), (step[1][1] / step[2]))
        self.frames += 1

title = True
playing = False
pause = False
gameOver = False
cutscene = False


ship = Ship(pygame.image.load('assets/ship.png'), [0,0])

world = World(True, 'Debug')

darkSouls = pygame.image.load('assets/gameOverTemp.jpg')

currentScene = (
    ship,
    (0, 150),
    120
)

while title:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))
    f = pygame.font.Font(None, 50)
    s = f.render("PRESS SPACE TO BEGIN", True, (255, 255, 255))
    screen.blit(s, (500 - s.get_width() // 2, 320 - s.get_height() // 2))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        playing = True
        title = False

    # show_fps(screen, clock)
    # clock.tick(FPS)

    pygame.display.flip()

while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(world.map[0])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if not world.pauseDelay:
                if pause:
                    pause = False
                    world.doLogic = True
                    ship.doLogic = True
                else:
                    pause = True
                    world.doLogic = False
                    ship.doLogic = False

                world.pauseDelay = True
        if not keys[pygame.K_ESCAPE] and world.pauseDelay:
            world.pauseDelay = False

        

        world.loop()
        ship.loop()
        
        if pause:
            s = pygame.Surface(size)
            s.set_alpha(120)
            s.fill((0,0,0))
            f = pygame.font.Font(None, 40)
            level = f.render(world.level, True, (255,255,255))
            progress = f.render(str(math.floor(world.map[2]/world.map[3])) + "% Complete", True, (255,255,255))
            s.blit(level, (460, 250))
            s.blit(progress, (420, 300))
            screen.blit(s, (0,0))

        if ship.health < 1:
            gameOver = True
            playing = False

        # show_fps(screen, clock)
        # clock.tick(FPS)
        
        pygame.display.flip()

while cutscene:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(world.map[0])

        # show_fps(screen, clock)
        # clock.tick(FPS)
    

while gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))
    screen.blit(darkSouls, darkSouls.get_rect())

    # show_fps(screen, clock)
    # clock.tick(FPS)

    pygame.display.flip()
    