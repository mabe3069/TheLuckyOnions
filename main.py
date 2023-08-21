import pygame
import sys
import random
import level_1
import os



pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (245, 220, 29)
GREEN = (0, 255, 0)
GREY = (111,111,111)
# Constants for the screen dimensions
SCREEN_WIDTH = 1242
SCREEN_HEIGHT = 700

Highscore = 0
# Text font
font = pygame.font.Font("freesansbold.ttf", 50)
fontScore = pygame.font.Font("freesansbold.ttf", 35)

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#eceff1'
        #text
        self.text_surf = font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 60)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 60)
        screen.blit(self.text_surf, self.text_rect)
        self.is_clicked()

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#b5bfc8'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
                return True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                return True

        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'






# Constants for the button dimensions
BUTTON_WIDTH = 420
BUTTON_HEIGHT = 60



# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Circle Button Example")


# Create the buttons
button2 = Button(
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    pos= (250,250),
    elevation= 5,
    # color=BLACK,
    text="Letter Mode",

)

button1 = Button(
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    pos= (250,350),
    elevation= 6,
    text="Word Mode",
)


button3 = Button(
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    pos= (250,450),
    elevation= 5,
    text="Exit",
)


# Image imports
BG = pygame.image.load("p4.jpg")
L2 = pygame.image.load("p6.png")
target = pygame.image.load("shot.png")
logo = pygame.image.load("p5.png")
#shotty = pygame.image.load("Shotgun.png")
shot = pygame.image.load("Shot.png")
#cowboy = pygame.image.load("Graphics\Cowboy.png")

# Title and icon
pygame.display.set_caption("Lucky onions!")
icon = pygame.image.load("onion.png")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()



# Target coordinates, these two values should change when the new word appears
textX = 170
textY = 450

# Current word that we are typing. It has an indexed version as well so we can update as we type
currentWord = " "
OGword = " "
indexedWord = list(currentWord)
currentLength = len(indexedWord)
lengthTracker = 0
starttrack = 0  # used to have the intro screen only appear at the begininning

# Random words (This can be changed to any list of words)
words = [
    "asdf",
    "throne",
    "thrill",
    "long",
    "size",
    "hair",
    "plan",
    "nauseating",
    "pull",
    "cagey",
    "berserk",
    "balance",
    "previous",
    "ship",
    "phone",
    "icky",
    "balance",
    "private",
    "hysterical",
    "ashamed",
    "bike",
    "sun",
    "better",
    "early",
    "glow",
    "chase",
    "verse",
    "stale",
    "point",
    "milky",
    "futuristic",
    "cushion",
    "clam",
    "wait",
    "flesh",
    "peaceful",
    "limit",
    "bat",
    "wound",
    "bag",
    "odd",
    "cave",
    "authority",
    "wink",
    "apparel",
    "settle",
    "debonair",
    "turn",
    "slip",
    "seal",
]

# Scoreboard
score = 0
scoreboard = "Words typed: " + str(score)

# All of the functions used in the program


def printer(x, y):
    """ Presents the text onto the screen."""
    show = font.render(currentWord, True, WHITE)
    screen.blit(show, (x, y))


def updatescore(scoreboard):
    """ Updates the score"""
    show = fontScore.render((scoreboard), True, (WHITE))  # pygame surface string
    screen.blit(show, (10, 40))
def updatelives(liveboard):
    show = fontScore.render((liveboard), True, (GREEN))  # pygame surface string
    screen.blit(show, (50, 100))
def intro():
    """ Lays out everything for the starting screen"""

    button1.draw()
    button2.draw()
    button3.draw()



def randomString():
    """Generate a random string of fixed length """
    num = random.randrange(50)
    return words[num]


def randomCoordinates():
    """Generates random coordinates to use when spawning a new word in"""
    textX = random.randrange(550)
    textY = random.randrange(125, 350)
    return textX, textY
def correctLetter():
    """Eliminates the first letter of the word when the user is correct"""
    global textX
    global lengthTracker
    global indexedWord
    global currentWord
    del indexedWord[0]
    temp = ""  # stores the joined string
    currentWord = temp.join(indexedWord)
    lengthTracker += 1  # used to keep track of which letter the user is on
def newGame(song):
    """Eliminates the first letter of the word when the user is correct"""
    global textX
    global lengthTracker
    global indexedWord
    global currentLength
    global currentWords
    global score
    score = -1
    temp = ""  # stores the joined string
    currentWord = temp.join(indexedWord)
    lengthTracker = 1  # used to keep track of which letter the user is on
    pygame.mixer.init()
    background_music_file = os.path.join("Music", song)
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1)


def endGame():
    global OGword
    global currentWord
    global OGindex
    global indexedWord
    global lengthTracker
    print(OGword)
    print(currentWord)
    print(indexedWord)
    currentWord = ""
    indexedWord = ""
    lengthTracker = 0 # resets the letter tracker
def wrongLetter():
    """When a letter is wrong, we want to restart and print out the original word."""
    global lives
    global OGword
    global currentWord
    global OGindex
    global indexedWord
    global lengthTracker
    # reseting the word length
    lives = lives - 1
    currentWord = OGword
    indexedWord = OGindex.copy()
    lengthTracker = 0  # resets the letter tracker

