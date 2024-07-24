import random

class Minesweeper:
    def __init__(self, size=5, mines=4):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.hidden_board = [[' ' for _ in range(size)] for _ in range(size)]
        self.flags = set()
        self.moves = []
        self.game_over = False
        self.win = False
        self.place_mines()

    def place_mines(self):
        count = 0
        while count < self.mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.hidden_board[x][y] != '*':
                self.hidden_board[x][y] = '*'
                count += 1

    def adjacent_mines(self, x, y):
        count = 0
        for i in range(max(0, x-1), min(self.size, x+2)):
            for j in range(max(0, y-1), min(self.size, y+2)):
                if self.hidden_board[i][j] == '*':
                    count += 1
        return count

    def open_cell(self, x, y):
        if (x, y) in self.flags or self.board[x][y] != ' ':
            return
        self.moves.append(f"Open ({x}, {y})")
        if self.hidden_board[x][y] == '*':
            self.board[x][y] = '*'
            self.game_over = True
            return
        count = self.adjacent_mines(x, y)
        self.board[x][y] = str(count)
        if count == 0:
            for i in range(max(0, x-1), min(self.size, x+2)):
                for j in range(max(0, y-1), min(self.size, y+2)):
                    if self.board[i][j] == ' ':
                        self.open_cell(i, j)

    def flag_cell(self, x, y):
        if self.board[x][y] == ' ':
            self.flags.add((x, y))
            self.board[x][y] = 'F'
            self.moves.append(f"Flag ({x}, {y})")
        elif self.board[x][y] == 'F':
            self.flags.remove((x, y))
            self.board[x][y] = ' '

    def check_win(self):
        unopened_cells = sum(row.count(' ') for row in self.board)
        if unopened_cells == self.mines:
            self.win = True
            self.game_over = True

    def display_board(self, reveal=False):
        for i in range(self.size):
            for j in range(self.size):
                if reveal:
                    print(self.hidden_board[i][j], end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()
        print()

    def save_game(self):
        with open('minesweeper_game.txt', 'w') as f:
            for row in self.hidden_board:
                f.write(' '.join(row) + '\n')
            f.write('\nMoves:\n')
            for move in self.moves:
                f.write(move + '\n')

def play_game():
    game = Minesweeper()
    while not game.game_over:
        game.display_board()
        action = input("Enter action (open/flag) and coordinates (x y): ").split()
        if len(action) == 3:
            command, x, y = action[0], int(action[1]), int(action[2])
            if command == 'open':
                game.open_cell(x, y)
            elif command == 'flag':
                game.flag_cell(x, y)
            game.check_win()
    game.display_board(reveal=True)
    if game.win:
        print("Congratulations, you win!")
    else:
        print("You hit a mine! Game over.")
    game.save_game()

if __name__ == '__main__':
    play_game()
