__author__ = 'Administrator'
from config import *


class Runner(pygame.sprite.Sprite):

    def __init__(self, manager):
        self.manager = manager
        pygame.sprite.Sprite.__init__(self)
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.x = width/2
        self.rect.y = height - 84
        self.surface = self.manager.surface
        self.velocity = 5
        self.gravity = 1
        self.jump_height = -20
        self.state = 'standing'
        self.power_up = 'none'
        self.power_up_timer = 0
        self.can_jump = True
        self.sprite_interval = 0

    def key_event(self, event):
        if event.key == pygame.K_SPACE:
            if self.can_jump:
                jump_sound.play()
                self.state = 'jumping'
                self.can_jump = False
                self.velocity = self.jump_height

    def move(self):
        self.rect.y += self.velocity
        if self.state == 'standing':
            self.velocity = 0
            self.can_jump = True
        if not pygame.sprite.spritecollideany(self, self.manager.formation.ground) or self.state == 'jumping' or self.state == 'falling':
            self.velocity += self.gravity
            if self.velocity > 0:
                self.state = 'falling'

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.sprite_interval += 1
        self.move()
        if self.state == 'jumping':
            self.image = image1
        if self.state == 'standing':
            if self.sprite_interval <= 11:
                self.image = image2
            elif self.sprite_interval <= 22:
                self.image = image3
            elif self.sprite_interval <= 33:
                self.image = image4
            elif self.sprite_interval <= 44:
                self.image = image5
            elif self.sprite_interval <= 55:
                self.image = image6
            elif self.sprite_interval <= 66:
                self.image = image7
            elif self.sprite_interval <= 77:
                self.image = image8
            elif self.sprite_interval <= 88:
                self.image = image9
            elif self.sprite_interval <= 99:
                self.image = image10
            elif self.sprite_interval <= 110:
                self.image = image11
            if self.sprite_interval >= 110:
                self.sprite_interval = 0
        if self.power_up != 'none':
            self.power_up_timer -= 1
            if self.power_up_timer == 0:
                self.power_up = 'none'


class Spikes(pygame.sprite.Sprite):

    def __init__(self, manager, x, y):
        self.manager = manager
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spikes.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(35), int(45)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.manager.speed

    def update(self):
        self.move()
        if self.rect.right <= 0:
            self.kill()


