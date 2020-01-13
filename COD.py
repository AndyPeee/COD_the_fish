"""
This first block of code just imports pygame and random and sys, and sets up some variables to be used later
"""


import pygame, sys
import random
clock = pygame.time.Clock()
timer = 3
intitaltext = '10'.rjust(3)  # sets the clocks first value
score = 0  # sets the initial score to be added to later
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255) # these lines set the colors to be used later
BLACK = (0, 0, 0)
speed = 10  # sets the speed of the fishing rod
fishspeedy = 2  # sets the respective speed of the fishes movement. Will be changed, but this is for the
fishspeedx = 2  # initial speed
randomlenofmovement = random.randint(10, 100)  # sets a random length for the first movement of the fish to be. This is needed as the length of movement is set after the first change, so there would be no initial length
first_time = True  # sets a bool to intitiate some features that only happen once, and only once the game has started
randomovementlist = []


"""
This next block of code sets the sprites to be used in the game at various points in time
"""

class ScoreandTimer(pygame.sprite.Sprite):  # this sprite will be used for all the text displayed in the top right corner
    def __init__(self, score, timer, fontx, fonty): # this function writes the initial text and sets the position of the text
        super().__init__()
        self.font = pygame.font.SysFont('arial', 30)
        self.image = self.font.render(str("Your score is: ")+str(score)+str(" Time left: ")+str(timer), True, BLACK) # uses one of the colors established above and sets the string to be printed
        self.score = score
        self.timer = timer
        self.rect = self.image.get_rect()
        self.rect.x = fontx
        self.rect.y = fonty
    def update(self, counter): # this function updates the score and time remaining every time one of these events happen
        self.image = self.font.render(str("Your score is: ")+str(score)+str(" Time left: ")+str(timer), True, BLACK)


class Background(pygame.sprite.Sprite):  # this sprite is the background in the game
    def __init__(self, backx, backy):
        super().__init__()
        self.image = pygame.Surface([800, 600])  # it is created as a surface, with a size the same as the screen
        self.image.fill(BLUE)  # uses one of the colors established above
        self.rect = self.image.get_rect()

class Target(pygame.sprite.Sprite):
    def __init__(self, targetx, targety):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\fish.png') # loads an image to be used over the sprites rect
        self.image = pygame.transform.scale(self.image, (100, 100))  # rescales the image to a reasonable size
        self.rect = self.image.get_rect()  # turns the image into a rectangle to give it x and y coordinates and a hitbox
        self.rect.x = targetx
        self.rect.y = targety

class Startbutton(pygame.sprite.Sprite):  # creates a sprite to be collided with to start the game
    def __init__(self, buttonx, buttony):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\72971ad31e78895.png') # loads the image of the button
        self.image = pygame.transform.scale(self.image, (200, 70))
        self.rect = self.image.get_rect()  # gives the button properties like x an y coordinate to be set to and a hitbox to be collided with
        self.rect.x = buttonx
        self.rect.y = buttony


class Lazergun(pygame.sprite.Sprite):  # creates the player-controlled sprite
    def __init__(self, gunx, guny):
        super().__init__()
        self.image = pygame.Surface([7, 7])  # makes the sprite a rectangle (with the given dimmensions) rather than an image
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()  # gives the sprite and x and y coordinate and a hitbox
        self.rect.x = gunx
        self.rect.y = guny


class Fishingrod(pygame.sprite.Sprite):  # this sprite will be following the player sprite
    def __init__(self,rodx, rody):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\andre\PycharmProjects\I\COD\fishing-rod-png-transparent-fishing-rods-clipart-db89d1e87e964c12.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()  # gives the sprite x and y coordinates so that it can follow the player
        self.rect.x = rodx
        self.rect.y = rody

"""
These next classes create sprites that will sit at the edges of the screen and are the same colour as the background
(invisible) and are 1 pixel wide to be used a walls that sense when the fish is touching them to reverse the fishes
direction. There is 4, 1 at each side to the screen
"""


class Tester1(pygame.sprite.Sprite):
    def __init__(self, test1x, test1y):
        super().__init__()
        self.image = pygame.Surface([1000, 1])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = test1x
        self.rect.y = test1y

