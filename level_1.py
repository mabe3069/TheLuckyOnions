import pygame
import random
import sys
import os

pygame.init()

FPS = 60
WIDTH = 1400
HEIGHT = 850
VERTICAL_MARGIN_SIZE = 150
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
SQUARE_SIZE = 50

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

LETTERS = [chr(ord('a') + i) for i in range(26)]
letter_images = {}
assets_path = r"C:\Users\HongM\Hong\TheLuckyOnions\Assets"

for letter in LETTERS:
    image_path = os.path.join(assets_path, f"{letter.upper()}_KEY.png")
    try:
        letter_images[letter.upper()] = pygame.image.load(image_path)
    except pygame.error:
        print(
            f"Image file {image_path} not found for letter {letter}. Make sure to have all letter images from A to Z.")
        sys.exit(1)

class Shape:
    def __init__(self, letter, spawn_time):
        self.shape = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.shape.x = random.randint(VERTICAL_MARGIN_SIZE, WIDTH - VERTICAL_MARGIN_SIZE - self.shape.width)
        self.shape.y = -self.shape.height
        self.letter = letter.upper()
        self.spawn_time = spawn_time
        self.falling_speed = 7

    def move(self):
        self.shape.y += self.falling_speed

    def draw(self, surface):
        letter_image = letter_images.get(self.letter)
        if letter_image:
            if self.letter == 'I':
                new_size = (SQUARE_SIZE // 2, SQUARE_SIZE)
            else:
                new_size = (SQUARE_SIZE, SQUARE_SIZE)
            letter_image = pygame.transform.scale(letter_image, new_size)
            surface.blit(letter_image, self.shape.topleft)
        else:
            pygame.draw.rect(surface, WHITE, self.shape)

    def is_in_hitbox(self):
        hitbox_bottom = HEIGHT // 8
        return self.shape.y + self.shape.height >= HEIGHT - hitbox_bottom and self.shape.y <= HEIGHT

def level_1():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prototype")
    clock = pygame.time.Clock()
    background_image = pygame.image.load(os.path.join("Assets", "BG.png"))
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    shapes = []
    SPAWN_INTERVAL = 1000
    last_spawn_time = 0
    score = 0
    score_font = pygame.font.Font(None, 36)
    pygame.mixer.init()
    background_music_file = os.path.join("Music", "Song_1.mp3")
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1)
    flash_color = None
    flash_end_time = 0
    FLASH_DURATION = 200  # flash duration in milliseconds

    while True:
        correct_key_pressed = False
        pressed_key = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode:
                    pressed_key = event.unicode.upper()

        current_time = pygame.time.get_ticks()

        if pressed_key:
            for shape in shapes[:]:
                if shape.is_in_hitbox() and shape.letter == pressed_key:
                    correct_key_pressed = True
                    shapes.remove(shape)
                    score += 1
                    flash_color = GREEN
                    flash_end_time = current_time + FLASH_DURATION
                elif shape.is_in_hitbox() and shape.letter != pressed_key:
                    flash_color = RED
                    flash_end_time = current_time + FLASH_DURATION

        for shape in shapes[:]:
            if shape.shape.y > HEIGHT:
                shapes.remove(shape)
                if not correct_key_pressed and (current_time - (flash_end_time - FLASH_DURATION)) >= 350:
                    flash_color = YELLOW
                    flash_end_time = current_time + FLASH_DURATION

        if current_time - last_spawn_time >= SPAWN_INTERVAL:
            letter = random.choice(LETTERS)
            shapes.append(Shape(letter, current_time))
            last_spawn_time = current_time

        screen.blit(background_image, (0, 0))
        bottom_rect_height = HEIGHT // 8
        bottom_rect_width = WIDTH - 2 * VERTICAL_MARGIN_SIZE
        bottom_rect = pygame.Surface((bottom_rect_width, bottom_rect_height), pygame.SRCALPHA)

        if flash_color and current_time <= flash_end_time:
            pygame.draw.rect(bottom_rect, flash_color, (0, 0, bottom_rect_width, bottom_rect_height))
        else:
            pygame.draw.rect(bottom_rect, TRANSPARENT, (0, 0, bottom_rect_width, bottom_rect_height))

        pygame.draw.rect(bottom_rect, WHITE, (2, 2, bottom_rect_width - 4, bottom_rect_height - 4), 2)
        screen.blit(bottom_rect, (VERTICAL_MARGIN_SIZE, HEIGHT - bottom_rect_height))

        for shape_obj in shapes:
            shape_obj.move()
            shape_obj.draw(screen)

        score_text = score_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    level_1()
