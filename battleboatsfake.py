import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 25)

# Game variables
board = []
for i in range(10):
    board.append(["O"] * 10)

ships = {
    "A": {"size": 5, "coords": []},
    "B": {"size": 4, "coords": []},
    "C": {"size": 3, "coords": []},
    "D": {"size": 3, "coords": []},
    "E": {"size": 2, "coords": []},
}

def place_ship(board, ship):
    random_row = random.randint(0, len(board) - 1)
    random_col = random.randint(0, len(board[0]) - 1)
    orientation = random.choice(["horizontal", "vertical"])

    if orientation == "horizontal":
        for i in range(ship["size"]):
            if random_col + i >= len(board[0]):
                return place_ship(board, ship)
            if board[random_row][random_col + i] != "O":
                return place_ship(board, ship)
        for i in range(ship["size"]):
            ship["coords"].append((random_row, random_col + i))
            board[random_row][random_col + i] = "X"
    elif orientation == "vertical":
        for i in range(ship["size"]):
            if random_row + i >= len(board):
                return place_ship(board, ship)
            if board[random_row + i][random_col] != "O":
                return place_ship(board, ship)
        for i in range(ship["size"]):
            ship["coords"].append((random_row + i, random_col))
            board[random_row + i][random_col] = "X"

for ship in ships.values():
    place_ship(board, ship)

def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(screen, WHITE, (i * 60, j * 60, 60, 60), 1)
            text = font.render(board[i][j], True, BLACK)
            screen.blit(text, (i * 60 + 25, j * 60 + 20))

def check_hit(coords, ship_coords):
    return coords in ship_coords

def check_win(ships):
    for ship in ships.values():
        if ship["coords"]:
            return False
        else:
            return True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            row = x // 60
            col = y // 60
            if board[row][col] == "O":
                board[row][col] = "M"
            for ship in ships.values():
                if check_hit((row, col), ship["coords"]):
                    for coord in ship["coords"]:
                        board[coord[0]][coord[1]] = "H"
                        ship["coords"] = []
                    if check_win(ships):
                        text = font.render("You Win!", True, RED)
                        screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        running = False

        screen.fill(BLACK)
        draw_board(board)
        pygame.display.update()