import pygame
import serial
import time

# Initialize pygame and create a small window.
pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Motor Control")

# Set up serial connection.
# Adjust '/dev/cu.usbmodem1301' to the correct port for your Arduino.
ser = serial.Serial('/dev/cu.usbmodem1301', 9600)

running = True

while running:
    # Process pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Poll the current state of all keys.
    keys = pygame.key.get_pressed()

    # Control Motor 1 (Up/Down arrows)
    if keys[pygame.K_UP]:
        ser.write(b'u')  # Motor 1 forward/up
    elif keys[pygame.K_DOWN]:
        ser.write(b'd')  # Motor 1 reverse/down

    # Control Motor 2 (Left/Right arrows)
    if keys[pygame.K_LEFT]:
        ser.write(b'i')  # Motor 2 forward/up
    elif keys[pygame.K_RIGHT]:
        ser.write(b'k')  # Motor 2 reverse/down

    # This loop runs repeatedly, so if both sets of keys are pressed,
    # commands for both motors will be sent nearly simultaneously.
    time.sleep(0.05)

ser.close()
pygame.quit()
