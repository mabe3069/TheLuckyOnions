import pygame
import random
import sys
import os

pygame.init()

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
assets_path = r"C:\Users\matth\PycharmProjects\Prototype\Assets"
for letter in LETTERS:
    image_path = os.path.join(assets_path, f"{letter.upper()}_KEY.png")
    try:
        letter_images[letter] = pygame.image.load(image_path)
    except pygame.error:
        print(f"Image file {image_path} not found for letter {letter}. Make sure to have all letter images from A to Z.")
        sys.exit(1)

class Shape:
    def __init__(self, letter, spawn_time):
        self.shape = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.shape.x = random.randint(0, WIDTH - self.shape.width)
        self.shape.y = -self.shape.height
        self.letter = letter
        self.spawn_time = spawn_time
        self.falling_speed = 5  # Adjust the falling speed here (change this value as needed)

    def move(self):
        self.shape.y += self.falling_speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.shape)
        letter_image = letter_images.get(self.letter.upper())
        if letter_image:
            surface.blit(letter_image, (self.shape.x + 5, self.shape.y + 5))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prototype")
    clock = pygame.time.Clock()

    # Load background image
    background_image = pygame.image.load(os.path.join("Assets", "Blue_BG.png"))
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    shapes = []
    SPAWN_INTERVAL = 2000  # 2000ms (2 seconds) interval
    last_spawn_time = 0

    letter_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()

        # Check if it's time to spawn a new shape
        if current_time - last_spawn_time >= SPAWN_INTERVAL:
            letter = LETTERS[letter_index]
            shapes.append(Shape(letter, current_time))
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

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
