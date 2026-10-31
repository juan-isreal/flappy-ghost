import pygame
import sys

# 1. Start Pygame
pygame.init()

# 2. Your Setup Strategy: Using a dictionary with a tuple
# If you need them together: screen_config["size"]
# If you need them individually: screen_config["size"][0] or screen_config["size"][1]
screen_config = {
    "size": (600, 800),
    "fps": 60,
    "bg_color": (30, 40, 60)  # Nice dark slate blue
}
key_config = {
    "flap": pygame.K_SPACE,
    "mouseFlap": pygame.MOUSEBUTTONUP,
}
screen = pygame.display.set_mode(screen_config["size"])
pygame.display.set_caption("Flappy Ghost")

# A clock tool to lock the game's speed so it runs smoothly on all computers
clock = pygame.time.Clock()

# 3. Load & Scale Your Player Sprite
# Loads your asset from the assets folder
player_image = pygame.image.load("assets/playersprite.png")
# Scales your 32x32 sprite 4x larger into a crisp 128x128 pixel block
player_image = pygame.transform.scale(player_image, (128, 128))

# Player variables for positioning and speed
player_x = (screen_config["size"][0] // 2) - 64  # Half of screen width minus half of sprite
player_y = (screen_config["size"][1] // 2) - 64  # Half of screen height minus half of sprite
player_speed = -9
velocity = 10
gravity = 0.5
# 4. The Game Loop
running = True
while running:
    # Handle window events (like clicking the close X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONUP):
            velocity = player_speed
            print("velocity: ", velocity)


    velocity += gravity
    if player_y >= 800:
        player_y = 800 / 2
        player_x = 600 / 2
    else:
        player_y += velocity
    # print(velocity)

    # 5. Drawing Section
    screen.fill(screen_config["bg_color"])  # Clear the screen with background color
    screen.blit(player_image, (player_x, player_y))  # Draw your player at their current x, y

    # 6. Refresh and Tick
    pygame.display.flip()  # Update the display
    clock.tick(screen_config["fps"])  # Enforce 60 frames per second limit

# Safe shutdown when loop ends
pygame.quit()
sys.exit()
