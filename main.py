import pygame
import random

pygame.init()
FPSCLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800,600))
GAMEOVER = False
ICON = pygame.image.load('sprites/icon.png')
PLAYER = pygame.image.load('sprites/player.png')
ENEMY = pygame.transform.scale(pygame.image.load('sprites/enemy.png'), (48,48))

pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(ICON)

SCREEN.fill((0,0,0))

class Bullet:
    def __init__(self, positionX, positionY):
        self.bulletSprite = pygame.image.load('sprites/bullet.png')
        self.positionX = positionX
        self.positionY = positionY
        self.speedUp = -5

    def move(self):
        self.positionY += self.speedUp
        if(self.positionY < 0): # Deleting the key-value pair for the bullet that exits the screen
            bullets.pop(bullets.index(self))
            del self 
        else:
            position = (self.positionX, self.positionY)
            SCREEN.blit(self.bulletSprite,position)

class Player:
    def __init__(self):
        self.playerSprite = PLAYER
        self.positionX = 365
        self.positionY = 480
        self.speedLeft = 0
        self.speedRight = 0

    def move(self):
        self.positionX += (-self.speedLeft + self.speedRight)
        if(self.positionX < 0):
            self.positionX = 0
        elif(self.positionX > 736):
            self.positionX = 736
        SCREEN.blit(self.playerSprite, (self.positionX, self.positionY))


class Enemy:
    def __init__(self, health, fallingspeed, path):
        self.health = health
        self.fallingspeed = fallingspeed
        self.enemySprite = path
        self.positionX = random.randint(0, 736)
        self.positionY = 20
    

    def move(self):
        if(self.positionY >= 600):
            enemies.pop(enemies.index(self))
            del self 
        else:
            self.positionY += self.fallingspeed
            self.positionX = pygame.Vector2.lerp(pygame.Vector2(self.positionX), pygame.Vector2(main_player.positionX), 0.01)
            SCREEN.blit(self.enemySprite,(self.positionX[0],self.positionY))

    
    def isHit(self):
        if(hit):
            self.health -= 25
            if(self.health <= 0):
                pass


bullets = []
enemies = []
bulletFireTimer = 0
enemySpawnTimer = 0
bulletCounter = 0
enemyCounter = 0

main_player = Player()
bulletY = 0

while not GAMEOVER:
    # Code to Spawn bullets
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMEOVER = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_player.speedLeft = 5.2
            if event.key == pygame.K_RIGHT:
                main_player.speedRight = 5.2 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                main_player.speedLeft = 0
            if event.key == pygame.K_RIGHT:
                main_player.speedRight = 0

    if(bulletFireTimer >= 7):
        bullets.append( Bullet(main_player.positionX + 15, main_player.positionY - 15))     
        bulletCounter += 1
        bulletFireTimer = 0
    else:
        bulletFireTimer += 1

    #  Code to spawn enemies
    if( enemies.__len__() <= 4 and enemySpawnTimer >= 50):
        enemies.append(Enemy(100, 1.5, ENEMY))
        enemyCounter += 1
        enemySpawnTimer = 0
    else:
        enemySpawnTimer += 1
        
    # Code to add everything on screen
    SCREEN.fill((0,0,0))

    main_player.move()
    for bullet in bullets:
        bullet.move()

    for enemy in enemies:
        enemy.move()
    pygame.display.update()
    FPSCLOCK.tick(30)

    # Code to handle the left and right arrow press