class Coin(pygame.sprite.Sprite):

    def __init__(self, manager, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.manager = manager
        self.image = pygame.image.load("coin.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(35), int(35)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.manager.speed

    def update(self):
        self.move()
        if self.rect.right <= 0:
            self.kill()


class Ground(pygame.sprite.Sprite):

    def __init__(self, manager, x, y):
        self.manager = manager
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ground.PNG").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.manager.speed

    def update(self):
        self.move()
        if self.rect.right <= 0:
            if self.rect.bottom == height:
                self.kill()
                block = Ground(self.manager, width, height-35)
                self.manager.formation.ground.add(block)

            else:
                self.kill()


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, manager, type):
        pygame.sprite.Sprite.__init__(self)
        self.manager = manager
        self.type = type
        if self.type == 1:
            self.image = pygame.image.load("invincibility.png").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("coin_heaven.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(0, height-100)

    def move(self):
        self.rect.x += self.manager.speed

    def update(self):
        self.move()
        if self.rect.right <= 0:
            self.kill()


class Background(pygame.sprite.Sprite):

    def __init__(self, manager, x):
        pygame.sprite.Sprite.__init__(self)
        self.manager = manager
        self.image = pygame.image.load("background.PNG").convert()
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def move(self):
        self.rect.x += self.manager.speed

    def update(self):
        self.move()
        if self.rect.right <= 0:
            self.kill()
            wall = Background(self.manager, width)
            self.manager.background.add(wall)


class Formation():

    def __init__(self, manager):
        self.manager = manager
        self.x = width
        self.coins = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.counter = 0

    def choose_formation(self):
        formation = random.randint(1, 4)
        if formation == 1:
            a = 0
            for i in range(0, 900, 35):
                spike = Spikes(self.manager, self.x+i, height-80)
                self.spikes.add(spike)
            for i in range(0, 175, 35):
                platform = Ground(self.manager, self.x+i, 400)
                self.ground.add(platform)
            for i in range(245, 420, 35):
                platform = Ground(self.manager, self.x+i, 200)
                self.ground.add(platform)
            for i in range(595, 770, 35):
                platform = Ground(self.manager, self.x+i, 450)
                self.ground.add(platform)
            for i in range(35, 450, 35):
                coin = Coin(self.manager, self.x+630+a, i)
                self.coins.add(coin)
                a += 5
        if formation == 2:
            for i in range(0, 900, 35):
                spike = Spikes(self.manager, self.x+i, height-80)
                self.spikes.add(spike)
            for i in range(0, 175, 35):
                platform = Ground(self.manager, self.x+i, 400)
                self.ground.add(platform)
            for i in range(350, 525, 35):
                platform = Ground(self.manager, self.x+i, 400)
                self.ground.add(platform)
            for i in range(700, 875, 35):
                platform = Ground(self.manager, self.x+i, 400)
                self.ground.add(platform)
            for i in range(140, 385, 35):
                coin = Coin(self.manager, self.x+i, 200)
                coin2 = Coin(self.manager, self.x+350+i, 200)
                self.coins.add(coin)
                self.coins.add(coin2)
        if formation == 3:
            for i in range(0, 210, 35):
                spike = Spikes(self.manager, self.x+i, height-80)
                self.spikes.add(spike)
                spike2 = Spikes(self.manager, self.x+i+350, 355)
                self.spikes.add(spike2)
                spike3 = Spikes(self.manager, self.x+i+665, height-80)
                self.spikes.add(spike3)
            for i in range(0, 210, 35):
                platform = Ground(self.manager, self.x+i, 400)
                platform2 = Ground(self.manager, self.x+i+350, 400)
                platform3 = Ground(self.manager, self.x+i+665, 400)
                self.ground.add(platform)
                self.ground.add(platform2)
                self.ground.add(platform3)
        if formation == 4:
            for i in range(0, 900, 35):
                platform = Ground(self.manager, self.x+i, 400)
                self.ground.add(platform)
            for i in range(0, 105, 35):
                spike2 = Spikes(self.manager, self.x+i+175, 355)
                coin = Coin(self.manager, self.x+i+175, 150)
                self.spikes.add(spike2)
                self.coins.add(coin)
                spike3 = Spikes(self.manager, self.x+i+525, 355)
                coin2 = Coin(self.manager, self.x+i+525, 150)
                self.coins.add(coin2)
                self.spikes.add(spike3)
                spike = Spikes(self.manager, self.x+i+795, 355)
                coin3 = Coin(self.manager, self.x+i+795, 150)
                self.spikes.add(spike)
                self.coins.add(coin3)

    def draw(self, surface):
        self.power_ups.draw(surface)
        self.coins.draw(surface)
        self.spikes.draw(surface)
        self.ground.draw(surface)

    def update(self):
        self.counter += 1
        self.coins.update()
        self.spikes.update()
        self.ground.update()
        self.power_ups.update()
        if self.counter == 180:
            self.counter = 0
            self.choose_formation()
        a = random.randint(0, 5000)
        if a >= 4990:
            power_up = PowerUp(self.manager, random.randint(1, 2))
            self.power_ups.add(power_up)
        if self.manager.runner.power_up == "coin heaven":
            if self.counter % 10 == 0:
                coin = Coin(self.manager, width, random.randint(0, height-100))
                self.coins.add(coin)


class GameScreen():

    def __init__(self, surface):
        self.speed = -5
        self.surface = surface
        self.runner = Runner(self)
        self.formation = Formation(self)
        self.background = pygame.sprite.Group()
        self.start_ground()
        self.score = 0
        self.scoreboard = eztext.Input(maxlength=45, color=white, prompt='score:'+str(self.score))
        self.power_up_type = eztext.Input(maxlength=45, color=white, prompt='power up:'+self.runner.power_up)
        self.power_up_type.set_pos(200, 0)

    def start_ground(self):
        for i in range(0, width+35, 35):
            block = Ground(self, i, height - 35)
            self.formation.ground.add(block)
        wall = Background(self, 0)
        wall2 = Background(self, width)
        self.background.add(wall)
        self.background.add(wall2)

    def draw(self):
        self.background.draw(self.surface)
        self.runner.draw()
        self.formation.draw(self.surface)
        self.scoreboard.draw(self.surface)
        self.power_up_type.draw(self.surface)

    def check_colliding(self):
        for coin in self.formation.coins:
            if pygame.sprite.collide_rect(coin, self.runner):
                self.score += 10
                coin.kill()

        for spike in self.formation.spikes:
            if pygame.sprite.collide_rect(spike, self.runner):
                if self.runner.power_up == 'shield':
                    self.runner.velocity = self.runner.jump_height
                    self.runner.state = 'jumping'
                else:
                    print self.score
                    sys.exit()

        for block in self.formation.ground:
            if pygame.sprite.collide_rect(block, self.runner):
                if self.runner.state == 'falling' or self.runner.state == 'standing':
                    if self.runner.rect.top <= block.rect.top:
                        self.runner.state = 'standing'
                        self.runner.rect.bottom = block.rect.top

        for power_up in self.formation.power_ups:
            if pygame.sprite.collide_rect(power_up, self.runner):
                if power_up.type == 1:
                    self.runner.power_up = 'shield'
                    self.runner.power_up_timer = 500
                    power_up.kill()
                if power_up.type == 2:
                    self.runner.power_up = 'coin heaven'
                    self.runner.power_up_timer = 500
                    power_up.kill()

    def update(self):
        self.runner.update()
        self.formation.update()
        self.background.update()
        self.check_colliding()
        self.score += 1
        self.power_up_type = eztext.Input(maxlength=45, color=white, prompt='power up:'+self.runner.power_up)
        self.scoreboard = eztext.Input(maxlength=45, color=white, prompt='score:'+str(self.score))
        self.power_up_type.set_pos(200, 0)