import pygame
import time
import sys
import math

# Pygame setup
pygame.init
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Chess Game")

# Establish colors here
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_WHITE = (238,238,210)
LIGHT_BLACK = (70,70,70)
HIGHLIGHTED_SQUARE = (255,182,193)

SQUARE_SIZE = 100

# Load piece images
images = {
    # load white pieces
    "wp": pygame.image.load("wP.png"),
    "wR": pygame.image.load("wR.png"),
    "wN": pygame.image.load("wN.png"),
    "wB": pygame.image.load("wB.png"),
    "wQ": pygame.image.load("wQ.png"),
    "wK": pygame.image.load("wK.png"),

    # load black pieces
    "bp": pygame.image.load("bP.png"),
    "bR": pygame.image.load("bR.png"),
    "bN": pygame.image.load("bN.png"),
    "bB": pygame.image.load("bB.png"),
    "bQ": pygame.image.load("bQ.png"),
    "bK": pygame.image.load("bK.png"),
}

# Variables
selected_square = None

board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    [".", ".",".", ".",".", ".",".", "."],
    [".", ".",".", ".",".", ".",".", "."],
    [".", ".",".", ".",".", ".",".", "."],
    [".", ".",".", ".",".", ".",".", "."],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

# visualise the board
def draw_board():
    for row in range(8):
        for col in range(8):
            # determine the starting point for the current square
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            # identify if it should be a black or white square
            if (row + col) % 2 == 0:
                color = LIGHT_WHITE
            else:
                color = LIGHT_BLACK
            # draw the square
            pygame.draw.rect(screen, color, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

            if selected_square == (row, col):
                pygame.draw.rect(screen, HIGHLIGHTED_SQUARE, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

            # get the relevant piece and paste it in its current position
            piece = board[row][col]
            if piece != ".":
                piece_image = images.get(piece)

            # this eliminates the issue of holding onto the image for future iterations through the board if no piece exists there
            else: 
                piece_image = None

            if piece_image:
                screen.blit(piece_image,(x,y))


# Function to detect mouse click and select a piece
def handle_click():
    global selected_square

    # store mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the clicked row and column
    clicked_row = math.ceil(mouse_y / SQUARE_SIZE)-1
    clicked_col = math.floor(mouse_x / SQUARE_SIZE)

    # If a square is clicked, select the piece if it's there
    if board[clicked_row][clicked_col] != ".":
        selected_square = (clicked_row,clicked_col)


# main game loop
def main():
    running = True
    while running:
        screen.fill(WHITE)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click()  # Call handle_click when mouse is clicked
        
        draw_board()  # Draw the chessboard and pieces
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()