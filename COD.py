import pygame
import random
import time
score = 0
RED = (255, 0, 0)
WHITE = (255, 255, 255)
speed = 10
fishspeed = 2
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
first_time = True
randomovementlist = []
distancemoved = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, backx, backy):
        super().__init__()
        self.image = pygame.Surface([1000, 1000])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

class Target(pygame.sprite.Sprite):
    def __init__(self, targetx, targety):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\fish.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = targetx
        self.rect.y = targety


class Multiplayerbutton(pygame.sprite.Sprite):
    def __init__(self, button2x, button2y):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\ENDLESSBUTTON.png')
        self.image = pygame.transform.scale(self.image, (200, 70))
        self.rect = self.image.get_rect()
        self.rect.x = button2x
        self.rect.y = button2y


class Startbutton(pygame.sprite.Sprite):
    def __init__(self, buttonx, buttony):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\72971ad31e78895.png')
        self.image = pygame.transform.scale(self.image, (200, 70))
        self.rect = self.image.get_rect()
        self.rect.x = buttonx
        self.rect.y = buttony


class Lazergun(pygame.sprite.Sprite):
    def __init__(self, gunx, guny):
        super().__init__()
        self.image = pygame.Surface([7, 7])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = gunx
        self.rect.y = guny


class Tester1(pygame.sprite.Sprite):
    def __init__(self, test1x, test1y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = test1x
        self.rect.y = test1y


class Tester2(pygame.sprite.Sprite):
    def __init__(self, test2x, test2y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = test2x
        self.rect.y = test2y

def timer():
    for n in range(3):
        return n

#def standard_game(Lazer, enemy):



pygame.init()



# Set the title of the window
pygame.display.set_caption('Not COD')

# Create the player paddle object
Lazer = Lazergun(50, 50)
Tester1 = Tester1(480, 260)
Tester2 = Tester2(300, 200)
s = Startbutton(300, 100)
e = Multiplayerbutton(300, 300)
fish = Target(100, 100)
background = Background(0, 0)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(Tester1)
all_sprites_list.add(Tester2)
all_sprites_list.add(s)
all_sprites_list.add(e)
all_sprites_list.add(Lazer)

gamesprites = pygame.sprite.Group()
gamesprites.add(background)


screen = pygame.display.set_mode([800, 600])

clock = pygame.time.Clock()
done = False
gameon = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Lazer.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        Lazer.rect.x += speed
    if keys[pygame.K_UP]:
        Lazer.rect.y -= speed
    if keys[pygame.K_DOWN]:
        Lazer.rect.y += speed
    if keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, s) and not gameon:
        gameon = True
        gametype = "standard"
        print("s")
    if keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, e) and not gameon:
        gameon = True
        gametype = "endless"
        print("e")
    if gameon and first_time:
        if gametype == "standard":
            first_time = False
            all_sprites_list.remove(Tester1, Tester2, s, e, Lazer)
            Lazer = Lazergun(50, 50)
            fish = Target(100, 100)
            gamesprites.add(fish)
            gamesprites.add(Lazer)
            gamesprites.draw(screen)
            pygame.display.flip()
    for addingtolist in range(20):
        direction = random.randint(0, 1)
        randomovementlist.append(direction)
    for randomovement in range(len(randomovementlist)):
        if randomovement == 0:
            ogposx = fish.rect.x
            fish.rect.x += fishspeed
            if int(fish.rect.x)+100 < ogposx or int(fish.rect.x)-100 > ogposx:# or int(fish.rect.x) < 0:
                fishspeed = -1 * (fishspeed)
                break
        elif randomovement == 1:
            ogposy = fish.rect.y
            fish.rect.y += fishspeed
            if int(fish.rect.y)+100 < ogposy or int(fish.rect.y)-100>ogposy:# or int(fish.rect.y) < 0:
                fishspeed = -1*(fishspeed)
                break
        #elif randomovement == 2:
         #   ogposx = fish.rect.x
          #  fish.rect.x += fishspeed
           # if int(fish.rect.x)+100 < ogposx or int(fish.rect.x)-100>ogposx:# or int(fish.rect.y) < 0:
            #    break
        #elif randomovement == 3:
         #   ogposy = fish.rect.y
          #  fish.rect.y += fishspeed
           # if int(fish.rect.y)+100 < ogposy or int(fish.rect.y)-100>ogposy:# or int(fish.rect.y) < 0:
            #    break

    if keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, fish):
        score += 1
        gamesprites.remove(fish)
        fish = Target(random.randint(100, 700), random.randint(50, 500))
        gamesprites.add(fish)
        gamesprites.remove(Lazer)
        gamesprites.add(Lazer)

    # -- Draw everything
    # Clear screen


    # Draw sprites
    if not gameon:
        all_sprites_list.draw(screen)
    else:
        screen.fill(BLUE)

        gamesprites.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(30)

pygame.quit()