lives = 0
# Loops through the game
tracker = True
tracker2 = False
while tracker:
    if tracker2 == False:
        currentWord = " "
        OGword = " "
        indexedWord = list(currentWord)
        currentLength = len(indexedWord)
        lengthTracker = 0
        starttrack = 0
        lives = 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tracker = False  # This causes the While loop to evaluate False and exit the game



        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
            mouse_pos = pygame.mouse.get_pos()

            if button3.is_clicked() and tracker2 == False:
                print("3")
                tracker = False
                
            if button1.is_clicked() and tracker2 == False:
                print("1")
                starttrack += 1
                tracker2 = True
                newGame("Song_2.mp3")
                


            # if button2.is_clicked():
            #    print("2")
            #    # starttrack += 1
            #    level_1.level_1("lv1.csv", "Song_1.mp3")
            #    level_1.level_1("lv2.csv", "Song_2.mp3")
            #    level_1.level_1("lv3.csv", "Song_3.mp3")
            #    level_1.level_1("lv4.csv", "Song_4.mp3")
            #    level_1.level_1("lv5.csv", "Song_5.mp3")

            if button2.is_clicked() and tracker2 == False:
                print("2")
                # starttrack += 1
                tscore = 0
                rscore = level_1.level_1("lv1.csv", "Song_1.mp3", tscore)
                tscore = rscore + tscore
                if rscore >= 0:
                    rscore = level_1.level_1("lv2.csv", "Song_2.mp3", tscore)
                    tscore = rscore + tscore
                if rscore >= 0:
                    rscore = level_1.level_1("lv3.csv", "Song_3.mp3", tscore)
                    tscore = rscore + tscore
                if rscore >= 0:
                    rscore = level_1.level_1("lv4.csv", "Song_4.mp3", tscore)
                    tscore = rscore + tscore
                if rscore >= 0:
                    rscore = level_1.level_1("lv5.csv", "Song_5.mp3", tscore)
                if tscore > Highscore:
                    Highscore = tscore





        # This is tracking if a key is pressed
        if tracker2:
            if lives <= 0:
                pygame.mixer.music.pause()
                starttrack = 0
                tracker2 = False
                endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    pygame.mixer.music.pause()
                    starttrack = 0
                    tracker2 = False
                    endGame()
                if event.key == pygame.K_a:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "a":
                        correctLetter()
                    else:
                        wrongLetter()

                # Each elif statement is for a certain letter on the keyboard
                elif event.key == pygame.K_b:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "b":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_c:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "c":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_d:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "d":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_e:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "e":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_f:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "f":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_g:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "g":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_h:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "h":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_i:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "i":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_j:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "j":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_k:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "k":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_l:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "l":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_m:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "m":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_n:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "n":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_o:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "o":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_p:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "p":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_q:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "q":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_r:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "r":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_s:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "s":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_t:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "t":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_u:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "u":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_v:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "v":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_w:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "w":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_x:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "x":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_y:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "y":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_z:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == "z":
                        correctLetter()
                    else:
                        wrongLetter()

                elif event.key == pygame.K_SPACE:
                    # if this key is pressed, we need to check if the  letter is the zero index
                    if indexedWord[0] == " ":
                        correctLetter()

    # basic updates
    screen.fill((27, 150, 44))

    if starttrack == 0:
        screen.blit(BG, (0, 0)) #backgroun first.
        screen.blit(logo, (150, 100))



        show = fontScore.render(("guide"), True, (GREY))  # pygame surface string
        screen.blit(show, (750, 500))
        show = fontScore.render(("delete: exit mode"), True, (GREY))  # pygame surface string
        screen.blit(show, (750, 550))
        show = fontScore.render(("esc: pause (let mode)"), True, (GREY))  # pygame surface string
        screen.blit(show, (750, 600))
        show = fontScore.render(("backspace: restart (let mode)"), True, (GREY))  # pygame surface string
        screen.blit(show, (750, 650))

    else:
        screen.blit(L2, (0, 0))




    printer(textX, textY)


    if starttrack == 0:
        # This loop only occurs at the start of the game
        intro()
    else:
        updatescore(scoreboard)

    if lengthTracker == currentLength:
        # this activates if the user types a whole word correctly
        IMAGE_TIME = 30
        if IMAGE_TIME > 0 and (starttrack != 0):
            screen.blit(shot, (textX - 10,  textY - 50))
            IMAGE_TIME -= 1
            score += 1

        starttrack += 1  # used to exit loading screen in the begining

        # sets up for the new word by slecting a new one and updating the score
        scoreboard = "Words typed: " + str(score)  # updates the scoreboard
        currentWord = randomString()  # choses a new word randomly
        OGword = currentWord  # this keeps the original random string
        indexedWord = list(currentWord)
        OGindex = indexedWord.copy()
        currentLength = len(indexedWord)
        lengthTracker = 0  # resets the tracker for the next word
        textX, textY = randomCoordinates()  # new target location

    if starttrack != 0:
        # this spawns shotgun and a new target
        screen.blit(target, (textX - 10, textY + 50))


    clock.tick(60)
    pygame.display.update()



# Things to do in future possibly:
# Two member can type at a same time.
# add a starting menu with advanced options
# calculate words per minute
