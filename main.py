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
POSSIBLE_MOVE = (100,255,100)

# Variables
player_turn_w = "w"
SQUARE_SIZE = 100
selected_square = None
possible_moves = []

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

valid_moves = [
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
    ["F", "F", "F", "F", "F", "F", "F", "F"],
]

# Game Logic for pieces
def is_valid_move(piece, start):
    
    global possible_moves

    start_row, start_col = start
    
    # if a new piece is pressed, it clears the list
    possible_moves = []

    print(piece)
    if piece == "wp":
        
        # check if square ahead is empty for move that is not the pawns first movement
        if board[start_row-1][start_col] == ".":
            possible_moves.append((start_row-1, start_col))
        
        # Check for pawns first move that the 2nd square is empty and square directly in front of pawn is cnot occupied
        # since a pawn can not jump over another piece
        if start_row == 6 and board[start_row-2][start_col] == "." and board[start_row-1][start_col] == ".":
            possible_moves.append((start_row-2, start_col))

        # Capture Moves
        if start_row - 1 > 0:
            if board[start_row - 1][start_col - 1][0] == "b" and (start_col - 1) >= 0:
                possible_moves.append(start_row - 1,start_col - 1)
                                      
            if board[start_row - 1][start_col + 1] == "b" and (start_col + 1) <= 7:                                  
                possible_moves.append(start_row - 1,start_col + 1)

        
        for move in possible_moves:
            print(move)



def highlight_square(position, colour):
    row, col = position
    x = col*SQUARE_SIZE
    y = row*SQUARE_SIZE
    pygame.draw.rect(screen, colour, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))


# visualise the board
def draw_board():
    global possible_moves
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

            # Highlight selected square
            if selected_square == (row, col):
                highlight_square (selected_square, HIGHLIGHTED_SQUARE)

            # Highlight possible moves
            if (row,col) in possible_moves:
                highlight_square ((row,col), POSSIBLE_MOVE)

            # get the relevant piece and paste it in its current position
            piece = board[row][col]
            if piece != ".":
                # identify if the selected piece is white or black
                piece_colour = piece[0]

                piece_image = images.get(piece)
            else: 
                piece_image = None

            if piece_image:
                screen.blit(piece_image,(x,y))


# Function to detect mouse click and select a piece
def handle_click():
    global selected_square, player_turn_w

    # store mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the clicked row and column
    clicked_row = math.ceil(mouse_y / SQUARE_SIZE)-1
    clicked_col = math.floor(mouse_x / SQUARE_SIZE)

    piece = board[clicked_row][clicked_col]
    # If a square is clicked, select the piece if it's there
    if piece != ".":
        piece_color = piece[0]
        if (player_turn_w and piece_color == 'w') or (not player_turn_w and piece_color == 'b'):
            selected_square = (clicked_row, clicked_col)
            is_valid_move(piece, selected_square)
        

    # Show which positions a piece can move to if selected. If one of these
    # positions are selected, update the pieces position, and change the turn
    







# Switch turns



# Main game loop
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

# Execute main function
if __name__ == "__main__":
    main()