import pygame
import serial
import time

# Initialize pygame and create a window.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Motor Control with Cursor")
clock = pygame.time.Clock()

# Set up the serial connection (adjust the port as needed).
ser = serial.Serial('/dev/cu.usbmodem11301', 9600)

# Define dead zone boundaries (central region where no command is sent)
dead_zone_x = (300, 500)  # For horizontal movement
dead_zone_y = (200, 400)  # For vertical movement

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position.
    x, y = pygame.mouse.get_pos()
    
    # --- Mapping Logic for Motor 1 (Horizontal) ---
    if x < dead_zone_x[0]:
        ser.write(b'd')  # Command for Motor 1 reverse/down.
    elif x > dead_zone_x[1]:
        ser.write(b'u')  # Command for Motor 1 forward/up.
    # Else, within dead zone: no command for Motor 1.
    
    # --- Mapping Logic for Motor 2 (Vertical) ---
    if y < dead_zone_y[0]:
        ser.write(b'k')  # Command for Motor 2 reverse/down.
    elif y > dead_zone_y[1]:
        ser.write(b'i')  # Command for Motor 2 forward/up.
    # Else, within dead zone: no command for Motor 2.
    
    # Optional: Visual feedback.
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)
    pygame.display.flip()
    
    clock.tick(30)

ser.close()
pygame.quit()
