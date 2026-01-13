import pygame
from random import randint


pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
CLOCK = pygame.time.Clock()


board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

CELL_SIZE = WIDTH // 3


BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
TEXT_COLOR = (0, 255, 0)


current_player = "X"
game_over = False
winner = None


def draw_grid():
    i = 1
    while i < 3:
        pygame.draw.line(SCREEN, LINE_COLOR, (i*CELL_SIZE, 0), (i*CELL_SIZE, HEIGHT), 5)
        pygame.draw.line(SCREEN, LINE_COLOR, (0, i*CELL_SIZE), (WIDTH, i*CELL_SIZE), 5)
        i += 1
#  Draws the 3x3 Tic Tac Toe grid lines on the screen


def draw_marks():
    row = 0
    while row < 3:
        col = 0
        while col < 3:
            center_x = col*CELL_SIZE + CELL_SIZE//2
            center_y = row*CELL_SIZE + CELL_SIZE//2
            if board[row][col] == "X":
                offset = CELL_SIZE//3
                pygame.draw.line(SCREEN, X_COLOR, (center_x-offset, center_y-offset),
                                 (center_x+offset, center_y+offset), 6)
                pygame.draw.line(SCREEN, X_COLOR, (center_x-offset, center_y+offset),
                                 (center_x+offset, center_y-offset), 6)
            elif board[row][col] == "O":
                pygame.draw.circle(SCREEN, O_COLOR, (center_x, center_y), CELL_SIZE//3, 6)
            col += 1
        row += 1
# Draws X and O symbols on the board based on board state


def check_win():
    # Rows
    if board[0][0] == board[0][1] == board[0][2] != "":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != "":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != "":
        return board[2][0]
    # Columns
    if board[0][0] == board[1][0] == board[2][0] != "":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != "":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != "":
        return board[0][2]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None
#  Checks all win conditions and returns the winner if found


def is_draw():
    if board[0][0] != "" and board[0][1] != "" and board[0][2] != "" \
       and board[1][0] != "" and board[1][1] != "" and board[1][2] != "" \
       and board[2][0] != "" and board[2][1] != "" and board[2][2] != "":
        return check_win() is None
    return False
#Determines whether the game is a draw (board full, no winner)



def AI():
    xord = randint(0, 2)
    yord = randint(0, 2)
    while board[xord][yord] != "":
        xord = randint(0, 2)
        yord = randint(0, 2)
    board[xord][yord] = "O"
# Randomly selects an empty cell and places an O for the AI


def draw_game_over(text):
    font = pygame.font.SysFont(None, 60)
    surface = font.render(text, True, TEXT_COLOR)
    rect = surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    SCREEN.blit(surface, rect)
# Displays the game over message at the center of the screen



key_map = {
    pygame.K_1: (2,0), pygame.K_2: (2,1), pygame.K_3: (2,2),
    pygame.K_4: (1,0), pygame.K_5: (1,1), pygame.K_6: (1,2),
    pygame.K_7: (0,0), pygame.K_8: (0,1), pygame.K_9: (0,2)
}


running = True
while running:
    CLOCK.tick(60)

    events = pygame.event.get()
    idx = 0
    while idx < len(events):
        e = events[idx]
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and not game_over:
            if current_player == "X" and e.key in key_map:
                r, c = key_map[e.key]
                if board[r][c] == "":
                    board[r][c] = "X"
                    winner = check_win()
                    if winner:
                        game_over = True
                    elif is_draw():
                        game_over = True
                        winner = "Draw"
                    else:
                        current_player = "O"
        idx += 1

    if current_player == "O" and not game_over:
        pygame.time.delay(300)
        AI()
        winner = check_win()
        if winner:
            game_over = True
        elif is_draw():
            game_over = True
            winner = "Draw"
        else:
            current_player = "X"

    SCREEN.fill(BG_COLOR)
    draw_grid()
    draw_marks()
    if game_over:
        if winner == "Draw":
            draw_game_over("Draw!")
        else:
            draw_game_over(f"{winner} Wins!")
    pygame.display.flip()
# Main game loop handling input, turns, AI moves, drawing, and game state updates

pygame.quit()



