import pygame
import random
import math
import level_1


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (245, 220, 29)

# Constants for the screen dimensions
SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 800
BUTTON_RADIUS = 50

class RectButton:
    def __init__(self, x, y, width, height, color, text, text_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height


# Constants for the button dimensions
BUTTON_WIDTH = 280
BUTTON_HEIGHT = 60



class CircleButton:
    def __init__(self, x, y, radius, color, text, text_color, font_size):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        distance = math.sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
        return distance <= self.radius

# Create the Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Circle Button Example")

# Create the button
#
# button1 = CircleButton(
#     x=SCREEN_WIDTH // 2,
#     y=(SCREEN_HEIGHT - SCREEN_HEIGHT//2)+110,
#     radius=BUTTON_RADIUS,
#     color=BLACK,
#     text="Level-2",
#     text_color=WHITE,
#     font_size=30
# )
#
# button2 = CircleButton(
#     x=SCREEN_WIDTH // 2,
#     y=SCREEN_HEIGHT // 2,
#     radius=BUTTON_RADIUS,
#     color=BLACK,
#     text="Level-1",
#     text_color=WHITE,
#     font_size=35
# )
#
#
#
# button3 = CircleButton(
#     x=SCREEN_WIDTH // 2,
#     y=(SCREEN_HEIGHT - SCREEN_HEIGHT//2)+220,
#     radius=BUTTON_RADIUS,
#     color=BLACK,
#     text="Exit",
#     text_color=WHITE,
#     font_size=30
# )


# Create the buttons
button2 = RectButton(
    x=SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
    y=SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    color=BLACK,
    text="Random Letter Mode",
    text_color=WHITE,
    font_size=35
)

button1 = RectButton(
    x=SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
    y=(SCREEN_HEIGHT - SCREEN_HEIGHT//2)+80,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    color=BLACK,
    text="Word Mode",
    text_color=WHITE,
    font_size=30
)

button3 = RectButton(
    x=SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
    y=(SCREEN_HEIGHT - SCREEN_HEIGHT//2)+130+BUTTON_HEIGHT,
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT,
    color=BLACK,
    text="Exit",
    text_color=WHITE,
    font_size=30
)


# Image imports
BG = pygame.image.load("p4.jpg")
L2 = pygame.image.load("p2.jpg")
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


# Text font
font = pygame.font.Font("freesansbold.ttf", 50)
fontScore = pygame.font.Font("freesansbold.ttf", 35)

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
score = -1
scoreboard = "Words typed: " + str(score)

# All of the functions used in the program


def printer(x, y):
    """ Presents the text onto the screen."""
    show = font.render(currentWord, True, YELLOW)
    screen.blit(show, (x, y))


def updatescore(scoreboard):
    """ Updates the score"""
    show = fontScore.render((scoreboard), True, (WHITE))  # pygame surface string
    screen.blit(show, (1100, 40))


def intro():
    """ Lays out everything for the starting screen"""
    #show1 = font.render((" PROTOTYPE"), True, TITLE )  # pygame surface string



    #screen.blit(show1, (70, 100))
   # screen.blit(show2, (70, 130))
    #screen.blit(show3, (70, 160))


    # button1.draw(screen)
    # button2.draw(screen)
    # button3.draw(screen)

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)


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


def wrongLetter():
    """When a letter is wrong, we want to restart and print out the original word."""
    global OGword
    global currentWord
    global OGindex
    global indexedWord
    global lengthTracker
    # reseting the word length
    currentWord = OGword
    indexedWord = OGindex.copy()
    lengthTracker = 0  # resets the letter tracker


# Loops through the game
tracker = True
while tracker:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tracker = False  # This causes the While loop to evaluate False and exit the game



        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button was clicked
            mouse_pos = pygame.mouse.get_pos()
            if button1.is_clicked(mouse_pos):
                print("1")
                starttrack += 1
                correctLetter()


            if button2.is_clicked(mouse_pos):
                print("2")
                #starttrack += 1
                level_1.level_1("lv1.csv", "Song_1.mp3")
                level_1.level_1("lv2.csv", "Song_2.mp3")
                level_1.level_1("lv3.csv", "Song_3.mp3")
                level_1.level_1("lv4.csv", "Song_4.mp3")
                level_1.level_1("lv5.csv", "Song_5.mp3")


            if button3.is_clicked(mouse_pos):
                print("3")
                tracker = False

        # This is tracking if a key is pressed
        if event.type == pygame.KEYDOWN:
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
            screen.blit(shot, (textX - 10, textY - 100))
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
        screen.blit(target, (textX - 10, textY - 100))
        #screen.blit(shotty, (250, 350))
    clock.tick(60)  # this is to control the length of the bullet muzzle flash
    pygame.display.update()



# Things to do in future possibly:
# word changes with cool sound effect, like a bullet firing
# word moves around screen
# randomly generates a word with a generator instead of a predisposed list
# add a starting menu with advanced options
# calculate words per minute
# Speed Letter Recognition game mode
# paragraph calculator that calculates words per minute





