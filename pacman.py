import os
import time


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 'P', 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


pacman_pos = [5, 8]  
ghost_pos = [1, 1]
score = 0


def print_maze():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in maze:
        print(' '.join(str(cell) if cell != 0 else '.' for cell in row))
    print(f"Score: {score}")
    print("Use WASD to move, Q to quit. Enter your move:")


def move_pacman(direction):
    global score
    new_pos = pacman_pos.copy()
    if direction == 'w':  
        new_pos[0] -= 1
    elif direction == 's':  
        new_pos[0] += 1
    elif direction == 'a':  
        new_pos[1] -= 1
    elif direction == 'd':  
        new_pos[1] += 1


    if (0 <= new_pos[0] < len(maze) and 0 <= new_pos[1] < len(maze[0]) and 
        maze[new_pos[0]][new_pos[1]] != 1):
        if maze[new_pos[0]][new_pos[1]] == 0:  
            score += 10
        maze[pacman_pos[0]][pacman_pos[1]] = ' '
        maze[new_pos[0]][new_pos[1]] = 'P'
        pacman_pos[0], pacman_pos[1] = new_pos[0], new_pos[1]


def move_ghost():
    new_pos = ghost_pos.copy()
    if ghost_pos[0] < pacman_pos[0] and maze[ghost_pos[0] + 1][ghost_pos[1]] != 1:
        new_pos[0] += 1
    elif ghost_pos[0] > pacman_pos[0] and maze[ghost_pos[0] - 1][ghost_pos[1]] != 1:
        new_pos[0] -= 1
    elif ghost_pos[1] < pacman_pos[1] and maze[ghost_pos[0]][ghost_pos[1] + 1] != 1:
        new_pos[1] += 1
    elif ghost_pos[1] > pacman_pos[1] and maze[ghost_pos[0]][ghost_pos[1] - 1] != 1:
        new_pos[1] -= 1
    
    maze[ghost_pos[0]][ghost_pos[1]] = 0 if maze[ghost_pos[0]][ghost_pos[1]] != 'P' else 'P'
    maze[new_pos[0]][new_pos[1]] = 'G'
    ghost_pos[0], ghost_pos[1] = new_pos[0], new_pos[1]


def game_loop():
    while True:
        print_maze()
        move = input().strip().lower()
        
        if move in ['w', 'a', 's', 'd']:
            move_pacman(move)
            move_ghost()  
        elif move == 'q':
            print("Game Over! Final Score:", score)
            break
        else:
            print("Invalid input! Use WASD to move, Q to quit.")
            time.sleep(1)
            continue

        
        if pacman_pos == ghost_pos:
            print_maze()
            print("Game Over! You were caught by the ghost! Final Score:", score)
            break

        time.sleep(0.1)


print("Welcome to Text-Based Pac-Man!")
print("Use WASD to move, Q to quit.")
input("Press Enter to start...")
game_loop()