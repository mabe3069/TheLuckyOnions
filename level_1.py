import pygame
import random
import sys
import os
import csv

pygame.init()
from pygame.locals import(
    K_BACKSPACE,
    K_ESCAPE,
)
# Screen dimensions
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)

SQUARE_SIZE = 30

# List of letters
LETTERS = [chr(ord('a') + i) for i in range(26)]

# Load images of letters
letter_images = {}
assets_path = r"C:\Users\benma\OneDrive\Documents\Onions Backup-20230807T003132Z-001\Onions Backup\Assets" #change to whatever your filepath is
for letter in LETTERS:
    image_path = os.path.join(assets_path, f"{letter.upper()}_KEY.png")
    try:
        letter_images[letter.upper()] = pygame.image.load(image_path)
    except pygame.error:
        print(
            f"Image file {image_path} not found for letter {letter}. Make sure to have all letter images from A to Z.")
        sys.exit(1)

class Pause:
    def __init__(self):
        self.pause = False
    def pause_game(self):
        self.pause = True
    def unpause_game(self):
        self.pause = False
    def pause_state(self):
        return self.pause
pause = Pause()
class Shape:
    def __init__(self, letter, spawn_time):
        self.shape = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.shape.x = random.randint(0, WIDTH - self.shape.width)
        self.shape.y = -self.shape.height
        self.letter = letter.upper()
        self.spawn_time = spawn_time
        self.falling_speed = 5  # Adjust the falling speed here (change this value as needed)

    def move(self):
        self.shape.y += self.falling_speed

    def draw(self, surface):
        letter_image = letter_images.get(self.letter)
        if letter_image:
            letter_image = pygame.transform.scale(letter_image, (SQUARE_SIZE, SQUARE_SIZE))
            surface.blit(letter_image, self.shape.topleft)
        else:
            pygame.draw.rect(surface, WHITE, self.shape)

    def is_in_hitbox(self):
        hitbox_bottom = HEIGHT // 8
        return self.shape.y + self.shape.height >= HEIGHT - hitbox_bottom


#hello
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prototype")
    clock = pygame.time.Clock()
    timedelay = 0
    let_list=[]
    time_list=[]
    running = True
    # Load background image
    background_image = pygame.image.load(os.path.join("Assets", "Blue_BG.png"))
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    #call the letter order from a csv file
    with open('lv1.csv', newline='') as csvfile:
        csvread = csv.reader(csvfile, delimiter=',')
        line = 0
        for row in csvread:
            let_list.append(row[0])
            time_list.append(row[1])
            line = line + 1

    shapes = []

    last_spawn_time = 0
    cur_index = 0

    letter_index = 0

    score = 0
    score_font = pygame.font.Font(None, 36)

    # Initialize Pygame mixer for background music
    pygame.mixer.init()

    # Load and play the background music
    background_music_file = os.path.join("Music", "Song_1.mp3")
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1)  # -1 means loop the music
    last_time = 0
    while running == True:
        pressed_key = None

        if pause.pause_state():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        pause.unpause_game()
                        main()
                    if event.key == K_ESCAPE:
                        timedelay = pygame.time.get_ticks() - last_time + timedelay
                        last_time = 0
                        pygame.mixer.music.unpause()
                        pause.unpause_game()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        main()
                    if event.key == K_ESCAPE:
                        last_time = pygame.time.get_ticks()
                        pygame.mixer.music.pause()
                        pause.pause_game()
                    if event.unicode:  # checks if the key corresponds to a character
                        pressed_key = event.unicode.upper()  # normalize to uppercase

            if pressed_key:
                for shape in shapes[:]:  # make a copy of the list to avoid issues while removing items
                    if shape.letter == pressed_key and shape.is_in_hitbox():
                        shapes.remove(shape)
                        score += 1

            current_time = pygame.time.get_ticks()

            if cur_index == line:
                spawn_interval = 5000
            else:
                spawn_interval = int(time_list[cur_index])
            if current_time - last_spawn_time >= spawn_interval + timedelay:
                timedelay = 0
                if cur_index == line:
                    running = False

                else:
                    letter = let_list[cur_index]
                    shapes.append(Shape(letter, current_time))
                    cur_index = cur_index + 1
                    last_spawn_time = current_time
                    letter_index = (letter_index + 1) % len(LETTERS)

        # Draw background image
            screen.blit(background_image, (0, 0))

        # rectangle on the bottom of the screen
            bottom_rect_height = HEIGHT // 8
            bottom_rect = pygame.Surface((WIDTH, bottom_rect_height), pygame.SRCALPHA)
            pygame.draw.rect(bottom_rect, TRANSPARENT, (0, 0, WIDTH, bottom_rect_height))
            pygame.draw.rect(bottom_rect, WHITE, (2, 2, WIDTH - 4, bottom_rect_height - 4), 2)
            screen.blit(bottom_rect, (0, HEIGHT - bottom_rect_height))

        # Move and draw the shapes
            for shape_obj in shapes:
                shape_obj.move()
                shape_obj.draw(screen)

            # Draw score
            score_text = score_font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)
main()