import sys, pygame
pygame.init()
size = width, height = 1000, 640

playing = True
cutscene = False

class Ship:
    def __init__(self, sprite, speed):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.speed = speed
        self.maxSpeed = 1.5
        self.health = 10
        self.fireRate = 100
        self.shot = False
        self.shots = []
        self.shotTimer = 0

    def loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]: self.speed[0] += 0.75
        if keys[pygame.K_a]: self.speed[0] -= 0.75
        if keys[pygame.K_s]: self.speed[1] += 0.75
        if keys[pygame.K_w]: self.speed[1] -= 0.75

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
            proj.logic()

    def fire(self):
        if not self.shot:
            self.shots.append(Shot(self.rect.x + (self.rect.width/2) - 5, self.rect.y - 5, (0, -2), pygame.image.load('assets/shot.png'), "player"))
        self.shot = True

class Shot:
    def __init__(self, x, y, speed, sprite, target):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = speed
        self.sprite = sprite
        self.target = target

    def logic(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])

        if self.rect.x < 0 or self.rect.x > width:
            if self.target == "player":
                ship.shots.remove(self)
            else:
                world.shots.remove(self)
        if self.rect.y < 0 or self.rect.y > height:
            if self.target == "player":
                ship.shots.remove(self)
            else:
                world.shots.remove(self)

        screen.blit(self.sprite, self.rect)

class World:
    def __init__(self, debug, level):
        self.debug = debug
        self.debugTimer = 0
        self.shots = []
        self.level = level
        self.map = [
            (15, 50, 255), #color
            [
                [
                    pygame.image.load('assets/rock1.png'),
                    (200, -500)
                ],
                [
                    pygame.image.load('assets/rock2.png'),
                    (750, -800)
                ]
            ], #assets
            0 #timer
        ]

    def loop(self):

        for asset in self.map[1]:
            pass

        for proj in self.shots:
            proj.logic()
            if ship.rect.colliderect(proj.rect):
                ship.health -= 1
                self.shots.remove(proj)

        self.debugTimer += 1

        if self.debug and self.debugTimer%1000 == 0:
            self.shots.append(Shot(0, 0, (1, 1), pygame.image.load('assets/enemyShot.png'), 'world'))

        self.map[2] += 1

ship = Ship(pygame.image.load('assets/ship.png'), [0,0])


world = World(True, 'Debug')


screen = pygame.display.set_mode(size)

while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        screen.fill(world.map[0])

        world.loop()
        ship.loop()
        
        
        screen.blit(ship.sprite, ship.rect)
        pygame.display.flip()