class Wall1(pygame.sprite.Sprite):
    def __init__(self, test1x, test1y):
        super().__init__()
        self.image = pygame.Surface([1000, 1])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = test1x
        self.rect.y = test1y

class Wall2(pygame.sprite.Sprite):
    def __init__(self, test1x, test1y):
        super().__init__()
        self.image = pygame.Surface([1, 1000])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = test1x
        self.rect.y = test1y


class Tester2(pygame.sprite.Sprite):
    def __init__(self, test2x, test2y):
        super().__init__()
        self.image = pygame.Surface([1, 1000])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = test2x
        self.rect.y = test2y






pygame.init()



# Set the title of the window
pygame.display.set_caption('Not COD')

# Create the player and other sprites origional positons
Lazer = Lazergun(50, 50)
Tester1 = Tester1(0, 0)
Tester2 = Tester2(0, 0)
wall1 = Wall1(0, 600)
wall2 = Wall2(800, 0)
s = Startbutton(300, 200)
fish = Target(100, 100)
background = Background(0, 0)
fishingrod = Fishingrod(50, 50)
scoreandtimer = ScoreandTimer(0, 10, 400, 50)

all_sprites_list = pygame.sprite.Group()  # creates a group for the sprites needed at the beggining to be added to. Groups let you update only certain sprites at a time

all_sprites_list.add(s)  # adds the sprites
all_sprites_list.add(Lazer)




gamesprites = pygame.sprite.Group()  # creates a group for all the sprites needed only for the game to be added to


gamesprites.add(background)
gamesprites.add(wall1)
gamesprites.add(wall2)  # adds the sprites needed for the game to this group
gamesprites.add(Tester1)
gamesprites.add(Tester2)
gamesprites.add(scoreandtimer)

screen = pygame.display.set_mode([800, 600])  # creates the screen and sets the size
pygame.time.set_timer(pygame.USEREVENT, 1000)  # sets an "event" to happen every 1000 milliseconds (1 second) for the timer to use to keep time

done = False  # sets a couple of bools and a variable to be altered during the game
gameon = False
counter = 0


"""
This next segment is what actually happens in the game. The game ends when this loop ends, and it repeats until a factor
inside the loop decides to end it. This means that the gameplay will continue until it is needed to be ended
"""

