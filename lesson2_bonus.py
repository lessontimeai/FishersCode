import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_SIZE = 30
BALL_SPEED = 5

# Colors (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Example - Bouncing Ball")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vel_x = BALL_SPEED
ball_vel_y = BALL_SPEED

# Player-controlled rectangle
player_width, player_height = 100, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

def main():
    global ball_x, ball_y, ball_vel_x, ball_vel_y, player_x
    
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get pressed keys for continuous movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        
        # Update ball position
        ball_x += ball_vel_x
        ball_y += ball_vel_y
        
        # Ball collision with walls
        if ball_x <= BALL_SIZE // 2 or ball_x >= WIDTH - BALL_SIZE // 2:
            ball_vel_x = -ball_vel_x
        if ball_y <= BALL_SIZE // 2:
            ball_vel_y = -ball_vel_y
        
        # Ball collision with bottom (reset position)
        if ball_y >= HEIGHT - BALL_SIZE // 2:
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_vel_y = -abs(ball_vel_y)  # Make sure it goes up
        
        # Ball collision with player paddle
        if (ball_y + BALL_SIZE // 2 >= player_y and 
            ball_y - BALL_SIZE // 2 <= player_y + player_height and
            ball_x >= player_x and 
            ball_x <= player_x + player_width):
            ball_vel_y = -abs(ball_vel_y)  # Make ball go up
        
        # Fill screen with background color
        screen.fill(WHITE)
        
        # Draw the ball
        pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), BALL_SIZE // 2)
        
        # Draw the player paddle
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        
        # Draw instructions
        font = pygame.font.Font(None, 36)
        text = font.render("Use LEFT/RIGHT arrows to move paddle", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
        
        # Update the display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(FPS)
    
    # Quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()