while not done:
    for event in pygame.event.get():  # this loop checks all the events and looks to see what action the program should perform
        if event.type == pygame.QUIT:
            done = True  # ends the while loop if the player presses the "x" in the top right of the window
        if gameon and event.type == pygame.USEREVENT:
            timer -= 1  # subtracts 1 off of the timer (of initially 10) every second, making the timer = 0 after 10 seconds
            scoreandtimer.update(timer)  # updates the timer displayed at the top right every second
        if timer == 0:  # occurs after 10 seconds
            highscore = open("Highscore.txt", "r")  # reads the old highscore
            currenthscore = highscore.readline()
            if int(score) > int(currenthscore):  # compares old highscore to new score
                highscore = open("Highscore.txt", "w")  # if the new score is higher, it writes the new score into a txt file to become the new highscore for later player
                highscore.write(str(score))
                print("The new High score is "+str(score))  # prints your new highscore
                pygame.quit()  # quits the game so you don't have to keep playing for ever
            else:
                print("The highscore is "+str(currenthscore)+", your score is "+str(score))  # if you didn't get a new highscore it just prints your score and the old one
            sys.exit("Thanks for playing")  # exits the game/code in general AND types in red (very cool)
    """
    This next section moves the sprite that you can control by taking in key presses and converting it to a change
    in the sprites position
    """
    keys = pygame.key.get_pressed()  # sets the keys variable to any event that involves keys getting pressed
    if keys[pygame.K_LEFT]:  # takes in the button press
        Lazer.rect.x -= speed  # changes the sprites position
        fishingrod.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        Lazer.rect.x += speed
        fishingrod.rect.x += speed
    if keys[pygame.K_UP]:
        Lazer.rect.y -= speed
        fishingrod.rect.y -= speed
    if keys[pygame.K_DOWN]:
        Lazer.rect.y += speed
        fishingrod.rect.y += speed
    if keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, s) and not gameon:  # uses the space bar as an activation for the game and checks to see if the player sprite and the start button sprite are touching
        gameon = True  # starts the game
    if gameon and first_time:  # sets a bunch of variables to ensure that only the things needed in the game are used
        first_time = False
        all_sprites_list.remove(Tester1, Tester2, s, Lazer)  # removes all the sprites from the non-gamesprites list as they won't be needed anymore
        fishingrod = Fishingrod(8, 30)  # redefines the positions and layers the sprites (the earlier they are defined the closer to the top)
        fish = Target(100, 100)
        Lazer = Lazergun(100, 100)
        gamesprites.add(fishingrod)
        gamesprites.add(fish)
        gamesprites.add(Lazer)  # adds the sprites to be used in the game to a new group
        gamesprites.draw(screen)  # draws the sprites onto the background
        pygame.display.flip()  # updates the window to these changes
        timer = 10  # sets the 10 sec timer

        """
        This next section randomly changes the fishes position based on a bunch of variables. It randomly chooses a 
        direction and a speed and a length that the fish will travel, then moves the fish, making sure to take into
        account of walls
        """

    if gameon:
        if counter == randomlenofmovement or keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, fish) or pygame.sprite.collide_rect(fish, wall1) or pygame.sprite.collide_rect(fish, wall2) or pygame.sprite.collide_rect(fish, Tester2) or pygame.sprite.collide_rect(fish, Tester1):
            # *for the previous line* picks a random direction and speed and length travelled for the fish if either the fish has travelled the previous length travelled, has been "cought" or is touching a wall
            if pygame.sprite.collide_rect(fish, wall1) or pygame.sprite.collide_rect(fish, wall2) or pygame.sprite.collide_rect(fish, Tester2) or pygame.sprite.collide_rect(fish, Tester1):
                # *for the previous line* checks to see if the reason for this was a wall or not, if it was a wall, reverses the fishs speed to send it the other way
                fishspeedx = -1*fishspeedx  # reverses the fishs speed
                fishspeedy = -1*fishspeedy
                fish.rect.x += fishspeedx  # moves it away from the wall
                fish.rect.y += fishspeedy
                pass  # it hit a wall, not was captured or expended its movement length, so it doesn't need to be reassigned an angle or a length, so it can skip the next section
            fishspeedx = random.randint(1, 5)  # this and the next line determine a random rate of change for the fish to move at (a speed)
            fishspeedy = random.randint(1, 5)
            randomlenofmovement = random.randint(50, 200)  # this chooses a random length of the path the fish will take before changing directions
            randomfwdbwd = random.randint(0, 1)  # randomly decides whether to go forward or backwards (50/50 chance)
            if randomfwdbwd == 1:  # 50% chance that nothing changes, but if its the other 50% this statement activates to change the direction
                fishspeedx = -1 * fishspeedx  # changes the sign in front of the speed variable, which changes the direction it was going to the opposite
            randomfwdbwd = random.randint(0, 1)
            if randomfwdbwd == 1:
                fishspeedy = -1 * fishspeedy
        else:  # if there is no need to change the fishes movement, it moves the fish then increases the distance moved
            counter += 1
            fish.rect.x += fishspeedx
            fish.rect.y += fishspeedy

    if keys[pygame.K_SPACE] and pygame.sprite.collide_rect(Lazer, fish):  # checks to see if the fish was caught (no need for new direction and speed in this loop because the other loop would activate anyways)
        score += 1  # increases the players score
        gamesprites.remove(fish)  # removes the fish so it will be placed again and not create multiple copies of it
        fish = Target(random.randint(100, 700), random.randint(50, 500))  # picks a random x and y coordinate for the fish to spawn
        gamesprites.add(fish)
        gamesprites.remove(fishingrod)  # relayers the fishing rod so that it is above the new fish and not underneath it
        gamesprites.add(fishingrod)



    if not gameon:
        all_sprites_list.draw(screen)  # draws sprites before the game has started, so only draws the ones needed for the beginning section
    else:
        screen.fill(BLUE)  # if the game has started it covers the game window with blue
        gamesprites.draw(screen)  # then it draws the sprites needed for the game in the positions they are in as they move

    pygame.display.flip()  # updates the screen

    clock.tick(30)  # creates a slight frame delay that slows down the game enough to not have to use decimals/fractions for speed value

pygame.quit()  # ends the game 
